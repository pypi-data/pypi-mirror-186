from setuptools import setup, find_packages

setup(
    name='hyc-utils',
    version='0.5.10',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
        'statsmodels',
        'torch',
        'tomli',
    ],
    extras_require={
        'test': ['pytest', 'scipy'],
    },
)
