from setuptools import setup, find_packages


setup(
    name='codeguru',
    version='0.5',
    license='MIT',
    author="kolya5544",
    author_email='a@nk.ax',
    packages=find_packages('codeGuruLib'),
    package_dir={'': 'codeGuruLib'},
    url='https://nk.ax/',
    keywords='codeguru',
    install_requires=[
          'asyncio',
      ],
)