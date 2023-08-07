from setuptools import setup, find_packages

setup(
    name='berteley',
    version='0.0.1',
    license='MIT',
    author="Danilla Ushizima, Eric Chagnon",
    author_email='echagnon@lbl.gov',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/dani-lbnl/berteley/tree/eric',
    keywords='Topic Modeling Scientific Articles',
    install_requires=[
          'bertopic',
      ],

)