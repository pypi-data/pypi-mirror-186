from setuptools import setup, find_packages

setup_requires = ["wheel"]

setup(name='dream_on_gym',
      version='0.0.1',
      description='',
      author='Hermann Ignacio Pempelfort Vergara',
      author_email='hermann.pempelfort@usm.cl',
      url='https://gitlab.com/IRO-Team/dream-on-gym',
      packages=["dreamongym"],
      #packages=find_packages("src"),
      #package_dir={'': 'src'},
      #   install_requires=INSTALL_REQUIRES,
      include_package_data=True,
      install_requires=[
          "numpy",
          "jsonschema",
          "gym == 0.21.0",
          "importlib-metadata==4.13.0",
          "tensorflow == 1.15.0",
          "tensorflow-gpu == 1.15",
          "protobuf == 3.20.0",
          "stable-baselines[mpi]",
          "stable-baselines3[extra]",
          "mpi4py"
      ],
      )