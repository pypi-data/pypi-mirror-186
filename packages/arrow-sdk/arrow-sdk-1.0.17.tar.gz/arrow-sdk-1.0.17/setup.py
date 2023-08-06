from setuptools import setup, find_packages

setup(
    name='arrow-sdk',
    version='1.0.17',
    author='Arrow Markets',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={'arrow_sdk': ['abis/*.json', 'abis/v4/*.json', 'abis/competition/*.json']},
    install_requires=[
        'web3',
        'eth_utils',
        'eth_account',
        'requests',
        'pytz'
    ],
)
