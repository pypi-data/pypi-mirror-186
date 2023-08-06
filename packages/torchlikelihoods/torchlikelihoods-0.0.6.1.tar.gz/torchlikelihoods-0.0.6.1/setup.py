from setuptools import setup, find_packages
import os
import re

classifiers = [
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'License :: OSI Approved :: MIT License',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
]

# Get the long description from the README file
with open('README.md', 'r', encoding='utf8') as fh:
    long_description = fh.read()

# Get version string from module
init_path = os.path.join(os.path.dirname(__file__), 'torchlikelihoods/__init__.py')
with open(init_path, 'r', encoding='utf8') as f:
    version = re.search(r"__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M).group(1)

setup(
    name='torchlikelihoods',
    version=version,
    description='TorchLikelihoods: User-friendly handling of likelihoods in Pytorch',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Pablo Sanchez Martin',
    author_email='psanch2103@gmail.com',
    license='MIT',
    url='https://github.com/psanch21/torchlikelihoods',
    classifiers=classifiers,
    keywords=['Distributions', 'Likelihoods', 'Heterogeneous Data', 'Pytorch',
              'Scalers'],
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=['torch>=1.10',
                      'numpy>=1.19'],
    extras_require={
        'dev': [
            'pytest>=3.7'
        ]
    })
