from setuptools import setup, find_packages

setup(
    name="morning_greetings",  # This is the package name
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'morning_greetings=morning_greetings.main:main',  # Define the script entry point
        ],
    },
)
