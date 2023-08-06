from setuptools import setup, Extension

import os


def is_package(path):
    return (
        os.path.isdir(path) and
        os.path.isfile(os.path.join(path, '__init__.py'))
    )


def find_packages(path, base=""):
    """ Find all packages in path """
    packages = {}
    for item in os.listdir(path):
        dir = os.path.join(path, item)
        if is_package(dir):
            if base:
                module_name = "%(base)s.%(item)s" % vars()
            else:
                module_name = item
            packages[module_name] = dir
            packages.update(find_packages(dir, module_name))
    return packages


def read_requirements(filename):
    """
    Get application requirements from
    the requirements.txt file.
    :return: Python requirements
    :rtype: list
    """
    with open(filename, 'r') as req:
        requirements = req.readlines()
    install_requires = [r.strip() for r in requirements if r.find('git+') != 0]
    return install_requires


def read(filepath):
    """
    Read the contents from a file.
    :param str filepath: path to the file to be read
    :return: file contents
    :rtype: str
    """
    with open(filepath, 'r') as f:
        content = f.read()
    return content


requirements = read_requirements('requirements/prod.txt')

packages = find_packages(".")


setup(name='flask_jwt_oidc_mds',
      version='0.0.2',
      description='Flask JWT OIDC MDS',
      author='mds devs, with help from others',
      author_email='mds-devs@gov.bc.ca',
      url='https://github.com/bcgov/flask-jwt-oidc',
      license=read('LICENSE'),
      include_package_data=False,
      long_description='',
      packages=packages.keys(),
      package_dir=packages,
      install_requires=requirements,
      setup_requires=[
          'pytest-runner',
      ],
      tests_require=[
          'pytest',
      ],
      platforms='any',
      zip_safe=False,
      keywords='flask extension development',
      classifiers=[
          'Topic :: System :: Software Distribution'
      ],
      )
