import setuptools
from os import path

VERSION = '0.0.3'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), 'r') as f:
    long_description = f.read()


setuptools.setup(name='uvs-training-sdk',
                 author='Ping Jin',
                 description='A sample python SDK for training and prediction with Unified Vision Service.',
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 url='',
                 version=VERSION,
                 python_requires='>=3.7',
                 license='MIT',
                 keywords='vision datasets classification detection',
                 packages=setuptools.find_packages(),
                 package_data={'': ['resources/*']},
                 install_requires=[
                     'requests',
                     'tqdm'
                 ],
                 classifiers=[
                     'Development Status :: 4 - Beta',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Programming Language :: Python :: 3.7',
                     'Programming Language :: Python :: 3.8',
                     'Programming Language :: Python :: 3.9',
                     'Programming Language :: Python :: 3.10',
                 ],
                 )
