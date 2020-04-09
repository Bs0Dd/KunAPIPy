from setuptools import setup, find_packages
import kunapipy


setup(
    name="kunapipy",
    version=kunapipy.__version__,
    url="https://github.com/kesha1225/DnevnikRuAPI",
    author="kesha1225 & Bs()Dd",
    packages=find_packages(),
    description="simple wrapper for kundelik.kz API, based on dnevnikruapi",
    install_requires=["requests", "aiohttp"],
    long_description=open("README.md", encoding="utf-8").read()
)
