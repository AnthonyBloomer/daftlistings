from setuptools import setup

setup(name='daftlistings',
      version='0.7',
      description='A web scraper for Daft.ie',
      url='https://github.com/AnthonyBloomer/daftlistings',
      author='Anthony Bloomer',
      keywords=['daft', 'web scraping'],
      author_email='ant0@protonmail.ch',
      license='MIT',
      packages=['daftlistings'],
      install_requires=[
          'beautifulsoup4',
      ],
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          "Topic :: Software Development :: Libraries",
          'Programming Language :: Python :: 2.7'
      ],
      zip_safe=False)
