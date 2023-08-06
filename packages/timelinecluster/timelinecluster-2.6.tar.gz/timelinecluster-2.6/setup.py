from setuptools import setup,find_packages

setup(name='timelinecluster',
      version='2.6',
      description='This is timelinecluster.',
      url='',
      author='author test',
      author_email='',
      license='MIT',
      include_package_data=True,
      package_data={'TimeLineCluster': ['utils/js/*.js']},
      packages=find_packages(),
      install_requires= [],
      python_requires='>=3.6',
      zip_safe=False)
