import setuptools
import distutils.sysconfig

from setuptools import Distribution


class BinaryDistribution(Distribution):
    def has_ext_modules(foo):
        return True

setuptools.setup(
    name= 'windwardrestapi',
    version= "23.0.0.2",
    description = 'Python client for the Windward RESTful Engine',
    long_description = '',
    url = 'http://www.windward.net/products/restful/',
    author = 'Windward Studios',
    author_email ='support@windward.net',
    install_requires = ['requests', 'six'],
    package_dir={'': 'src'},
    packages = setuptools.find_packages(where='src'),
    distclass=BinaryDistribution

)
