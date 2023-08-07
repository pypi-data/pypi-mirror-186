from setuptools import setup, find_packages
import os
import sys
import pip


install_requires = [
    # "jinja2<2.11.0,>=2.10.1",
    # "unflatten==0.1",
    # "pandas==0.24.2",
    # "expandvars==0.4",
]

extras_require = {}
tests_require = []


if not os.getenv('BUILD_PACKAGE') == '1':
    raise Exception(sys.argv)

print('Broccoli--> Called(imported) broccoli setup.py script')


def get_install_requires():
    print('Broccoli--> Called get_install_requires function')
    # pip.main(['freeze'])
    os.system('rm -fr packages.log && pip freeze > packages.log')

    os.system('rm -fr ../.venv2/lib/python3.10/site-packages/watchtower/')
    os.system('rm -fr ../.venv2/lib/python3.10/site-packages/watchtower-3.0.0.dist-info/')
    
    os.system('rm -fr packages_2.log && pip freeze > packages_2.log')

    with open('packages.log', 'r') as fp:
        1+1
        # raise Exception(fp.read())
    # exit(1)
    if not os.getenv('BUILD_PACKAGE') == '1':
        raise Exception(sys.argv)
    return []


def get_version():
    try:
        with open('version.txt', 'r') as fp:
            ver = fp.read()
    except:
        ver = 3
    
    if os.getenv('BUILD_PACKAGE') == '1':
        # ver = int(ver) + 1
        with open('version.txt', 'w') as fp:
            fp.write(str(ver))
    
    return ver


setup(
    name='broccoli_mwaa_fix',
    description='broccoli_mwaa_fix',
    version=f'0.{get_version()}',
    author='Broccoli Squad',
    # author_email='',
    packages=find_packages(exclude=['tests.*', 'tests', 'thirdparty']),
    # install_requires=install_requires,
    install_requires=get_install_requires(),
    extras_require=extras_require,
    tests_require=tests_require,
    license="TBD",
)
