import asyncio
from timeit import default_timer as timer

async def run_task(name, seconds):
    print(f'{name} started at: {timer()}')
    await asyncio.sleep(seconds)
    print(f'{name} ended at: {timer()}')


async def main():
    start = timer()
    await asyncio.gather(
        run_task('Task 1', 2),
        run_task('Task 2', 1),
        run_task('Task 3', 3)
    )
    print(f'Total time taken to complete: {timer() - start:.1f}')

asyncio.run(main())