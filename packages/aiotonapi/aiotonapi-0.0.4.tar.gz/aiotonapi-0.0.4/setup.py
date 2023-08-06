import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aiotonapi",
    version="0.0.4",
    author="nessshon",
    description="Provide access to indexed TON blockchain.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nessshon/aiotonapi",
    packages=setuptools.find_packages(exclude="aiotonapi"),
    python_requires='>=3.10',
    install_requires=[
        "aiohttp>=3.8.3",
        "pydantic>=1.10.4",
        "libscrc>=1.8.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
