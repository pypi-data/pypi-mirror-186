from setuptools import find_packages, setup

setup(
    name='PySimulationEngine',
    packages=find_packages(include=['PySimulationEngine']),
    version='0.1.3',
    description='Python Library to run a simulation with user objects and AIs and display it all through a simple GUI.',
    long_description='BS long desc',
    author='Cristos Criniti',
    license='MIT',
    install_requires=['pyqt5==5.15.7'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)
