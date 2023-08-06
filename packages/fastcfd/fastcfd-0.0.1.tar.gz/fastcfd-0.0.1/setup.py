import codefast as cf
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = setuptools.find_packages()
print(packages)
data = [f.lstrip('fastcfd/') for f in cf.io.walk('fastcfd/bins/')]

setuptools.setup(
    name="fastcfd",
    version="0.0.1",
    author="slipper",
    author_email="r2fscg@gmail.com",
    description="NULL",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/private_repo/uuidentifier",
    packages=setuptools.find_packages(),
    package_data={'fastcfd': data},
    install_requires=['codefast', 'fire', 'simauth', 'asyncio'],
    entry_points={'console_scripts': [
        'fastcfd=fastcfd.app:main',
    ]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
