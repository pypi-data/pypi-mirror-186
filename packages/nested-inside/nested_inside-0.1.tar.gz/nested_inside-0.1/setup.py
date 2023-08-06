from setuptools import setup, find_packages

setup(
    name='nested_inside',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/MrDebugger/nested_inside',
    license='MIT',
    author='Ijaz Ur Rahim',
    author_email='ijazkhan095@gmail.com',
    description='A nested data structure for accessing and modifying values using a delimiter',
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
