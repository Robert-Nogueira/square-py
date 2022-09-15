from setuptools import setup

with open("README.md", "r") as file:
    readme = file.read()

setup(name='square-py',
    version='0.0.1',
    license='MIT License',
    author='Robert Nogueira',
    long_description='Wrapper não oficial da SquareCloud API',
    long_description_content_type="text/markdown",
    author_email='robertlucasnogueira@gmail.com',
    keywords='squarecloud api python',
    description=u'Wrapper não oficial da SquareCloud API',
    packages=['square'],
    install_requires=['requests'],)