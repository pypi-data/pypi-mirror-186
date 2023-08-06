try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='tothemoon',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    version='0.1.8',
    description='A package for predicting buy and sell signals',
    license='MIT',
    author='Nicolus Rotich',
    author_email='nicholas.rotich@gmail.com',
    install_requires=[
    	"setuptools>=58.1.0",
    	"wheel>=0.37.1",
    	"sklearn>=0.0",
        "scikit-learn>=1.1.2",
    	"h5py>=3.6.0",
        "fire"
    ],
    url='https://nkrtech.com',
    download_url='https://github.com/moinonin/tothemoon/archive/refs/heads/main.zip',
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
)
