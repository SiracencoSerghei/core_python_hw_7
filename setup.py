""" setup module """
from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0',
    description='Clean folder script',
    author='Siracenco Serghei',
    author_email='siracencoserghei@gmail.com',
    url='https://github.com/siracencoserghei/core_python_hw_07',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"],
    packages=find_namespace_packages(),
    long_description=open('README.md', "r", encoding="utf-8").read(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.sort_dir:sort_folder']},
    include_package_data=True
    )
