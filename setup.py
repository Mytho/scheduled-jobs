from setuptools import find_packages, setup

setup(
    name='scheduled-jobs',
    version='0.0.1',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'APScheduler==3.0.4',
        'requests==2.8.1',
    ],
)
