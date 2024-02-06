import timeit
import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("looger")


def timer(number, repeat):
    def wrapper(func):
        runs = timeit.repeat(func, number=number, repeat=repeat)
        log.info(sum(runs) / len(runs))
