from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='refconfig',
    version='0.0.3',
    keywords=['configuration', 'refer'],
    description='a flexible and variable-based tool for multi-type configuration, including json, yaml, and python dict',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT Licence',
    url='https://github.com/Jyonn/RefConfig',
    author='Jyonn Liu',
    author_email='i@6-79.cn',
    platforms='any',
    packages=find_packages(),
    install_requires=[
        'smartdict',
        'pyyaml',
    ],
)
