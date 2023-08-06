import setuptools
import os

with open(f'{os.path.abspath(os.path.dirname(__file__))}/README.md', 'r') as f:
    description = f.read()

setuptools.setup(
    name='andromeda-nlp',
    version='0.0.1',
    author='mchaney-dev',
    author_EMAIL='mchaneydev@gmail.com',
    packages=['andromeda'],
    description='Easy longform text generation for creative writing.',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/mchaney-dev/andromeda',
    license='MIT',
    install_requires=['torch', 'happytransformer']
)