import setuptools, os
setuptools.setup(
    # State the generic information about the package
    name='uintel',
    version='0.1.1',
    author="Sam Archie",
    author_email="sam.archie@urbanintelligence.co.nz",
    description="Urban Intelligence's collection of Python code for everyday use",
    long_description=open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md')).read(),
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/uintel/pyui/",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',        
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'License :: OSI Approved :: MIT License',        
        'Programming Language :: Python :: 3 :: Only',
        'Natural Language :: English'
        ],
    # State the dependecies of the package
    install_requires=['matplotlib', 'colour', 'slack_sdk', 'sqlalchemy', 'sqlalchemy_utils', 'psycopg2', 'pyyaml', 'tqdm', 'paramiko', 'boto3', 'geopandas', 'esridump', 'requests', 'rasterio', 'gdal', 'topojson'],
    # Include all package files when installing (hence moving over the mplstyle and ttf files)
    packages=setuptools.find_namespace_packages(where="src"),
    package_dir={"": "src"},
    package_data={"uintel.fonts": ["*.ttf"], "uintel.styles": ["*.mplstyle"]},
)