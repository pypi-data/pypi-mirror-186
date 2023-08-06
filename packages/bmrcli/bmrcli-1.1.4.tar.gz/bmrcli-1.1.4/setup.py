from setuptools import setup, find_packages

with open("requirements.txt", "r") as fh:
    install_requires = [line for line in fh.readlines() if line[0] not in ("#", "-")]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bmrcli",
    version="1.1.4",
    description="Command-line tool for BMR HC64 heating controller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dan Keder",
    author_email="dan.keder@protonmail.com",
    url="http://github.com/dankeder/bmrcli",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={"console_scripts": ["bmrcli = bmrcli:main"]},
    python_requires='>=3.6',
    keywords="bmr hc64 heating home-automation",
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
