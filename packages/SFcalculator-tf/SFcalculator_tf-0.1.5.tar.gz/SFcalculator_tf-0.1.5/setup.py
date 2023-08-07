from setuptools import setup, find_packages

# Get version number
def getVersionNumber():
    with open("SFC_TF/VERSION", "r") as vfile:
        version = vfile.read().strip()
    return version

__version__ = getVersionNumber()

def choose_proper_project( requires ):
    '''
    https://stackoverflow.com/questions/14036181/
    provide-a-complex-condition-in-install-requires-python-
    setuptoolss-setup-py
    '''
    import pkg_resources
    for req in requires:
       try:
           pkg_resources.require( req )
           return [ req ]
       except pkg_resources.DistributionNotFound :
           pass
       pass
    print("There are no proper project installation available")
    print("To use this app one of the following project versions have to be installed - %s" % requires)
    import os; os._exit( os.EX_OK )
    pass


setup(name="SFcalculator_tf",
    version=__version__,
    author="Minhaun Li",
    license="MIT",
    description="A Differentiable pipeline connecting molecule models and crystallpgraphy data", 
    url="https://github.com/Hekstra-Lab/SFcalculator",
    author_email='minhuanli@g.harvard.edu',
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=[
        "gemmi>=0.5.6",
        "reciprocalspaceship>=0.9.18",
        choose_proper_project([
            "tensorflow>=2.6.0",
            "tensorflow-macos>=2.6.0"]),
        "tensorflow_probability>=0.14.0",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
)