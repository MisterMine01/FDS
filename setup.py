from setuptools import setup
from pathlib import Path

setup(
    name="fd-system",
    version="1.0.1",
    description="Folder Downloader System for version system",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type='text/markdown',
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
