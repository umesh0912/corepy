import asyncio
import time
import logging


"""
to print log in file 
logging.basicConfig(
    level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log',  # Specify a log file (optional)
    filemode='w'  # Set the file mode ('w' for write, 'a' for append)
)
"""
logging.basicConfig(level=logging.INFO)
log = logging.getLogger("my logger")


async def async_sleep(n):
    log.info(f"before async_sleep {n}")
    log.info(f"hello from async_sleep {n}")
    await asyncio.sleep(n)
    log.info(f"after async_sleep {n}")


async def print_hello():
    log.info("hello from print_hello")


"""
following function works same as synchronously 
async def main():
    log.info("in main")
    start = time.time()
    task = asyncio.create_task(print_hello())
    await async_sleep(2)
    await async_sleep(1)
    await task
    stop = time.time()
    log.info(f"total time taken to complete {(stop - start)}")
    

o/p:
INFO:my logger:hello from print_hello
INFO:my logger:after async_sleep 2
INFO:my logger:before async_sleep 1
INFO:my logger:hello from async_sleep 1
INFO:my logger:after async_sleep 1
INFO:my logger:total time taken to complete 3.0220823287963867

"""



async def coroutine1():
    print("Running coroutine 1")
    await asyncio.sleep(1)
    return "Coroutine 1 result"

async def coroutine2():
    try:
        print("Running coroutine 2")
        await asyncio.sleep(2)
        raise Exception("got some exception")
        return "Coroutine 2 result"
    except Exception as error :
        print("error in Coroutine 2")

async def coroutine3():
    print("Running coroutine 3")
    await asyncio.sleep(0.5)
    return "Coroutine 3 result"

async def main():
    log.info("in main")
    start = time.time()
    try:
        results = await asyncio.gather(coroutine1(), coroutine2(), coroutine2(), return_exceptions=True)

        for result in results:
            if isinstance(result, Exception):
                print(f"An error occurred: {result}")
            else:
                print(f"Result: {result}")

    except Exception as excep:
        print(f"error: {excep}")
    stop = time.time()
    log.info(f"total time taken to complete {(stop - start)}")
"""
running above method concurrently 
INFO:my logger:in main
INFO:my logger:before async_sleep 2
INFO:my logger:hello from async_sleep 2
INFO:my logger:before async_sleep 1
INFO:my logger:hello from async_sleep 1
INFO:my logger:hello from print_hello
INFO:my logger:after async_sleep 1
INFO:my logger:after async_sleep 2
INFO:my logger:total time taken to complete 2.0112760066986084

Process finished with exit code 0

"""

if __name__ == "__main__":
    asyncio.run(main(), debug=True) # creates the event loop
