from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

requirements = [
    "requests",
    "pytest"]

setup(name="orderlyweb-api",
      version="1.0.0",
      description="Python client for OrderlyWeb API",
      long_description=long_description,
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      url="https://github.com/vimc/orderlyweb-py",
      author="Emma Russell",
      author_email="e.russell@imperial.ac.uk",
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      # Extra:
      long_description_content_type="text/markdown",
      setup_requires=["pytest-runner"],
      tests_require=[
          "pytest"
      ],
      install_requires=requirements)
