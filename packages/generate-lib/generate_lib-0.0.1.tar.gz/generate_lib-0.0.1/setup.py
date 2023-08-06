from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='generate_lib',
    version='0.0.1',
    license='MIT License',
    author='Kaio Cândido Santiago',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='kaio.santiago.13@hotmail.com',
    keywords='generate lib robot framework',
    description=u'Keywords lib to robotframework',
    packages=['generate_lib'],
    install_requires=['robotframework'],)