import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vvvvvv_text",
    version="1.0.1",
    author="Ally Tilde",
    author_email="alexiatilde@gmail.com",
    description="A GUI interface for creating VVVVVV textboxes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AllyTally/VVVVVV-Text",
    packages=['vvvvvv_text'],
    scripts=['vvvvvv_text'],
    install_requires=['PyQt5'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
