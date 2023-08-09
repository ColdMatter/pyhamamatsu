import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pyhamamatsu",
    version="0.1.0",
    author="Arijit Chakraborty",
    author_email="arijit.phd@gmail.com",
    description="API interface for Hamamatsu camera with DCAM SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ColdMatter/pyhamamatsu",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
