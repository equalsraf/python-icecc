"""
A django app to display information about icecream scheduler
"""

from distutils.core import setup


DJANGO_ICECC_VERSION = '0.1'

setup(
    name = 'django_icecc',
    version = DJANGO_ICECC_VERSION,
    description = 'Django app to monitor and control icecream schedulers.',

    author = 'Rui Ferreira',
    packages = ['django_icecc'],
    package_data = {'django_icecc':['templates/*.html', 
	                            'templates/icecc/*.html']},
    license = 'BSD',
    requires=[ 'icecc (== %s)' % DJANGO_ICECC_VERSION ],
)
