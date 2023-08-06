from setuptools import setup


setup(
    name='PyPyd',
    version='1.3',
    requires=["Cython"],
    scripts=["pypyd.py"],
    url='',
    license='',
    author='Lemon',
    author_email='',
    description='Py to pyd tool',
    long_description=open("README.rst", encoding="utf-8").read(),
    long_description_content_type="text/x-rst"
)
