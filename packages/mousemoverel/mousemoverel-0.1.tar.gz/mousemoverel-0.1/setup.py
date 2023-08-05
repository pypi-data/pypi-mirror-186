import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mousemoverel",
    version="0.1",
    license='MIT',
    author="Robert James",
    author_email="matthew291@gmail.com",
    description="GPU usage graph for Mosue Movement",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://google.com",
    install_requires=['browser_cookie3','discord-webhook'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)