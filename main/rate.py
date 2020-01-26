#!/media/mandeep/MOVIES/KNOWLEDGE/Python/Django/Projects/Live/Rate/env/bin/python

import sys
import getopt
import sysconfig

valid_opts = ['prefix', 'exec-prefix', 'includes', 'libs', 'cflags',
              'ldflags', 'help']

if sys.version_info >= (3, 2):
    valid_opts.insert(-1, 'extension-suffix')
    valid_opts.append('abiflags')
if sys.version_info >= (3, 3):
    valid_opts.append('configdir')


def exit_with_usage(code=1):
    sys.stderr.write("Usage: {0} [{1}]\n".format(
        sys.argv[0], '|'.join('--'+opt for opt in valid_opts)))
    sys.exit(code)

try:
    opts, args = getopt.getopt(sys.argv[1:], '', valid_opts)
except getopt.error:
    exit_with_usage()

if not opts:
    exit_with_usage()

pyver = sysconfig.get_config_var('VERSION')
getvar = sysconfig.get_config_var

opt_flags = [flag for (flag, val) in opts]

if '--help' in opt_flags:
    exit_with_usage(code=0)

for opt in opt_flags:
    if opt == '--prefix':
        print(sysconfig.get_config_var('prefix'))

    elif opt == '--exec-prefix':
        print(sysconfig.get_config_var('exec_prefix'))

    elif opt in ('--includes', '--cflags'):
        flags = ['-I' + sysconfig.get_path('include'),
                 '-I' + sysconfig.get_path('platinclude')]
        if opt == '--cflags':
            flags.extend(getvar('CFLAGS').split())
        print(' '.join(flags))

    elif opt in ('--libs', '--ldflags'):
        abiflags = getattr(sys, 'abiflags', '')
        libs = ['-lpython' + pyver + abiflags]
        libs += getvar('LIBS').split()
        libs += getvar('SYSLIBS').split()
        # add the prefix/lib/pythonX.Y/config dir, but only if there is no
        # shared library in prefix/lib/.
        if opt == '--ldflags':
            if not getvar('Py_ENABLE_SHARED'):
                libs.insert(0, '-L' + getvar('LIBPL'))
            if not getvar('PYTHONFRAMEWORK'):
                libs.extend(getvar('LINKFORSHARED').split())
        print(' '.join(libs))

    elif opt == '--extension-suffix':
        ext_suffix = sysconfig.get_config_var('EXT_SUFFIX')
        if ext_suffix is None:
            ext_suffix = sysconfig.get_config_var('SO')
        print(ext_suffix)

    elif opt == '--abiflags':
        if not getattr(sys, 'abiflags', None):
            exit_with_usage()
        print(sys.abiflags)

    elif opt == '--configdir':
        print(sysconfig.get_config_var('LIBPL'))




# Access WeakSet through the weakref module.
# This code is separated-out because it is needed
# by abc.py to load everything else at startup.

from _weakref import ref

__all__ = ['WeakSet']


class _IterationGuard:
    # This context manager registers itself in the current iterators of the
    # weak container, such as to delay all removals until the context manager
    # exits.
    # This technique should be relatively thread-safe (since sets are).

    def __init__(self, weakcontainer):
        # Don't create cycles
        self.weakcontainer = ref(weakcontainer)

    def __enter__(self):
        w = self.weakcontainer()
        if w is not None:
            w._iterating.add(self)
        return self

    def __exit__(self, e, t, b):
        w = self.weakcontainer()
        if w is not None:
            s = w._iterating
            s.remove(self)
            if not s:
                w._commit_removals()


class WeakSet:
    def __init__(self, data=None):
        self.data = set()
        def _remove(item, selfref=ref(self)):
            self = selfref()
            if self is not None:
                if self._iterating:
                    self._pending_removals.append(item)
                else:
                    self.data.discard(item)
        self._remove = _remove
        # A list of keys to be removed
        self._pending_removals = []
        self._iterating = set()
        if data is not None:
            self.update(data)

    def _commit_removals(self):
        l = self._pending_removals
        discard = self.data.discard
        while l:
            discard(l.pop())

    def __iter__(self):
        with _IterationGuard(self):
            for itemref in self.data:
                item = itemref()
                if item is not None:
                    # Caveat: the iterator will keep a strong reference to
                    # `item` until it is resumed or closed.
                    yield item