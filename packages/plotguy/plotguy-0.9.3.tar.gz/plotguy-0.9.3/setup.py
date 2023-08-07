import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plotguy",
    version="0.9.3",
    author="Plotguy Team",
    author_email="plotguy.info@gmail.com",
    description="Plotguy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[         
        'pandas>=1.5.2',  
        'numpy>=1.24.1',  
        'hkfdb>=2.2',         
        'dash',
        'dash_bootstrap_components',
        'dash_daq',
        'dash_dangerously_set_inner_html',
    ],
    url="https://pypi.org/project/plotguy/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)