import setuptools


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="useckit",
    version="0.3.3",
    author="BlindForReview.com",
    author_email="mail@blindforreview.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://blindforreview.com",
    packages=setuptools.find_packages(include=['useckit', 'useckit.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=parse_requirements('requirements.txt')
)
