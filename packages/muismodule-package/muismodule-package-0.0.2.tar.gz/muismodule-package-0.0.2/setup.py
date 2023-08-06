from setuptools import setup, find_packages

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name="muismodule-package",
  version="0.0.2",
  author="muis",
  author_email="exlkip@gmail.com",
  description="Testing!",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/mui",
  packages=find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)
