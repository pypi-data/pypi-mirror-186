from setuptools import setup, find_packages

setup(
   name="Mensajitos-saidnahum",
   version="5.0",
   description="Un paquete para saludar y despedir",
   long_description=open("README.md").read(),
   long_description_content_type = "text/markdown",
   author="Said Montes",
   author_email="saidnahum.dev@gmail.com",
   url="https://sidn.ml",
   license_files=["LICENSE"],
   packages=find_packages(),
   scripts=["test.py"],
   install_requires=[paquete.strip() for paquete in open("requirements.txt").readlines()],
   classifiers=[
      'Environment :: Console',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3.9',
      'Programming Language :: Python :: 3.10',
      'Topic :: Utilities',
   ]
)