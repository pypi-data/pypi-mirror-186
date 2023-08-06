from setuptools import setup, find_packages


setup(name='econometrics_tests_statistics',
      version='1.4',
      description='Numerical methods',
      packages=find_packages(),
      author_email='dmitriyalmazof1@gmail.com',
      install_requires = ['numpy','pandas'],
      zip_safe=False,
      )
