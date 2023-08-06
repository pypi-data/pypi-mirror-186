from setuptools import setup
from setuptools import find_packages


VERSION = "0.1.2"

DESCRIPTION = "Some commonly used computer vision functions and modules"
with open("README.md") as f:
    LONG_DESCRIPTION = f.read()

INSTALL_REQUIRES = [
    "carefree-toolkit>=0.2.11",
    "opencv-python-headless",
    "pillow",
    "scikit-image",
    "scipy>=1.8.0",
]

setup(
    name="carefree-cv",
    version=VERSION,
    packages=find_packages(exclude=("tests",)),
    install_requires=INSTALL_REQUIRES,
    author="carefree0910",
    author_email="syameimaru.saki@gmail.com",
    url="https://github.com/carefree0910/carefree-cv",
    download_url=f"https://github.com/carefree0910/carefree-cv/archive/v{VERSION}.tar.gz",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    keywords="python computer-vision",
)
