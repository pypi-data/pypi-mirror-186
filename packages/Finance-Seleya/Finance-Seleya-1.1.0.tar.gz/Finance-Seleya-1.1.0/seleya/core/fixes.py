# -*- encoding:utf-8 -*-
"""
    不同系统的规范进行统一以及问题修正模块
"""

import functools, numbers, sys, scipy, warnings

import numpy as np
import pandas as pd
import sklearn as skl


def _parse_version(version_string):
    version = []
    for x in version_string.split('.'):
        try:
            version.append(int(x))
        except ValueError:
            version.append(x)
    return tuple(version)


"""numpy 版本号tuple"""
np_version = _parse_version(np.__version__)
"""sklearn 版本号tuple"""
skl_version = _parse_version(skl.__version__)
"""pandas 版本号tuple"""
pd_version = _parse_version(pd.__version__)
"""scipy 版本号tuple"""
sp_version = _parse_version(scipy.__version__)

try:
    from inspect import signature, Parameter
except ImportError:
    warnings.warn("inspect is error, pip install --upgrade inspect")

try:
    import six as six
except ImportError:
    warnings.warn("six is error, pip install --upgrade six")

try:
    from six.moves import zip, xrange, range, reduce, map, filter
except ImportError:
    warnings.warn("six is error, pip install --upgrade six")

try:
    # noinspection all
    from six.moves import cPickle as pickle
except ImportError:
    # noinspection all
    from six.moves import cPickle as pickle

if six.PY3:
    Unpickler = pickle._Unpickler
    Pickler = pickle._Pickler
else:
    Unpickler = pickle.Unpickler
    Pickler = pickle.Pickler

if six.PY3:

    def as_bytes(s):
        if isinstance(s, bytes):
            return s
        return s.encode('latin1')
else:
    as_bytes = str

try:
    if six.PY3:
        from functools import lru_cache
    else:
        from functools32 import lru_cache
except ImportError:
    # noinspection PyUnusedLocal
    def lru_cache(maxsize=100):

        def decorate(func):

            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

        return decorate


try:
    from itertools import combinations_with_replacement
