import sys
from pkg_resources import parse_version
from httplib import HTTPConnection
from xml.etree import ElementTree
from util import cacheable, is_release


PYTHON_HG_HOST = 'hg.python.org'
PYTHON_HG_PATH = '/cpython/atom-tags'
PYTHON_DOWNLOAD_URL = 'http://www.python.org/ftp/python/%(v)s/Python-%(v)s.tgz'
ATOM_NS = 'http://www.w3.org/2005/Atom'
ATOM_XPATH = './/{%(ns)s}entry/{%(ns)s}content' % {'ns': ATOM_NS}


@cacheable
def all_versions():
    versions = []

    try:
        conn = HTTPConnection(PYTHON_HG_HOST)
        conn.request('GET', PYTHON_HG_PATH)
        response = conn.getresponse()

        if response.status != 200:
            raise RuntimeError('Cannot retrieve versions list at this time. '
                               ' (HTTP error %d' % response.status)

        body = response.read()
        root = ElementTree.fromstring(body)

        versions = sorted([v.text[1:] for v in root.iterfind(ATOM_XPATH)],
                          key=lambda x: parse_version(x),
                          reverse=True)

    except Exception as ex:
        sys.stdout.write(ex.message)
        sys.exit(1)

    return versions


def all_releases():
    # TODO: Move _is_release logic into all_releases() to reduce duplication
    #       in all of the methods that follow
    return [x for x in all_versions() if is_release(x)]


def series_versions(series=None):
    if not series:
        return all_versions()

    series_prefix = series + '.'
    return [r for r in all_versions()
            if r == series or series_prefix == r[0:len(series_prefix)]]


def series_releases(series=None):
    if not series:
        return all_releases()

    series_prefix = series + '.'
    return [r for r in all_releases()
            if r == series or series_prefix == r[0:len(series_prefix)]]


def last_version(series=None):
    versions = series_versions(series)
    return versions[0] if versions else None


def last_release(series=None):
    versions = series_releases(series) if series else all_releases()
    return versions[0] if versions else None
