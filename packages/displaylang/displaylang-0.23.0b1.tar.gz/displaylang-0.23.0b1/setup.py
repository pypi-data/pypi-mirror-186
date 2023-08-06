import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="displaylang",
    version="0.23.0b1",
    license="Apache 2.0",
    url="https://github.com/proofscape/displaylang",
    description="Just enough Python to write displays",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        'pfsc-util>=0.22.8',
        'typeguard==2.13.3',
    ],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
