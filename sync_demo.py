import time
from timeit import default_timer as timer


def run_task(name, seconds):
    print(f'{name} started at: {timer()}')
    time.sleep(seconds)
    print(f'{name} ended at: {timer()}')


start =  timer()
run_task('Task 1', 2)
run_task('Task 2', 1)
run_task('Task 3', 3)

print(f'Total time taken to complete: {timer() - start:.1f}')