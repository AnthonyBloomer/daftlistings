from setuptools import setup

setup(name='daftlistings',
      version='0.5',
      description='A web scraper for Daft.ie',
      url='https://github.com/AnthonyBloomer/daftlistings',
      author='Anthony Bloomer',
      author_email='ant0@protonmail.ch',
      license='MIT',
      packages=['daftlistings'],
      install_requires=[
            'beautifulsoup4',
      ],
      zip_safe=False)