except ImportError:

    def combinations_with_replacement(iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        if not n and r:
            return
        indices = [0] * r
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != n - 1:
                    break
            else:
                return
            indices[i:] = [indices[i] + 1] * (r - i)
            yield tuple(pool[i] for i in indices)


if sys.version_info < (2, 7, 0):

    class partial(object):

        def __init__(self, func, *args, **keywords):
            functools.update_wrapper(self, func)
            self.func = func
            self.args = args
            self.keywords = keywords

        def __call__(self, *args, **keywords):
            args = self.args + args
            kwargs = self.keywords.copy()
            kwargs.update(keywords)
            return self.func(*args, **kwargs)
else:
    # noinspection PyUnresolvedReferences
    from functools import partial

if six.PY3:
    from urllib.parse import urlencode
else:
    from urllib import urlencode


def check_random_state(seed):
    if seed is None or seed is np.random:
        return np.random.mtrand._rand
    if isinstance(seed, (numbers.Integral, np.integer)):
        return np.random.RandomState(seed)
    if isinstance(seed, np.random.RandomState):
        return seed
    raise ValueError('%r cannot be used to seed a numpy.random.RandomState'
                     ' instance' % seed)


try:
    skl_ver_big = skl_version >= (0, 18, 0)
except:
    skl_ver_big = True

if skl_ver_big:
    mean_squared_error_scorer = 'neg_mean_squared_error'
    mean_absolute_error_scorer = 'neg_mean_absolute_error'
    median_absolute_error_scorer = 'neg_median_absolute_error'
    log_loss = 'neg_log_loss'

    try:
        from sklearn.model_selection import train_test_split
        from sklearn.model_selection import learning_curve
        from sklearn.model_selection import cross_val_score
        from sklearn.model_selection import GridSearchCV
        from sklearn.mixture import GaussianMixture as GMM

        class KFold(object):

            def __init__(self, n, n_folds=3, shuffle=False, random_state=None):
                if abs(n - int(n)) >= np.finfo('f').eps:
                    raise ValueError("n must be an integer")
                self.n = int(n)

                if abs(n_folds - int(n_folds)) >= np.finfo('f').eps:
                    raise ValueError("n_folds must be an integer")
                self.n_folds = n_folds = int(n_folds)

                if n_folds <= 1:
                    raise ValueError(
                        "k-fold cross validation requires at least one"
                        " train / test split by setting n_folds=2 or more,"
                        " got n_folds={0}.".format(n_folds))
                if n_folds > self.n:
                    raise ValueError(
                        ("Cannot have number of folds n_folds={0} greater"
                         " than the number of samples: {1}.").format(
                             n_folds, n))

                if not isinstance(shuffle, bool):
                    raise TypeError("shuffle must be True or False;"
                                    " got {0}".format(shuffle))
                self.shuffle = shuffle
                self.random_state = random_state

                self.idxs = np.arange(n)
                if shuffle:
                    rng = check_random_state(self.random_state)
                    rng.shuffle(self.idxs)

            def __iter__(self):
                ind = np.arange(self.n)
                for test_index in self._iter_test_masks():
                    train_index = np.logical_not(test_index)
                    train_index = ind[train_index]
                    test_index = ind[test_index]
                    yield train_index, test_index

            def _iter_test_masks(self):
                for test_index in self._iter_test_indices():
                    test_mask = self._empty_mask()
                    test_mask[test_index] = True
                    yield test_mask

            def _empty_mask(self):
                return np.zeros(self.n, dtype=np.bool)

            def _iter_test_indices(self):
                n = self.n
                n_folds = self.n_folds
                fold_sizes = (n // n_folds) * np.ones(n_folds, dtype=np.int)
                fold_sizes[:n % n_folds] += 1
                current = 0
                for fold_size in fold_sizes:
                    start, stop = current, current + fold_size
                    yield self.idxs[start:stop]
                    current = stop

            def __repr__(self):
                return '%s.%s(n=%i, n_folds=%i, shuffle=%s, random_state=%s)' % (
                    self.__class__.__module__,
                    self.__class__.__name__,
                    self.n,
                    self.n_folds,
                    self.shuffle,
                    self.random_state,
                )

            def __len__(self):
                return self.n_folds

    except ImportError:
        from sklearn.cross_validation import train_test_split
        from sklearn.cross_validation import KFold
        from sklearn.cross_validation import cross_val_score
        from sklearn.learning_curve import learning_curve
        from sklearn import cross_validation
        from sklearn.grid_search import GridSearchCV
        from sklearn.mixture import GMM
else:
    mean_squared_error_scorer = 'mean_squared_error'
    mean_absolute_error_scorer = 'mean_absolute_error'
    median_absolute_error_scorer = 'median_absolute_error'
    log_loss = 'log_loss'

    from sklearn.cross_validation import train_test_split
    from sklearn.cross_validation import KFold
    from sklearn.cross_validation import cross_val_score
    from sklearn.learning_curve import learning_curve
    from sklearn import cross_validation
    from sklearn.grid_search import GridSearchCV
    from sklearn.mixture import GMM

try:
    if np_version < (1, 8, 1):

        def array_equal(a1, a2):
            # copy-paste from numpy 1.8.1
            try:
                a1, a2 = np.asarray(a1), np.asarray(a2)
            except:
                return False
            if a1.shape != a2.shape:
                return False
            return bool(np.asarray(a1 == a2).all())
    else:
        from numpy import array_equal
except:
    from numpy import array_equal

try:
    if sp_version < (0, 13, 0):

        def rankdata(a, method='average'):
            if method not in ('average', 'min', 'max', 'dense', 'ordinal'):
                raise ValueError('unknown method "{0}"'.format(method))

            arr = np.ravel(np.asarray(a))
            algo = 'mergesort' if method == 'ordinal' else 'quicksort'
            sorter = np.argsort(arr, kind=algo)

            inv = np.empty(sorter.size, dtype=np.intp)
            inv[sorter] = np.arange(sorter.size, dtype=np.intp)

            if method == 'ordinal':
                return inv + 1

            arr = arr[sorter]
            obs = np.r_[True, arr[1:] != arr[:-1]]
            dense = obs.cumsum()[inv]

            if method == 'dense':
                return dense

            count = np.r_[np.nonzero(obs)[0], len(obs)]

            if method == 'max':
                return count[dense]

            if method == 'min':
                return count[dense - 1] + 1

            return .5 * (count[dense] + count[dense - 1] + 1)
    else:
        from scipy.stats import rankdata
except:
    from scipy.stats import rankdata
