from setuptools import setup, find_packages
import kunapipy


setup(
    name="kunapipy",
    version=kunapipy.__version__,
    url="https://github.com/Bs0Dd/KunAPIPy",
    author="kesha1225 & Bs()Dd",
    packages=find_packages(),
    description="simple wrapper for kundelik.kz API, based on pydnevnikruapi",
    install_requires=["requests", "aiohttp"],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown"
)
