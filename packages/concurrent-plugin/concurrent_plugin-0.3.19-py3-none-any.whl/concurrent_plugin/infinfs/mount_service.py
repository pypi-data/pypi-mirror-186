import socket
import time
import os
from concurrent_plugin.infinfs import infinmount
import json
from mlflow.tracking import MlflowClient
import psutil
from concurrent_plugin.concurrent_backend import MOUNT_SERVICE_READY_MARKER_FILE
import logging
import requests
import subprocess

logger = logging.getLogger()
logger.setLevel(logging.INFO)


FUSE_DEBUG_FILE = '/tmp/fuse_debug.log'
VERBOSE = False

def parse_mount_request(data):
    req = json.loads(data.decode('utf-8'))
    if req['use_cache'].lower() == 'false':
        use_cache = False
    else:
        use_cache = True
    if req['shadow_path'].lower() == 'none':
        shadow_path = None
    else:
        shadow_path = req['shadow_path']
    return req['mount_path'], req['mount_spec'], shadow_path, use_cache


def check_pid(pid):
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


##Returns true if any task is active
def check_pids():
    task_processes = []
    for proc in psutil.process_iter():
        pid = proc.pid
        with open('/proc/' + str(pid) + '/cmdline') as inf:
            cmdline = inf.read()
            if 'mount_main' in cmdline or 'mount_service' in cmdline:
                continue
            if 'python' in cmdline:
                task_processes.append(pid)

    if not task_processes:
        return False

    some_tasks_active = False
    for pid in task_processes:
        alive = check_pid(pid)
        if alive:
            some_tasks_active = True
            break
    return some_tasks_active


def print_info(*args):
    print(*args)


def mount_service_ready():
    ##Create empty marker file
    if not os.path.exists(MOUNT_SERVICE_READY_MARKER_FILE):
        with open(MOUNT_SERVICE_READY_MARKER_FILE, "w"):
            pass

def read_token(token_file):
    with open(token_file, 'r') as tfh:
        token_file_content = tfh.read()
        for token_line in token_file_content.splitlines():
            if token_line.startswith('Token='):
                return token_line[6:]
    return None

def launch_dag_controller():
    if 'DAG_EXECUTION_ID' not in os.environ:
        logger.info('Not a dag execution, skip dag controller')
        return
    infinstor_token = read_token('/root/.concurrent/token')
    mlflow_parallels_uri = os.environ['MLFLOW_CONCURRENT_URI']
    dag_execution_id = os.environ['DAG_EXECUTION_ID']
    dagid = os.environ['DAGID']
    periodic_run_name = os.environ.get('PERIODIC_RUN_NAME')
    periodic_run_frequency = os.getenv('PERIODIC_RUN_FREQUENCY')
    periodic_run_start_time = os.getenv('PERIODIC_RUN_START_TIME')
    periodic_run_end_time = os.getenv('PERIODIC_RUN_END_TIME')

    execute_dag_url = mlflow_parallels_uri.rstrip('/') + '/api/2.0/mlflow/parallels/execdag'
    logger.info(execute_dag_url)
    headers = {'Content-Type': 'application/json', 'Authorization': infinstor_token}
    body = {'dagid': dagid, 'dag_execution_id': dag_execution_id, "periodic_run_name": periodic_run_name}
    if periodic_run_frequency:
      body['periodic_run_frequency'] = periodic_run_frequency
    if periodic_run_start_time:
      body['periodic_run_start_time'] = periodic_run_start_time
    if periodic_run_end_time:
      body['periodic_run_end_time'] = periodic_run_end_time
    attempts_left = max_attempts = 3
    while attempts_left > 0:
        attempts_left -= 1
        try:
            response = requests.post(execute_dag_url, json=body, headers = headers)
            logger.info(f"DAG Controller response: {response}")
            return
        except Exception as ex:
            logger.warning(str(ex))
            print(f'Exception in dag controller call, retry {attempts_left} more times')
            if attempts_left > 0:
                ##wait before retrying
                time.sleep(10 * 2 ** (max_attempts - attempts_left))
    else:
        raise Exception("Dag Controller launch failed multiple times")


