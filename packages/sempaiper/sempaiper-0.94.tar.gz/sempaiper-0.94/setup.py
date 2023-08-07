from setuptools import setup,find_namespace_packages
from os import listdir
setup(name='sempaiper',

      version='0.94',

      url='https://github.com/parlorsky/sempaiper',

      license='ceeers',

      author='Levap Vobayr',

      author_email='tffriend015@gmail.com',

      description='',
      packages=find_namespace_packages(where="src"),
      package_dir={"": "src"},
      package_data={**{
        f"sempaiper.q1_1.{x}": ["*.png"] for x in range(1,len(listdir('src/sempaiper/q1_1'))+1)
        },**{
        f"sempaiper.q2_1.{x}": ["*.png"] for x in range(1,len(listdir('src/sempaiper/q2_1'))+1)
        },**{
        f"sempaiper.q3_1.{x}": ["*.png"] for x in range(1,len(listdir('src/sempaiper/q3_1'))+1)
        }},


      zip_safe=False)
