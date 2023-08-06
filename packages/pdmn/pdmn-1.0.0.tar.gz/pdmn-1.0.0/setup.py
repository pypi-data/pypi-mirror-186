import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdmn",
    version="1.0.0",
    author="Simon Vandevelde",
    author_email="s.vandevelde@kuleuven.be",
    description="A package providing a pDMN solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=['openpyxl==3.0.10', 'ply==3.11',
                      'numpy==1.24.1', 'python-dateutil',
                      'problog==2.2.4'],
    entry_points={
        'console_scripts': ['pdmn=pdmn.pdmn:main']
    }
)
