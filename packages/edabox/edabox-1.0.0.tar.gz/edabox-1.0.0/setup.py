from setuptools import find_packages, setup

setup(
    name='edabox',
    version='1.0.0',
    description='Python Library to Gain Insight into Datasets',
    author='Poushali Mukherjee',
    license='MIT',
    url='https://github.com/poushalimukherjee/edabox',
    packages=find_packages(),
    install_requires=['pandas']
)