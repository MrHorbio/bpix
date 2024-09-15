from setuptools import setup, find_packages # type: ignore

setup(

    name='beautypix',
    description='BeautyPix is a versatile Python tool designed for capturing and managing screenshots of specified domains. It efficiently captures screenshots, merges multiple files, and eliminates duplicate values, ensuring a streamlined and organized output. Ideal for web developers, testers, and digital archivists, BeautyPix simplifies the process of monitoring and documenting web content',   
    version='0.1',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    author='Ankush Kumar Rajput',
    url='https://github.com/MrHorbio/BeautyPix/',
    youtube="https://www.youtube.com/@Mr-Horbio",
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
        "selenium",
        "requests",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Windows',
    ],
    python_requires='>=3.6',  # Specify Python versions
)
