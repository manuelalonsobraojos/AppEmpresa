from setuptools import setup

setup(name='Empresas',
      version='0.1',
      description='Aplicacion para valorar las practicas de empresas',
      long_description='Esta aplicacion permite registrar una empresa en la que se haya realizado las practicas y dar una valoracion de ella',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: GNU :: GNU License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='aplicacion basica de valoracion',
      url='https://github.com/manuelalonsobraojos/AppEmpresa',
      author='ManuelAlonso',
      author_email='Manuel Alonso',
      license='GNU',
      install_requires=[
          'sqlite3',
      ],
      include_package_data=True,
      zip_safe=False)
