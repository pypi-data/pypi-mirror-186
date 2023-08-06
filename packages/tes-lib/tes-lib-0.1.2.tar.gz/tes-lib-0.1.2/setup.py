import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="tes-lib",
    version="0.1.2",
    author="Laurence Caraccio",
    author_email="laurencecaraccio@hotmail.co.uk",
    description="Test Event Store LIBrary (tes-lib)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/LCaraccio/tes-lib",
    packages=setuptools.find_packages(),
    license="MIT License",
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
