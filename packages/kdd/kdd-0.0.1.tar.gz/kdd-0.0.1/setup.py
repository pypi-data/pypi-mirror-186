from setuptools import setup, find_packages

setup(
    name='kdd',
    version='0.0.1',
    author='Arno De Donder',
    author_email='arno@brainjar.ai',
    description='Helper package for easier management of order data',
    packages=find_packages(),
    install_requires=[
        'pydantic',
        'pandas',
        'matplotlib',
        'msgpack',
        'pdf2image'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
)
