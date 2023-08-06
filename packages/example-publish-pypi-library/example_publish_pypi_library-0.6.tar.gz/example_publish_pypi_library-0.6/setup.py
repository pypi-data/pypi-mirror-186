from setuptools import setup, find_packages

setup(
    name='example_publish_pypi_library',
    version='0.6',
    license='MIT',
    author="Marina Sanchez",
    author_email='marina.s.millan@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/msmillan7/example-publish-pypi',
    keywords='example project',
    install_requires=[],

)