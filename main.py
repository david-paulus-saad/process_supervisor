import subprocess
import time
import argparse
import logging

logging.basicConfig(filename='process_supervisor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def start_process(process_name):
    try:
      subprocess.Popen(process_name)
    except FileNotFoundError:
        return False

def check_process(process_name):
    try:
        subprocess.check_output(['pgrep', process_name])
        return True
    except subprocess.CalledProcessError:
        return False

def supervise_process(process_name, wait_time, max_attempts, check_interval):
    attempts = 0
    while attempts < max_attempts:
        if not check_process(process_name):
            logging.info('({}/{}) trying to start the process {}'.format(attempts+1, max_attempts, args.name))
            start_process(process_name)
            attempts += 1
            time.sleep(wait_time)
        else:
            attempts = 0
            time.sleep(check_interval)
    logging.info(f"Failed to start {process_name} after {max_attempts} attempts.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required= True, help="name of the process to supervise")
    parser.add_argument("-w", "--wait", default= "3", help="seconds to wait between attempts to restart service", type=int)
    parser.add_argument("-t", "--tries", default="3", help="number of tries before giving up", type=int)
    parser.add_argument("-i", "--interval", default="3", help="check interval in seconds", type=int)
    args = parser.parse_args()
    
    supervise_process(args.name, args.wait, args.tries, args.interval)
    
    def lambda_handler(event, context):
    supervise_process(event['name'], event['wait'], event['tries'], event['interval'])