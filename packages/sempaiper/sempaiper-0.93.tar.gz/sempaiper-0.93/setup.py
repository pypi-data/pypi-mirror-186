from setuptools import setup,find_namespace_packages
from os import listdir
setup(name='sempaiper',

      version='0.93',

      url='https://github.com/parlorsky/sempaiper',

      license='ceeers',

      author='Levap Vobayr',

      author_email='tffriend015@gmail.com',

      description='',
      packages=find_namespace_packages(where="src"),
      package_dir={"": "src"},
      package_data={
        f"sempaiper.q{y}_1.{x}": ["*.png"] for x in range(1,len(listdir('/Users/parlorsky/sempaiper/src/sempaiper/q1_1'))+1)  for y in [1,2,3]
        },


      zip_safe=False)
