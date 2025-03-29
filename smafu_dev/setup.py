from setuptools import setup, find_packages

setup(
    name="smafu_dev",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pillow",
        "flask",
        "opencv-python",
        "pydroid3"
    ],
    dependency_links=[
        "git+https://github.com/kramcat/CharacterAI#egg=characterai"
    ],
    entry_points={
        "console_scripts": [
            "smafu_dev=smafu_dev.__init__:install_smafu_dev",
        ],
    },
)
