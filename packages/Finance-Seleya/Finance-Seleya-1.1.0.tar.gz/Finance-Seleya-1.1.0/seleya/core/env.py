# -*- encoding:utf-8 -*-
import platform, sys, os, warnings, re
from os import path
import numpy as np
import pandas as pd
from seleya.core.fixes import six

g_is_mac_os = platform.system().lower().find(
    "windows") < 0 and sys.platform != "win32"

g_is_py3 = six.PY3
g_is_ipython = True
g_main_pid = os.getpid()

try:
    __IPYTHON__
except NameError:
    g_is_ipython = False

try:
    import psutil
    g_cpu_cnt = psutil.cpu_count(logical=True) * 1
except ImportError:
    if g_is_py3:
        g_cpu_cnt = os.cpu_count()
    else:
        import multiprocessing as mp
        g_cpu_cnt = mp.cpu_count()
except:
    g_cpu_cnt = 4

pd.options.mode.chained_assignment = None
g_display_control = True

if g_display_control:
    pd.options.display.max_rows = 20
    pd.options.display.max_columns = 20
    pd.options.display.precision = 4
    np.set_printoptions(precision=4, suppress=True)

g_ignore_all_warnings = False

g_ignore_lib_warnings = True

if g_ignore_all_warnings:
    warnings.filterwarnings('ignore')
    warnings.simplefilter('ignore')


def str_is_cn(a_str):

    def to_unicode(text, encoding=None, errors='strict'):
        if isinstance(text, six.text_type):
            return text
        if not isinstance(text, (bytes, six.text_type)):
            raise TypeError('to_unicode must receive a bytes, str or unicode '
                            'object, got %s' % type(text).__name__)
        if encoding is None:
            encoding = 'utf-8'
        try:
            decode_text = text.decode(encoding, errors)
        except:
            decode_text = text.decode(
                'gbk' if encoding == 'utf-8' else 'utf-8', errors)
        return decode_text

    cn_re = re.compile(u'[\u4e00-\u9fa5]+')
    try:
        is_cn_path = cn_re.search(to_unicode(a_str)) is not None
    except:
        is_cn_path = True
    return is_cn_path


root_drive = path.expanduser('~')

if str_is_cn(root_drive):
    seleya_source_dir = os.path.abspath(
        os.path.join(os.path.dirname(os.path.realpath(str(__file__))),
                     os.path.pardir))
    root_drive = seleya_source_dir
    print('root_drive is change to {}'.format(root_drive))

g_project_root = path.join(root_drive, 'seleya')

g_project_data_dir = path.join(g_project_root, 'data')

g_project_log_dir = path.join(g_project_root, 'log')

g_project_db_dir = path.join(g_project_root, 'db')

g_project_cache_dir = path.join(g_project_data_dir, 'cache')

g_project_rom_data_dir = path.join(
    path.dirname(path.abspath(path.realpath(__file__))), '../RomDataBu')

g_project_log_info = path.join(g_project_log_dir, 'info.log')

_p_dir = os.path.abspath(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir))

g_plt_figsize = (14, 7)


def init_plot_set():
    """全局plot设置"""
    import seaborn as sns
    sns.set_context('notebook', rc={'figure.figsize': g_plt_figsize})
    sns.set_style("darkgrid")

    import matplotlib
    # conda 5.0后需要添加单独matplotlib的figure设置否则pandas的plot size不生效
    matplotlib.rcParams['figure.figsize'] = g_plt_figsize


init_plot_set()