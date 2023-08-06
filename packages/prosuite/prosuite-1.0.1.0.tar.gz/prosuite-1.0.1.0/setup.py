import setuptools
import sys

# build the prosuite package.
# version parameter is read from setup.cfg

setuptools.setup(
    name="prosuite",
    author="Dira GeoSystems",
    author_email="programmers@dirageosystems.ch",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
    url="https://dirageosystems.ch/prosuite.html",
    packages=['prosuite', 'prosuite.generated',
              'prosuite.datatypes', 'prosuite.factories'],
    package_data={'': ['*.txt']},
    install_requires=["lxml", "grpcio>1.4.0", "grpcio-tools"],
    description='An API to configure quality assurance tests for geodata and execute quality verifications on a ProSuite Server',
    long_description="""ProSuite API for Python
     ProSuite is a suite of high-end productivity tools for ArcGIS for data production,
     quality assurance, and cartographic refinement.The ProSuite API for Python allows to configure quality assurance tests for geodata and 
     execute quality verifications on a ProSuite Server. For further information please contact: hello@dirageosystems.ch
    """,
    keywords="gis, arcgis, geodata, prosuite, quality, quality-assurance, qa, test"
)
