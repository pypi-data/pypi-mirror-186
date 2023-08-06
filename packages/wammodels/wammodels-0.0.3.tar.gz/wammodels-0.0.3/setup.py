from setuptools import setup, find_packages

setup(
    name='wammodels',
    version='0.0.3',
    author="Felipe Ardila (WorldArd)",
    description="library for customization modeling .WA",
    include_package_data=True,
    packages=["wammodels"],
    install_requires=[
        'pandas',
        'numpy',
        'statsmodels',
        'patsy' 
    ],
)