import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LeetPride",
    version="0.6.9.001",
    author="Alicia Yingling",
    author_email="AliciaYingling@gmail.com",
    description="LeetPride makes for a beautiful problem solving and learning environment for test and timing data "
                "structures and algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tallicia/LeetPride",
    packages=setuptools.find_packages(),
    install_requires=[
        "colorama",
        "pystyle",
    ],
    license="GNU AGPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
