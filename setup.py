import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ois_api_client",
    version="0.0.3",
    author="Peter Kulik",
    author_email="peter@importas.dev",
    description="A python client library for the hungarian Online Invoice System API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/peterkulik/ois_api_client",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Office/Business",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",

    ],
    python_requires='>=3.7.0',
)