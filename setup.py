from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0',
    description='Clean folder script',
    url='https://github.com/siracencoserghei/core_python_hw_07',
    author='Siracenco Serghei',
    author_email='siracencoserghei@gmail.com',
    packages=find_namespace_packages(),
    long_description=open('README.md').read(),
     entry_points={'console_scripts': ['clean-folder=clean_folder.sort_dir:sort_folder']}
    )
