from setuptools import setup
def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="launchscreen",
    version="1.0.4",
    description="Launch Screen for Tkinter",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/mahinbinhasan/launchscreen",
    author="Mahin Bin Hasan (mahinbinhasan)",
    author_email="<allmahin149@gmail.com>",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=[],
    include_package_data=True,
    install_requires=[],
)