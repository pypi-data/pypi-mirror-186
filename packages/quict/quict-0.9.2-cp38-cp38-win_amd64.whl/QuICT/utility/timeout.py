import ctypes
import threading


class TimeoutThread(threading.Thread):
    def __init__(self, func, *args, **kwargs):
        threading.Thread.__init__(self)
        self.result = None
        self.exception = None
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            self.result = self.func(*self.args, **self.kwargs)
        except Exception as e:
            self.exception = e


def _async_raise(tid, excobj):
    tid = ctypes.c_long(tid)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(excobj))
    if res == 0:
        raise ValueError("nonexistent thread id")
    elif res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, 0)
        raise SystemExit("PyThreadState_SetAsyncExc failed")


def terminal_thread(thread):
    assert thread.is_alive(), "thread must be started"
    _async_raise(thread.ident, SystemExit)


def timeout():
    def decorator(func):
        def wraps(self, *args, **kwargs):
            t_out = self._timeout
            new_thread = TimeoutThread(func, self, *args, **kwargs)
            new_thread.start()
            new_thread.join(t_out)

            if new_thread.is_alive():
                terminal_thread(new_thread)
                raise TimeoutError("Running time exceed the time limit.")
            elif new_thread.exception:
                raise new_thread.exception
            else:
                return new_thread.result

        return wraps

    return decorator
