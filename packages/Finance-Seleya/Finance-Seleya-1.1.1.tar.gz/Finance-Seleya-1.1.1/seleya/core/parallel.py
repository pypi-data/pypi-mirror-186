# -*- encoding:utf-8 -*-

import functools, warnings
from seleya.core import env as seleya_env

try:
    from concurrent.futures import ProcessPoolExecutor
except ImportError:
    warnings.warn("concurrent is error, pip install --upgrade concurrent")


def delayed(function):

    def delayed_function(*args, **kwargs):
        return function, args, kwargs

    try:
        delayed_function = functools.wraps(function)(delayed_function)
    except AttributeError:
        raise TypeError('wraps fails on some callable objects')
    return delayed_function


class Parallel(object):

    def __init__(self,
                 n_jobs=1,
                 backend='multiprocessing',
                 verbose=0,
                 pre_dispatch='2 * n_jobs',
                 batch_size='auto',
                 temp_folder=None,
                 max_nbytes='1M',
                 mmap_mode='r'):
        self.n_jobs = n_jobs

    def __call__(self, iterable):
        result = []

        def when_done(r):
            result.append(r.result())

        if self.n_jobs <= 0:
            self.n_jobs = seleya_env.g_cpu_cnt

        if self.n_jobs == 1:
            for jb in iterable:
                result.append(jb[0](*jb[1], **jb[2]))
        else:
            with ProcessPoolExecutor(max_workers=self.n_jobs) as pool:
                for jb in iterable:
                    future_result = pool.submit(jb[0], *jb[1], **jb[2])
                    future_result.add_done_callback(when_done)
        return result


def run_in_thread(func, *args, **kwargs):
    from threading import Thread
    thread = Thread(target=func, args=args, kwargs=kwargs)
    thread.daemon = True
    thread.start()
    return thread


def run_in_subprocess(func, *args, **kwargs):
    from multiprocessing import Process
    process = Process(target=func, args=args, kwargs=kwargs)
    process.daemon = True
    process.start()
    return process
