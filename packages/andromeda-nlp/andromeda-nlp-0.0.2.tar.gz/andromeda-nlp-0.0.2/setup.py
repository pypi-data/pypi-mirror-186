import setuptools
import os

os.chdir(os.path.abspath(os.path.dirname(__file__)))
with open('./README.md', 'r') as f:
    description = f.read()

setuptools.setup(
    name='andromeda-nlp',
    version='0.0.2',
    author='mchaney-dev',
    author_email='mchaneydev@gmail.com',
    packages=['andromeda'],
    description='Easy longform text generation for creative writing.',
    long_description=description,
    long_description_content_type='text/markdown',
    url='https://github.com/mchaney-dev/andromeda',
    license='MIT',
    install_requires=['torch', 'happytransformer', 'pytest']
)