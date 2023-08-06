# Auteur : Esteban COLLARD, Nordine EL AMMARI
# Modifications : Reda ID TALEB & Manal LAGHMICH

from setuptools import setup
import os.path

setupdir = os.path.dirname(__file__)

setup(
    name="L1test",
    version="2.0.7",
    author="Mirabelle MARVIE-NEBUT, Maude PUPIN",
    description="A plug-in which adds a test framework",
    long_description="""A plug-in for Thonny which allows you to test your doc examples
 
More info: https://gitlab.univ-lille.fr/mirabelle.nebut/thonny-tests""",
    url="https://gitlab.univ-lille.fr/mirabelle.nebut/thonny-tests",
#    keywords="IDE education programming tests in documentation",
    classifiers=[
        "Topic :: Education :: Testing",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education"
        ],
    platforms=["Windows", "macOS", "Linux"],
    python_requires=">=3.7",
    package_data={
        "thonnycontrib": ["*.py"],
        "thonnycontrib.docs": ["res/*"],
        "thonnycontrib.docstring_generator":["*.py"],
        "thonnycontrib.l1test":["*.py"],
        "thonnycontrib.l1test.classe":["*.py"],
        "thonnycontrib.tests":["*.py"]
    },
    install_requires=["thonny>=3.2.1"],

    packages=["thonnycontrib", "thonnycontrib.docstring_generator", "thonnycontrib.docs", "thonnycontrib.l1test.classe", "thonnycontrib.l1test", "thonnycontrib.tests"],
)
