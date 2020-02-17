from setuptools import setup

setup(name='pypowerbi',
      version='0.24.2',
      description='A python library for Microsoft\'s PowerBI',
      url='https://github.com/Kondratenko-Valeriy/pypowerbi',
      author='Chris Berry',
      author_email='chris@chrisberry.com.au',
      license='MIT',
      packages=['pypowerbi'],
      install_requires=[
            'requests',
            'adal',
            'future-fstrings',
      ],
      zip_safe=False)
