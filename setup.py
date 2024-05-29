from setuptools import setup, find_packages

setup(
    name='asvtest',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=['asvtest'],
    install_requires=[
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'asvtest = asvtest:main',
        ],
    },
)