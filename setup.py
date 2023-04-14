import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='csrnet',
     version='0.2',
     scripts=['csrnet'] ,
     author="Xavier Gillard and Pierre Schaus",
     author_email="xavier.gillard@uclouvain.be,pierre.schaus@uclouvain.be",
     description="Packaging of ",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/pschaus/csrnet_pip.git",
     packages=setuptools.find_packages(),
     data_files=[('models',['models/weights.zip.npz'])],
     install_requires=['numpy==1.19.2','h5py==2.9.0','Pillow==8.0.1','torch==1.13.1'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],

 )