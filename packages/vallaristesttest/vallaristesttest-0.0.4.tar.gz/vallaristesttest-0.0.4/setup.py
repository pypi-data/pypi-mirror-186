import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vallaristesttest", # Replace with your own username
    version="0.0.4",
    author="Supachai Phoosomma",
    author_email="supachai.pho@gistda.or.th",
    description="A package to processing Vallaris Maps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://v2k.vallarismaps.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires= ['jsonschema','ndjson','geojson','requests','geopandas','pandas', 'rtree', 'numpy', 'rasterio'],
    python_requires='>=3.6',
)