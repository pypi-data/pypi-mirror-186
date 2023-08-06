from setuptools import setup, find_packages

with open("README.md", "r") as stream:
    long_description = stream.read()

# long_description = "An universal wrapper (and useful tool) to make event / commands in python"

setup(
    name='easy-playlist',
    version="1.3.0",
    url='https://github.com/ThePhoenix78/easy-playlist',
    download_url='https://github.com/ThePhoenix78/easy-playlist/tarball/master',
    license='MIT',
    author='ThePhoenix78',
    author_email='thephoenix788@gmail.com',
    description='An universal wrapper (and useful tool) to make event / commands in python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=[
        "playlist",
        "music manager",
        "MP3"
    ],
    install_requires=[
        'easy-events>=1.8.4'
    ],
    setup_requires=[
        'wheel'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages()
    # packages=["sdist", "bdist_wheel"]
    # python_requires='>=3.6',
)
