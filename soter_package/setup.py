from setuptools import setup#find_namespace_packages- this function we use in case if we need to load al modules and dont want to list it

setup(name='sort_it',
      version='0.1',
      description='Python sorting script',
      author='FAA',
      author_email='alexandr.frankevich@gmail.com',
      #url='https://www.python.org/sigs/distutils-sig/',
      license="LICENSE.md",
      packages=['soter_package','soter_package.in_use'],#packages=find_namespace_packages()
      install_requires=['markdown'],
      entry_points={'console_scripts': ['sortit =soter_package.in_use.sorting_script:main']}
     )