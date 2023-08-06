from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("./requirements.txt") as f:
    requirements = f.readlines()

with open("./LICENSE") as f:
    LICENSE = f.read()

setup(name='scanplan-lidar-toolkit',
      description='ScanPlan LiDAR Tool Kit',
      long_description=readme,
      long_description_content_type='text/markdown',
      license='Licensed to ScanPlan',
      keywords='lidar gis las',
      author=LICENSE,
      author_email='shayan@scan-plan.nl',
      url='https://github.com/bimbuildings/ltk',
      python_requires='>=3.8',
      install_requires=requirements,
      packages=find_packages(),
      classifiers=[
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3",
      ],
    )
