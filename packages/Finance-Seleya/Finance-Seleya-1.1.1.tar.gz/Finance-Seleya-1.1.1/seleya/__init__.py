# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import warnings, requests, os

#defaul_url = 'https://ultronsandbox.oss-cn-hangzhou.aliyuncs.com/version/seleya.json'
default_url = 'https://seleya.blob.core.windows.net/nsark'
version_url = "{}/{}/{}".format(os.environ.get('jdw_version_url', default_url),
                                'version', 'seleya.json')
try:
    from . import seleya
    from .DataAPI.db.fetch_engine import FetchEngine as DBFetchEngine
    from .DataAPI.db.db_factory import *

    from .DataAPI import REST as SeleyaAPI
    from .DataAPI import db as DBAPI
except ImportError:
    warnings.warn("pip install --upgrade  SeleyaSDK")

from .Toolset import *

try:
    from ultron.factor.data.standardize import standardize
    from ultron.factor.data.winsorize import winsorize_normal
    from ultron.factor.data.neutralize import neutralize
    from ultron.factor.data.processing import factor_processing
    from ultron import sentry
except ImportError:
    warnings.warn(
        "If you need high-performance computing，please install Finance-Ultron.First make sure that the C++ compilation environment has been installed"
    )

from .version import __version__

session = requests.Session()


def get_version():
    res = requests.get(version_url).json()
    if res.get('code') != 200:
        return '', ''

    remote_version = res['data']['version']
    content = res['data']['content']

    return remote_version, content


def check_version():
    remote_version, content = get_version()
    if not remote_version or remote_version <= __version__:
        return
    print(
        'Seleya version is upgraded from %s to %s, upgrade content %s, execute pip install --upgrade Finance-Seleya'
        % (__version__, remote_version, content))


check_version()