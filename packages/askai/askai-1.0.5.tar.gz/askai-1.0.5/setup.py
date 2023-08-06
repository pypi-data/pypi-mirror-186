from setuptools import find_packages, setup  # type: ignore


setup(
    name="askai",
    version="1.0.5",
    author="Max Fischer",
    description="Your simple terminal helper",
    long_description=open("README.md", encoding="utf8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/maxvfischer/askai",
    download_url="https://github.com/maxvfischer/askai/archive/refs/tags/v1.0.5.tar.gz",
    packages=["askai"],
    install_requires=[
        "click==8.1.3",
        "openai==0.25.0",
        "PyYAML==6.0",
    ],
    entry_points="""
        [console_scripts]
        askai=askai.entrypoint_askai:askai
    """
)
