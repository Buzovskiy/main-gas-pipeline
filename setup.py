import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="maingaspipeline-buzovskyi-vitalii", # Replace with your own username
    version="0.0.1",
    author="Buzovskyi Vitalii",
    author_email="buzovskiy.v@gmail.com",
    description="Main gas pipeline calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>=3.8',
    # install_requires=['openpyxl'],
    # cmdclass={
    #     'develop': PostDevelopCommand,
    #     'install': PostInstallCommand,
    # },
)