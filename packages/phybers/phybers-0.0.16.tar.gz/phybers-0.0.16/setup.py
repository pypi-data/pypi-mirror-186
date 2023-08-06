import setuptools
import os
import subprocess
from pathlib import Path

this_directory = Path(__file__).parent

long_description = (this_directory / "README.md").read_text()

setuptools.setup(name='phybers',
      version='0.0.16',
      description='Integration of multiple tractography and neural-fibers related tools and algorithms.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/GonzaloSabat/MT',
      author='Gonzalo Sabat',
      author_email='gsabat@udec.cl',
      license='UdeC',
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src"),
      include_package_data=True,
      install_requires=[
          'numpy==1.21.2',
          'dipy==1.4.1',
          'joblib==1.0.1',
          'matplotlib==3.4.2', 
          'scikit-learn',
          'networkx==2.6.3',
          'pandas==1.3.3',
          'PyQt5==5.15.6',
          'PyOpenGL==3.1.6',
          'PyOpenGL_accelerate==3.1.5',
          'nibabel==3.2.1',
          'pydicom==2.1.2',
          'scikit-image==0.16.2',
          'scipy==1.7.1'
      ]
)




