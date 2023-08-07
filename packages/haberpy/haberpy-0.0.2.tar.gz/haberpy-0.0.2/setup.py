from setuptools import setup, find_packages

setup(
    name="haberpy",
    version="0.0.2",
    description="Son dakika haberleri çekebilmenize yarar.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    author="Emre",
    author_email="rewoxirewo@gmail.com",
    license="MIT",
    #classifiers = [
    #"Programming Language :: Python :: 3",
    #"License :: OSI Approved :: MIT License",
    #"Operating System :: OS Independent",
    #],
    keywords=["haberpy","haberpython", "haber", "haber-python", "haber-py", "sondakika", "son-dakika"],
    packages=find_packages(),
    requires=["requests", "beautifulsoup4"]
)