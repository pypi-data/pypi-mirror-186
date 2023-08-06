from setuptools import setup, find_packages

setup(
    name='nested_inside',
    version='0.2',
    packages=find_packages(),
    url='https://github.com/MrDebugger/nested_inside',
    license='MIT',
    author='Ijaz Ur Rahim',
    author_email='ijazkhan095@gmail.com',
    description='A nested data structure for accessing and modifying values using a delimiter',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords=[
        "parser",
        "json",
        "dict",
        "nested",
        "nested_dict",
        "nested_list",
        "nested_tuple",
        "tuple",
        "list",
        "nested_inside",
    ],
    install_requires=[
        'typing',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
