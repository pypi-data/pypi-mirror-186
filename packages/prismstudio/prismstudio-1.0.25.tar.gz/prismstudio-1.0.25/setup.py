from setuptools import setup, find_packages

setup(
    name="prismstudio",
    version="1.0.25",
    description="Python Extension for PrismStudio",
    author="Prism39",
    author_email="jmp@prism39.com",
    url="https://www.prism39.com",
    packages=find_packages(),
    python_requires=">=3.7",
    data_files=[("dlls", ["prism/pytransform/_pytransform.dll"])],
    install_requires=[
        "pandas==1.4.1",
        "pytest==7.1.1",
        "mypy==0.941",
        "pyarrow==8.0.0",
        "py7zr==0.18.9",
        "multivolumefile==0.2.3",
        "urllib3==1.26.9",
        "tqdm==4.64.0",
        "orjson==3.7.3",
        "ipywidgets==7.7.1",
        "requests==2.26.0",
        "pyarmor==7.6.1",
        "setuptools==58.1.0",
        "wheel==0.37.1",
        "twine==4.0.1",
        "pydantic==1.10.2",
    ],
    include_package_data=True
)