from setuptools import setup, find_packages

with open("README.md", "r") as rd:
    long_description = rd.read()
	
setup(
 name='fmpdistribution',
 version='1.0.0',
 description='A Python package for calculating pdf, cdf, and sf for Poisson, Binomial,Normal, Multinomial and Exponential distributions.',
 long_description=long_description,
 long_description_content_type="text/markdown",
 url='https://github.com/fmkundi/kundidocs', 
 author='Fazal Masud Kundi',
 author_email='fmkundi@gmail.com',
 classifiers=[
   'Intended Audience :: Education',
   'Operating System :: OS Independent',
   'License :: OSI Approved :: MIT License',
   'Programming Language :: Python :: 3.9',
 ],
 keywords=['python','statistics','probability','probability distribution','poisson',
           'binomial','normal','multinomial','exponential'],
 packages=find_packages()
)