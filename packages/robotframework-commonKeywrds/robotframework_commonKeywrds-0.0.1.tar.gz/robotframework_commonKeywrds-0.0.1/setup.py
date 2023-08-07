""" common keywords library """
from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'robotframework_commonKeywrds'
LONG_DESCRIPTION = 'robot framework package'

# Setting up
setup(
    name="robotframework_commonKeywrds",
    version=VERSION,
    author="Ritika",
    author_email="ritika.kumar90@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "robotframework",
        "robotframework-seleniumlibrary",
        "robotframework-requests",
        "robotframework-jsonlibrary",
        "robotframework-seleniumscreenshots",
        "robotframework-datetime-tz",
        "robotframework-pabot",
        "robotframework-csvlib",
        "robotframework-databaselibrary",
        "boto3"
    ],
    package_data={
        '': ['*.robot'],
    },
    keywords=['arithmetic', 'CommonKeywords', 'mathematics', 'python tutorial', 'Ritika kumar'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]

)
