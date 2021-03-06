import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="LeetPride",
    version="0.6.9.2.7",
    author="Alicia Yingling",
    author_email="AliciaYingling@gmail.com",
    description="LeetPride makes for a beautiful problem solving and learning environment for test and timing data "
                "structures and algorithms. Happy Pride everyone and may the leet coding favor your fortune.",
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
    include_package_data=True,
    python_requires=">=3.6",
)
