import time
from threading import Thread


class ProcessTime:
    def __init__(self):
        self.tic = self()
        self.last_run = 0
        self.first_run = True

    def running_time(self, print_: bool = False, reset_mode=False):
        toc = self() - self.tic
        process_time = int(toc * 1000)

        if print_:
            print("Process Time: ", process_time, " ms")

        if reset_mode:
            self.tic = self()

        return process_time

    def timeout(self, cycle_ms: int):
        if self.last_run == 0:
            self.last_run = self()

        time_difference = self() - self.last_run

        if time_difference >= cycle_ms * 0.001:
            self.last_run = self()

            return True
        return False

    def reset(self):
        self.last_run = 0
        self.first_run = True

    def __call__(self):
        return time.perf_counter()


class Loop:
    def __init__(self, timeout: int = 100):
        self.timeout = timeout

    @staticmethod
    def pause(milliseconds: int):
        time.sleep(milliseconds * 0.001)

    def __call__(self):
        self.pause(self.timeout)
        return True


class ThreadIt(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        if kwargs is None:
            kwargs = {}

        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._return = []

        self.start()

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


if __name__ == "__main__":
    t = ProcessTime()
    while True:
        if t.timeout(5000):
            print(t.running_time())
