#!/usr/bin/env python
#
# __COPYRIGHT__
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

__revision__ = "__FILE__ __REVISION__ __DATE__ __DEVELOPER__"

import os
import sys
import TestSCons

import SCons.Platform

_exe = TestSCons._exe

platform = SCons.Platform.platform_default()

if platform == 'posix':
    test_plan = [
      {
          'libversion' : '2',
          'files'      : [ 'libtest.so', 'libtest.so.2', 'test.os' ],
          'instfiles'  : [ 'libtest.so', 'libtest.so.2' ],
          'symlinks'   : [ ('libtest.so', 'libtest.so.2') ],
      },
      {
          'libversion' : '2.5',
          'files'      : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.5', 'test.os' ],
          'instfiles'  : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.5' ],
          'symlinks'   : [ ('libtest.so', 'libtest.so.2.5'), ('libtest.so.2', 'libtest.so.2.5') ],
      },
      {
          'libversion' : '2.5.4',
          'files'      : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.5.4', 'test.os' ],
          'instfiles'  : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.5.4' ],
          'symlinks'   : [ ('libtest.so', 'libtest.so.2.5.4'), ('libtest.so.2', 'libtest.so.2.5.4') ],
      },
      {
          'libversion' : '2.5.4.7.8',
          'files'      : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.5.4.7.8', 'test.os' ],
          'instfiles'  : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.5.4.7.8' ],
          'symlinks'   : [ ('libtest.so', 'libtest.so.2.5.4.7.8'), ('libtest.so.2', 'libtest.so.2.5.4.7.8') ],
      },
      {
          'libversion' : 'aabf114f',
          'files'      : [ 'libtest.so', 'libtest.so.aabf114f', 'test.os' ],
          'instfiles'  : [ 'libtest.so', 'libtest.so.aabf114f' ],
          'symlinks'   : [ ('libtest.so', 'libtest.so.aabf114f') ],
      },
      {
          'libversion' : '2.dfffa11',
          'files'      : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.dfffa11', 'test.os' ],
          'instfiles'  : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.dfffa11' ],
          'symlinks'   : [ ('libtest.so', 'libtest.so.2.dfffa11'), ('libtest.so.2', 'libtest.so.2.dfffa11') ],
      },
    ]
elif platform == 'darwin':
    # All (?) the files we expect will get created in the current directory
    test_plan = [
      {
          'libversion' : '2.5.4',
          'files'      : [ 'libtest.dylib', 'libtest.2.5.4.dylib', 'test.os' ],
          'instfiles'  : [ 'libtest.dylib', 'libtest.2.5.4.dylib' ],
          'symlinks'   : [],
      },
    ]
elif platform == 'cygwin':
    test_plan = [
      {
          'libversion' : '2',
          'files'      : [ 'cygtest-2.dll', 'libtest-2.dll.a', 'libtest.dll.a', 'test.os' ],
          'instfiles'  : [ 'cygtest-2.dll', 'libtest-2.dll.a', 'libtest.dll.a' ],
          'symlinks'   : [ ('libtest.dll.a', 'libtest-2.dll.a') ],
      },
      {
          'libversion' : '2.5',
          'files'      : [ 'cygtest-2-5.dll', 'libtest-2-5.dll.a', 'libtest.dll.a', 'test.os' ],
          'instfiles'  : [ 'cygtest-2-5.dll', 'libtest-2-5.dll.a', 'libtest.dll.a' ],
          'symlinks'   : [ ('libtest.dll.a', 'libtest-2-5.dll.a') ],
      },
      {
          'libversion' : '2.5.4',
          'files'      : [ 'cygtest-2-5-4.dll', 'libtest-2-5-4.dll.a', 'libtest.dll.a', 'test.os' ],
          'instfiles'  : [ 'cygtest-2-5-4.dll', 'libtest-2-5-4.dll.a', 'libtest.dll.a' ],
          'symlinks'   : [ ('libtest.dll.a', 'libtest-2-5-4.dll.a') ],
      },
      {
          'libversion' : '2.5.4.7.8',
          'files'      : [ 'cygtest-2-5-4-7-8.dll', 'libtest-2-5-4-7-8.dll.a', 'libtest.dll.a', 'test.os' ],
          'instfiles'  : [ 'cygtest-2-5-4-7-8.dll', 'libtest-2-5-4-7-8.dll.a', 'libtest.dll.a' ],
          'symlinks'   : [ ('libtest.dll.a', 'libtest-2-5-4-7-8.dll.a') ],
      },
      {
          'libversion' : 'aabf114f',
          'files'      : [ 'cygtest-aabf114f.dll', 'libtest-aabf114f.dll.a', 'libtest.dll.a', 'test.os' ],
          'instfiles'  : [ 'cygtest-aabf114f.dll', 'libtest-aabf114f.dll.a', 'libtest.dll.a' ],
          'symlinks'   : [ ('libtest.dll.a', 'libtest-aabf114f.dll.a') ],
      },
      {
          'libversion' : '2.dfffa11',
          'files'      : [ 'cygtest-2-dfffa11.dll', 'libtest-2-dfffa11.dll.a', 'libtest.dll.a', 'test.os' ],
          'instfiles'  : [ 'cygtest-2-dfffa11.dll', 'libtest-2-dfffa11.dll.a', 'libtest.dll.a' ],
          'symlinks'   : [ ('libtest.dll.a', 'libtest-2-dfffa11.dll.a') ],
      },
    ]
