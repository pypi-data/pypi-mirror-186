from setuptools import setup, find_packages

with open('README.md', 'r') as readmefile:
    readme = readmefile.read()

setup(
    name='pywifiscan',
    version='1.0.0',
    author='David Ferreira',
    author_email='ferreirad08@gmail.com',
    description='Library to get the received signal strength indicator (RSSI) from Wi-Fi networks.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/ferreirad08/pywifiscan',
    packages=find_packages(),
    install_requires=[],
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
    project_urls={
        "Source": "https://github.com/ferreirad08/pywifiscan",
    }
)
