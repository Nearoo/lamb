import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lamb-sgyger",
    version="0.0.1",
    author="Silas Gyger",
    author_email="silasgyger@gmail.com",
    description="Provides lamb, a shorter way to expression of functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nearoo/lamb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Code Generators",
    ],
    python_requires='>=3.6',
)
