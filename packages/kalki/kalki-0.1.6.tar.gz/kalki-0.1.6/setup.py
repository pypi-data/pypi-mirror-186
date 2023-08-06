from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text() +"\n\n\n"+ (this_directory / "LICENSE").read_text()

setup(
    name="kalki",
    version="0.1.6",
    description="Kalki is a library to create dynamic CSS",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Biswajit Bimoli",
    packages=['kalki'],
    readme = "README.md",
    author_email='biswajitbimoli@gmail.com',
    url='https://github.com/biswajitbimoli/kalki',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
    entry_points={
        'console_scripts': [
            'kalki = bin.kalki:startproject'],
    },
    include_package_data=True,
)