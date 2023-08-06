from setuptools import setup, find_packages

version = {}
with open("ends/version.py") as f:
    exec(f.read(), version)

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

extra_setuptools_args = dict(tests_require=["pytest"])

setup(
    name="burnt-ends",
    version=version["__version__"],
    description="A Python package containing modular, well-tested, utility and statistical functions handy for scientific computing and analysis.",
    maintainer="Cosan Lab, Eshin Jolly",
    maintainer_email="luke.j.chang@dartmouth.edu, eshin.jolly@dartmouth.edu",
    url="http://github.com/cosanlab/neighbors",
    install_requires=requirements,
    packages=find_packages(exclude=["ends/tests"]),
    include_package_data=True,
    package_data={},
    license="MIT",
    keywords=[
        "statistics",
        "utilities",
        "social science",
        "machine-learning",
        "neuroscience",
        "psychology",
        "programming",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
    ],
    **extra_setuptools_args
)
