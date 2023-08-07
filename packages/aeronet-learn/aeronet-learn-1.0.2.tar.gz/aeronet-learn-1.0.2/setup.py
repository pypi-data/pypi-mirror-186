from setuptools import setup, find_packages
# https://youtu.be/GaWs-LenLYE
# https://packaging.python.org/en/latest/tutorials/packaging-projects/
# Run 'pip install .' in the root to test the package locally

# https://towardsdatascience.com/how-to-upload-your-python-package-to-pypi-de1b363a1b3
# Create the dist directory
# python setup.py sdist

# Uploading to TestPyPi
# pip install twine
# twine upload --repository testpypi dist/*

# Specify index-url to download from TestPyPi
# pip install --extra-index-url https://test.pypi.org/simple/ aeronet-learn==1.0.1
# If you don't use the above command syntax then installing dependencies will fail.

# For uploading to prod PyPi. It will prompt for username / password
# twine upload dist/*

setup(
    name='aeronet-learn',
    version='1.0.2',
    author='Logan Zehm',
    author_email='logondz27@gmail.com',
    packages=find_packages(),
    url='https://github.com/Logon27/AeroNet',
    license='LICENSE',
    description='AeroNet is an educational neural network library. It is written entirely using python, numpy, and scipy.',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    install_requires=[
        "numpy",
        "scipy",
        "dill",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
)