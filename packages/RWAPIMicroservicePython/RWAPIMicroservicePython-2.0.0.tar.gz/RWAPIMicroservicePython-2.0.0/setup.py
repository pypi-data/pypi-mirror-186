from setuptools import setup

setup(name='RWAPIMicroservicePython',
      version='2.0.0',
      description='Python integration library for the RW API microservices',
      author='Vizzuality',
      author_email='info@vizzuality.com',
      url='https://vizzuality.com',
      license='MIT',
      packages=['RWAPIMicroservicePython'],
      install_requires=[
        'Flask<=2.2.2',
        'requests<2.29',
        "itsdangerous < 2.3;python_version > '3.7'",
        "MarkupSafe < 2.2;python_version > '3.7'",
        "click < 8.1;python_version > '3.7'"
      ],
      extras_require={
        'dev': [
            'Flask==2.2.2',
            'pytest==7.2.1',
            'pytest-cov==4.0.0',
            'pytest-mock==3.10.0',
            'codecov==2.1.12',
            'requests_mock==1.10.0',
        ]
      },
      zip_safe=False)
