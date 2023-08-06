from setuptools import find_packages, setup

desc = """
This package is created for use of the ....."""
setup(
    name='ada_utils',
    packages=find_packages(include=['ada_utils']),
    version='0.2.0',
    description='General purpose Python library for use of Migros Advanced Data Analytics Team',
    author='M.O.',
    license='MIT',
    long_description=desc,
    long_description_content_type='text/x-rst',
    install_requires=['numpy==1.23.5'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.1.2'],
    test_suite='tests'
)