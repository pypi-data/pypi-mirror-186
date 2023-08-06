from re import search, MULTILINE
from setuptools import setup, find_packages


with open('asyncsqlite3/_version.py') as f:
    version = search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), MULTILINE).group(1)


with open('README.md') as f:
    long_description = f.read()


setup(
    name='asyncsqlite3',
    version=version,
    url='https://github.com/Vladyslav49/asyncsqlite3',
    license='MIT',
    author='Vladyslav49',
    python_requires='>=3.7',
    description='Asynchronous driver for sqlite3.',
    long_description_content_type='text/markdown',
    long_description=long_description,
    install_requires=[
        'async_timeout>=4.0.1,<4.0.2',
        'typing_extensions>=4.3.0,<4.4.0; python_version < "3.8.0"',
    ],
    extras_require={
        'uvloop': [
            'uvloop>=0.16.0,<0.17.0',
        ],
    },
    include_package_data=False,
)
