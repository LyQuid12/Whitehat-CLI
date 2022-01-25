from setuptools import setup, find_packages
import re

with open('README.md') as f:
    long_description = f.read()

version = ''
with open('wht/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise TypeError('Version is not set')

def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements

setup(
    name='whitehat-cli',
    version=version,
    author='LyQuid',
    author_email='lyquidpersonal@gmail.com',
    description = 'CLI Version of Whitehat Packages',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='Apache License 2.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points="""
        [console_scripts]
        wht=wht.cli:cli
    """,
)