def get_mlflow_param(run_id, pname):
    attempts_left = max_attempts = 4
    while attempts_left > 0:
        attempts_left -= 1
        try:
            client = MlflowClient()
            run = client.get_run(run_id)
            if pname in run.data.params:
                return run.data.params[pname]
            else:
                return None
        except Exception:
            print(f'Exception in mlflow call, retry {attempts_left} more times')
            if attempts_left > 0:
                ##wait before retrying
                time.sleep(10 * 2 ** (max_attempts - attempts_left))
    print(f'Failed to get mlflow param {pname} from run {run_id}')

def upload_logs_for_pod(run_id, pod_name, tmp_log_file, container_name=None):
    if container_name:
        get_log_cmd = ['kubectl', 'logs', pod_name, '-c', container_name]
    else:
        get_log_cmd = ['kubectl', 'logs', pod_name]
    try:
        log_content = subprocess.check_output(get_log_cmd)
        with open(tmp_log_file, "w") as fh:
            fh.write(log_content.decode('utf-8'))
    except Exception as ex:
        logger.warning("Failed to fetch logs for {}, {}: {}".format(run_id, pod_name, ex))
        return

    try:
        client = MlflowClient()
        client.log_artifact(run_id, tmp_log_file, artifact_path='.concurrent/logs')
    except Exception as ex:
        logger.warning("Failed upload logs for {}, {}: {}".format(run_id, pod_name, ex))


def update_mlflow_run(run_id, status):
    client = MlflowClient()
    client.set_terminated(run_id, status)


def log_describe_pod(pod_name, run_id):
    describe_file = "/tmp/describe-" + pod_name + ".txt"
    describe_cmd = ['kubectl', 'describe', 'pod', pod_name]
    try:
        desc_content = subprocess.check_output(describe_cmd)
        with open(describe_file, "w") as fh:
            fh.write(desc_content.decode('utf-8'))
        client = MlflowClient()
        client.log_artifact(run_id, describe_file, artifact_path='.concurrent/logs')
    except Exception :
        logger.warning('Failed to log describe pod, try again later')
        return


def fetch_upload_pod_status_logs(run_id, pod_name):
    pods_status_cmd = ['kubectl', 'get', 'pod', pod_name,
                       "-o=jsonpath={range .items[*]}{.metadata.name}{\"\\t\"}{.status.phase}{\"\\n\"}{end}"]
    try:
        pod_status = subprocess.check_output(pods_status_cmd)
    except Exception as ex:
        logger.warning("Failed to get pods status: " + str(ex))
        return

    pod_phase = None
    if pod_status:
        try:
            pn, pphase = pod_status.split()
            if pn == pod_name:
                pod_phase = pphase
            else:
                pod_phase = None
        except Exception as ex:
            print("Exception in getting pod_status")

    if pod_phase:
        side_car_container = "sidecar-" + run_id
        if pod_phase == 'Pending':
            logger.info("{} is in Pending phase. Waiting".format(pod_name))
            log_describe_pod(pod_name, run_id)
            upload_logs_for_pod(run_id, pod_name, "/tmp/run-logs.txt")
            upload_logs_for_pod(run_id, pod_name, f"/tmp/sidecar-logs.txt", container_name=side_car_container)
        elif pod_phase == 'Running':
            logger.info("{} is in Running phase. Waiting".format(pod_name))
            upload_logs_for_pod(run_id, pod_name, "/tmp/run-logs.txt")
            upload_logs_for_pod(run_id, pod_name, "/tmp/sidecar-logs.txt", container_name=side_car_container)
        elif pod_phase == 'Succeeded':
            logger.info("{} is in Succeeded phase".format(pod_name))
            log_describe_pod(pod_name, run_id)
            upload_logs_for_pod(run_id, pod_name, "/tmp/run-logs.txt")
            upload_logs_for_pod(run_id, pod_name, "/tmp/sidecar-logs.txt",
                                container_name=side_car_container)
        elif pod_phase == 'Failed':
            logger.info("{} is in Failed phase".format(pod_name))
            log_describe_pod(pod_name, run_id)
            upload_logs_for_pod(run_id, pod_name, "/tmp/run-logs.txt")
            upload_logs_for_pod(run_id, pod_name, "/tmp/sidecar-logs.txt",
                                container_name=side_car_container)
        elif pod_phase == 'Unknown':
            logger.warning("{} is in Unknown phase".format(pod_name))
            log_describe_pod(pod_name, run_id)
        else:
            logger.warning("{} is in unfamiliar phase {}".format(pod_name, pod_phase))
            log_describe_pod(pod_name, run_id)
    else:
        return
        ## Pod status not available, check job status
        # logger.warning('Pod status not available for ' + pod_name + ", find job status for job " + job_name)
        # # Check for failed job first (more likely job failed)
        # job_status_cmd = ['kubectl', 'wait', 'job/' + job_name, "--for=condition=failed", "--timeout=1s"]
        # try:
        #     job_status = subprocess.check_output(job_status_cmd)
        #     if 'condition met' in job_status:
        #         update_mlflow_run(run_id, "FAILED")
        # except Exception as ex:
        #     logger.warning("Failed to get pods status: " + str(ex))
        #     return


