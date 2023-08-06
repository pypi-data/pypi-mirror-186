from setuptools import setup, find_packages

VERSION = '1.2' 
DESCRIPTION = 'Cameralyze No-Code AI Platform'
LONG_DESCRIPTION = 'Offical Cameralyze No-Code AI Platform package'

setup(
        name="cameralyze", 
        version=VERSION,
        author="Cameralyze Inc",
        author_email="info@cameralyze.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["requests==2.28.2"],
        keywords=["Cameralyze", "AI", "Computer Vision", "NLP"]
)