elif platform == 'win32':
    test_plan = [
        {
          'libversion' : '2.5.4',
          'files'      : [ 'test.dll', 'test.lib', 'test.obj' ],
          'instfiles'  : [ 'test.dll', 'test.lib' ],
          'symlinks'   : [],
        },
    ]
elif platform == 'sunos':
    test_plan = [
      {
          'libversion' : '2',
          'files'      : [ 'libtest.so', 'libtest.so.2', 'so_test.os' ],
          'instfiles'  : [ 'libtest.so', 'libtest.so.2' ],
          'symlinks'   : [ ('libtest.so', 'libtest.so.2') ],
      },
      {
          'libversion' : '2.5',
          'files'      : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.5', 'so_test.os' ],
          'instfiles'  : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.5' ],
          'symlinks'   : [ ('libtest.so', 'libtest.so.2.5'), ('libtest.so.2', 'libtest.so.2.5') ],
      },
      {
          'libversion' : '2.5.4',
          'files'      : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.5.4', 'so_test.os' ],
          'instfiles'  : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.5.4' ],
          'symlinks'   : [ ('libtest.so', 'libtest.so.2.5.4'), ('libtest.so.2', 'libtest.so.2.5.4') ],
      },
      {
          'libversion' : '2.5.4.7.8',
          'files'      : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.5.4.7.8', 'so_test.os' ],
          'instfiles'  : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.5.4.7.8' ],
          'symlinks'   : [ ('libtest.so', 'libtest.so.2.5.4.7.8'), ('libtest.so.2', 'libtest.so.2.5.4.7.8') ],
      },
      {
          'libversion' : 'aabf114f',
          'files'      : [ 'libtest.so', 'libtest.so.aabf114f', 'so_test.os' ],
          'instfiles'  : [ 'libtest.so', 'libtest.so.aabf114f' ],
          'symlinks'   : [ ('libtest.so', 'libtest.so.aabf114f') ],
      },
      {
          'libversion' : '2.dfffa11',
          'files'      : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.dfffa11', 'so_test.os' ],
          'instfiles'  : [ 'libtest.so', 'libtest.so.2', 'libtest.so.2.dfffa11' ],
          'symlinks'   : [ ('libtest.so', 'libtest.so.2.dfffa11'), ('libtest.so.2', 'libtest.so.2.dfffa11') ],
      },
    ]
else:
    test_plan = [
        {
          'libversion' : '2.5.4',
          'files'      : [ 'libtest.so', 'test.os' ],
          'instfiles'  : [ ],
        },
    ]

test_c_src = """\
#if _WIN32
__declspec(dllexport)
#endif
int testlib(int n) { return n+1 ; }
"""

test_c_src2 = """\
#if _WIN32
__declspec(dllexport)
#endif
int testlib(int n) { return n+11 ; }
"""

testapp_c_src = """\
#if _WIN32
__declspec(dllimport)
#endif
int testlib(int n);
#include <stdio.h>
int main(int argc, char **argv)
{
int itest ;

itest = testlib(2) ;
printf("results: testlib(2) = %d\\n",itest) ;
return 0 ;
}
"""

for t in test_plan:

    test = TestSCons.TestSCons()

    libversion  = t['libversion']
    files       = t['files']
    symlinks    = t['symlinks']
    instfiles   = t['instfiles']

    test.write('SConstruct', """\
import os
env = Environment()
objs = env.SharedObject('test.c')
mylib = env.SharedLibrary('test', objs, SHLIBVERSION = '%s')
env.Program('testapp1.c', LIBS = mylib, LIBPATH='.')
env.Program('testapp2.c', LIBS = ['test'], LIBPATH='.')
instnode = env.InstallVersionedLib("#/installtest",mylib)
env.Default(instnode)
""" % libversion)

    test.write('test.c', test_c_src)
    test.write('testapp1.c', testapp_c_src)
    test.write('testapp2.c', testapp_c_src)

    test.run(arguments = ['--tree=all'])

    for f in files:
        test.must_exist([ f])
    for f in instfiles:
        test.must_exist(['installtest', f])

    wrong_symlinks = []
    for (linkname,expected) in symlinks:
        try:
            endpoint = os.readlink(linkname)
        except OSError, err:
            print "%s (expected symlink %r -> %r)" % (err, linkname, expected)
            wrong_symlinks.append(linkname)
        else:
            if endpoint != expected:
                print "Wrong symlink: %r -> %r (expected symlink: %r -> %r)" % (linkname, endpoint, linkname, expected)
                wrong_symlinks.append(linkname)

    if wrong_symlinks:
        test.fail_test(wrong_symlinks)

    # modify test.c and make sure it can recompile when links already exist
    test.write('test.c', test_c_src2)

    test.run()

    test.run(arguments = ['-c'])

    for f in files:
        test.must_not_exist([ f])

    for f in instfiles:
        test.must_not_exist(['installtest', f])

test.pass_test()

# Local Variables:
# tab-width:4
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=4 shiftwidth=4:
