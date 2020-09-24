import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ois_client_sdk",
    version="0.0.1",
    author="Peter Kulik",
    author_email="peter@importas.dev",
    description="A python client library for the hungarian Online Invoice System API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/peterkulik/ois_client_sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Topic :: Text Processing :: Markup :: XML",
        "License :: OSI Approved :: MIT License",

    ],
    python_requires='>=3.6.1',
)