import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="classpyit-pkg-jsmatias", # Replace with your own username
    version="0.0.1",
    author="Jean Matias",
    author_email="smatias.jean@gmail.com",
    description="Simple module to create object from dictionary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jsmatias/classpyit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
