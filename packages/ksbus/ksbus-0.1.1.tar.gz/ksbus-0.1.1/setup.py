from setuptools import find_packages, setup

VERSION = '0.1.1'
DESCRIPTION = 'Ksbus client for python https://github.com/kamalshkeir/ksbus'
LONG_DESCRIPTION = 'Ksbus is a client for python https://github.com/kamalshkeir/ksbus, it can be used with korm bus'

# Setting up
setup(
    name="ksbus",
    version=VERSION,
    author="Ksbus (Kamal Shkeir)",
    author_email="<kamalshkeir@yahoo.fr>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['asyncio', 'websockets'],
    keywords=['eventbus', 'bus', 'ksbus', 'korm', 'pubsub', 'websockets'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)