import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wfdsl",
    version="0.1.19",
    author="Muhammad Mainul Hossain",
    author_email="mainul.hossain@usask.ca",
    description="Workflow Domain Specific Language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/srlabUsask/wfdsl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
