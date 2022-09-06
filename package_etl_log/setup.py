import setuptools
  
with open("README.md", "r") as fh:
    long_description = fh.read()
  
setuptools.setup(
    name="package_etl_log",
    version="1.0.0",
    author="Juan Carlos Cifuentes Durán",
    author_email="juan.cifuentes@elektra,com.mx",
    description="Package to control and save all logs information in a table",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)