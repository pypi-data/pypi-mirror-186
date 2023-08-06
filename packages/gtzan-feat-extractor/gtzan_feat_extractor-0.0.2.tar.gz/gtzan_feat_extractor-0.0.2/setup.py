import setuptools

setuptools.setup(name='gtzan_feat_extractor',
      version='0.0.2',
      description='Feature Extraction for GTZAN Dataset',
      long_description='Feature Extraction for GTZAN Dataset',
      long_description_content_type="text/markdown",
      classifiers=[
          "Programming Language :: Python :: 3.8",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires=">=3.8",
      package_dir = {"": "gtzan_feat_extractor"},
      packages = setuptools.find_packages(where="gtzan_feat_extractor"),
      author="ranierifr",
      author_email='ranierifra@hotmail.it',
      zip_safe=False)
