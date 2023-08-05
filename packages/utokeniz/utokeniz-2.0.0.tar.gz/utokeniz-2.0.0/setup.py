from setuptools import setup
from utoken import __version__

with open('README.md', 'r') as reader:
    readme = reader.read()

setup(
    name='utokeniz',
    author='Jaedson Silva',
    author_email='imunknowuser@protonmail.com',
    description='Create healthy and secure authentication tokens with UTokeniz.',
    long_description=readme,
    long_description_content_type='text/markdown',
    version=__version__,
    packages=['utoken'],
    url='https://github.com/jaedsonpys/utoken',
    license='BSD-3-Clause',
    keywords=['token', 'auth', 'json', 'web', 'login', 'secure']
)