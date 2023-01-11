
from setuptools import find_packages, setup  # noqa: H301

NAME = "fakepup"
VERSION = "0.0.5"

REQUIRES = [
  "fdsclient @ git+ssh://git@github.com/gdebeaupuis-plenty/fake-fds.git@0.0.3#subdirectory=python/fds_client"
]

setup(
    name=NAME,
    version=VERSION,
    description="Fake PUP",
    author_email="info@plenty.ag",
    url="",
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Fake
    """
)
