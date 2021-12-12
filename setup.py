from setuptools import setup

setup(
    name="fds",
    version="1.0",
    description="Folder Downloader System for version system",
    url="https://github.com/MisterMine01/FDS",
    author="MisterMine01",
    install_requires=[
        "pcjs-api"
    ],
    package_dir={"fds": "fds"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ],
    keywords=["version"]
)
