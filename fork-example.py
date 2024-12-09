import os
import time

def child_process(name):
    print(f"Child process {name} is starting with PID: {os.getpid()} and PPID: {os.getppid()}")
    # Simulate some work
    time.sleep(2)
    print(f"Child process {name} has finished with PID: {os.getpid()} and PPID: {os.getppid()}")

def father_process():
    print(f"Father process is starting with PID: {os.getpid()} and PPID: {os.getppid()}")

    for i in range(3):  # Create 3 child processes
        pid = os.fork()
        if pid == 0:
            # In the child process
            child_process(f"Process-{i+1}")
            os._exit(0)  # Exit the child process after it has finished its work
        else:
            # In the father process
            continue

    # Father process waits for all child processes to complete
    for i in range(3):
        os.wait()

    print(f"Father process has finished with PID: {os.getpid()} and PPID: {os.getppid()}")

# Run the father process
if __name__ == '__main__':
    father_process()

print("All processes have finished.")
