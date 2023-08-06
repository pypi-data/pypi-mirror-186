import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='expressintegrations',
    version='1.4.9',
    author="Express Integrations",
    author_email="express.integrations@gmail.com",
    description="Custom Utilities for the Express Integrations platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/expressintegrations",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
