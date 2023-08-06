from setuptools import setup, Extension
#from distutils.core import setup, Extension
module1 = Extension(
    'winlin',
    define_macros = [('MAJOR_VERSION', '1'),('MINOR_VERSION', '0')],
    include_dirs = ['/usr/local/include/xdo/'],
    libraries = ['xdo'],
    library_dirs = ['/usr/local/lib/xdo/'],
    sources = ['src/winlin.c']
)

setup(
  name = 'winlin',
  version = '1.0',
  description = 'A tool kit for manipulating windows in linux',
  author = 'Connor Johnson',
  author_email = 'corndog@corn.dog',
  url = 'https://google.com',
  long_description = '#TODO',
  ext_modules = [module1]
)