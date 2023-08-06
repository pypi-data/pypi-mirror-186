from distutils.core import setup
import setuptools
from setuptools import setup, Extension

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
      name="hyper-v",
      packages=setuptools.find_packages(),
      version="0.0.9",
      author="Viktor Gorinskiy",
      author_email="viktor@gorinskiy.ru",
      description="Удаленное управление Hyper-V через winrm",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/viktor-gorinskiy/hyper-v",
	install_requires=[
            'pywinrm==0.4.3',
            'python-nmap==0.7.1'
      ],
	classifiers=[
		"Programming Language :: Python :: 3.8",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)