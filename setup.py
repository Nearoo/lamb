import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lamb-sgyger",
    version="0.0.1",
    author="Silas Gyger",
    author_email="silasgyger@gmail.com",
    description="Express lambdas without `lamdbda`",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nearoo/lamb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
