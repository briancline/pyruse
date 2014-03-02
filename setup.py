from setuptools import setup
from pyruse.version import version_str

setup(
    name='pyruse',
    version=version_str,
    author='Brian Cline',
    author_email='brian.cline@gmail.com',
    description=('Peruse metadata about Python releases (namely version '
                 'information).'),
    long_description=open('README.rst').read(),
    license='MIT',
    keywords='python release metadata version',
    url='https://github.com/briancline/pyruse',
    packages=['pyruse'],
    install_requires=open('requirements.txt').readlines(),
    test_suite='nose.collector',
    entry_points={
        'console_scripts': [
            'pyruse-versions=pyruse.commands:versions_main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Environment :: Console',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: AIX',
        'Operating System :: POSIX :: HP-UX',
        'Operating System :: POSIX :: IRIX',
        'Operating System :: POSIX :: SunOS/Solaris',
        'Operating System :: POSIX :: BSD :: BSD/OS',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Operating System :: POSIX :: BSD :: NetBSD',
        'Operating System :: POSIX :: BSD :: OpenBSD',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ],
)
