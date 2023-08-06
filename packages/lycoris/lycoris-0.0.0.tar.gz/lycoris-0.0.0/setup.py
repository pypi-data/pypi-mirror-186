import setuptools


with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="lycoris",
    version="0.0.0",
    author="Demian Oh",
    author_email="demie.oh@gmail.com",
    description="Lycoris",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/demianoh/lycoris",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.10',
)
