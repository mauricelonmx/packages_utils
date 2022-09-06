import setuptools
  
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
  
setuptools.setup(
    name="package_utilities",
    version="1.0.0",
    author="Mauricio Londono",
    author_email="mauricio.londono@elektra,com.mx",
    description="Package Utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)