from distutils.core import setup

setup(name='vwa-utils',

      version='2.0',

      description='Test de PyTest',

      author='Ecole IT',

      packages=["utils"],
      package_dir={"":"src"},

      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",]

      )
