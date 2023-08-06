from setuptools import setup, find_packages

VERSION = "0.0.6"

setup(
    name="langSrc",
    version=VERSION,
    description="A language package manager",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="language package manager",
    author="RhythmLian",
    url="https://github.com/Rhythmicc/langSrc.git",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=[],
    entry_points={},
)