def get_pod_name():
    return os.environ['MY_POD_NAME']


def get_task_exit_code(pod_name, num_attempt=1):
    max_attempts = 3
    cmd = ['kubectl', 'get', 'pods', pod_name,
           "-o=jsonpath='{.status.containerStatuses[0].state.terminated.exitCode}'"]
    try:
        exitCode = subprocess.check_output(cmd)
        exitCode = int(exitCode.decode('utf-8'))
        logger.info("Task container finished with exitCode " + str(exitCode))
        return exitCode
    except Exception as ex:
        logger.error("Couldn't determine exit code..trying {0} more time(s)".format(max_attempts-num_attempt))
        if num_attempt < max_attempts:
            time.sleep(5* 2**num_attempt)
            return get_task_exit_code(pod_name, num_attempt=num_attempt+1)
        else:
            return -1





if __name__ == '__main__':
    print_info("Starting..")
    HOST = "127.0.0.1"
    PORT = 7963
    last_upload_time = time.time()
    start_time = time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(10)
        s.bind((HOST, PORT))
        run_id = os.environ['RUN_ID']
        print('Listening on port {}:{}'.format(HOST, PORT))
        s.listen()
        pod_name = os.environ['MY_POD_NAME']
        mount_service_ready()
        while True:
            print_info('Waiting for request..')
            try:
                conn, addr = s.accept()
            except socket.timeout:
                pass
            else:
                with conn:
                    print(f"Connected by {addr}")
                    data = conn.recv(1024*16)
                    if not data:
                        time.sleep(1)
                        continue
                    try:
                        mount_path, mount_spec, shadow_path, use_cache = parse_mount_request(data)
                        print_info("mount request {}, {}, {}, {}".format(
                            mount_path, mount_spec, shadow_path, use_cache))
                        infinmount.perform_mount(mount_path, mount_spec, shadow_path=shadow_path, use_cache=use_cache)
                        response = "success".encode('utf-8')
                        print_info("mount successful")
                    except Exception as ex:
                        print_info('Exception in mounting: '+str(ex))
                        response = str(ex).encode('utf-8')
                    conn.send(response)
            ##Check if tasks are alive
            curr_time = time.time()
            if curr_time - start_time > 30:
                tasks_alive = check_pids()
                if tasks_alive:
                    if last_upload_time + 30 < curr_time:
                        fetch_upload_pod_status_logs(run_id, pod_name)
                        last_upload_time = curr_time
                else:
                    print_info("Task process done, exiting mount service")
                    exitCode = get_task_exit_code(pod_name)
                    if exitCode == 0:
                        update_mlflow_run(run_id, "FINISHED")
                    else:
                        update_mlflow_run(run_id, "FAILED")
                    fetch_upload_pod_status_logs(run_id, pod_name)
                    launch_dag_controller()
                    exit(0)

