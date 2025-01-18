import multiprocessing
import os

# Function to be run by each child process
def child_process(name):
    print(f"Child process {name} is starting with PID: {os.getpid()} and PPID: {os.getppid()}")

    # Simulate some work
    import time
    time.sleep(2)
    print(f"Child process {name} has finished with PID: {os.getpid()} and PPID: {os.getppid()}")

# Father process function
def father_process():
    print(f"Father process is starting with PID: {os.getpid()} and PPID: {os.getppid()}")

    child_processes = []
    for i in range(3):  # Create 3 child processes
        process = multiprocessing.Process(target=child_process, args=(f"Process-{i+1}",))
        child_processes.append(process)
        process.start()

    # Wait for all child processes to complete
    for process in child_processes:
        process.join()

    print(f"Father process has finished with PID: {os.getpid()} and PPID: {os.getppid()}")

# Create and start the father process
if __name__ == '__main__':
    father_process()

print("All processes have finished.")
