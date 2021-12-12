from setuptools import setup

setup(
    name="fd-system",
    version="1.0",
    description="Folder Downloader System for version system",
    url="https://github.com/MisterMine01/FDS",
    author="MisterMine01",
    install_requires=[
        "pcjs-api"
    ],
    packages=["fd-system", "fd-system.utils"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ],
    keywords=["version"]
)
