from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(name='trainner',  # 包名
      version='0.0.5',  # 版本号
      description='A small package for trainning in deep learning',
      long_description=long_description,
      author='haijie',
      author_email='963493140@qq.com',
      url='',
      install_requires=['torch','numpy','matplotlib'],
      packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      )
