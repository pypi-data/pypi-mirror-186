from setuptools import setup, find_packages


setup(
    name='inca_interfaces',
    version='0.0.2',
    license='MIT',
    author="Inca",
    author_email='mike@nexxt.in',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/nexxt-intelligence/inca-interfaces',
    keywords='',
    install_requires=[
          'scikit-learn',
      ],

)
