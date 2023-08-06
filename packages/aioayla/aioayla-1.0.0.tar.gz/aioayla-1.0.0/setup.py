from setuptools import setup
import os

setup(
    name="aioayla",
    version="1.0.0",
    author="Dominick Meglio",
    author_email="dmeglio@gmail.com",
    description="Interact with the Ayla IoT Platform",
    license="MIT",
    keywords="ayla",
    packages=["aioayla"],
    url="https://github.com/dcmeglio/aioayla",
    long_description=open(os.path.join(os.path.dirname(__file__), "README.rst")).read(),
    install_requires=["httpx"],
)
