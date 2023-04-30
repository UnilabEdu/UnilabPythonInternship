import time


class TimerError(Exception):
    pass


class Timer:

    def __init__(self):
        self._start_time = None

    def start(self):
        if self._start_time is not None:
            raise TimerError(f"Timer is already running time.time Please use the .stop() method first.")

        self._start_time = time.perf_counter()

    def stop(self):
        if self._start_time is None:
            raise TimerError(f"Timer is off. Please try, .start() method first.")

        time_delta = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time is {time_delta:0.2f} seconds")

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *execution_information):
        self.stop()


if __name__ == '__main__':
    with Timer():
        time.sleep(2)
