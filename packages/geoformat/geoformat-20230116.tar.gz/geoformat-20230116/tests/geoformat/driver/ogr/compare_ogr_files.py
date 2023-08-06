import time


def measure_time(func):
    def time_it(*args, **kwargs):
        time_started = time.time()
        func(*args, **kwargs)
        time_elapsed = time.time()
        print("{execute} running time is {sec} seconds".format(
            execute=func.__name__,
            sec=round(time_elapsed - time_started, 4)
            )
        )

    return time_it
