from setuptools import setup
setup(
    name = 'sankalpcli',
    version = '0.1.0',
    packages = ['sankalpcli'],
    entry_points = {
        'console_scripts': [
            'sankalpcli = sankalpcli.__main__:main'
        ]
    })