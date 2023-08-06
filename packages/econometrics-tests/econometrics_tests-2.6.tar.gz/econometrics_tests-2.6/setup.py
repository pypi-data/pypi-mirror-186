from setuptools import setup, find_packages


setup(name='econometrics_tests',
      version='2.6',
      description='-',
      author_email='dmitriyalmazof1@gmail.com',
      packages=find_packages(),
      install_requires = ['pandas'],
      zip_safe=False,
      )
