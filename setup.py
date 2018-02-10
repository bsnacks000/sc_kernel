from setuptools import setup, find_packages
import os

root_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root_dir, 'README.rst'), encoding='utf8') as f:
    long_description = f.read()


requirements=[
    'Click',
    'pexpect==4.3.1',
    'ptyprocess==0.5.2',
    'future',
    'ipykernel'
]
test_requirements =[
    'nose'
]

setup(
    name='sc_kernel',
    version='0.0.0',
    description='A basic IPython kernel REPLwrapper for SuperCollider',
    long_description=long_description,
    url=''
    author='bsnacks000',
    classifiers=[
        'Development Status :: 3 - Alpha'
        'Intended Audience :: SuperCollider users, Developers'
        'License :: MIT License'
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
    packages=find_packages(exclude=['contrib', 'docs', 'tests'])
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts':[
            'install_kernel=sc_kernel.__main__:install_kernel'
        ]
    },
    test_suite='nose.collector',
    tests_require=test_requirements

)
