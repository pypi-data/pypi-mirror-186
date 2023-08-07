from setuptools import setup, find_packages


setup(
    name="lexisnexisapi",
    version='2.0.40',
    license='MIT',
    author="Robert Cuffney",
    author_email='robert.cuffney@lexisnexis.com',
    packages=find_packages('src'),
    data_files=[('', ['myCredentials.json'])],
    package_dir={'': 'src'},
    include_package_data=True,
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords='example project',
    install_requires=[
          'scikit-learn',
          'multipledispatch',
      ],
     

)