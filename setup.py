from distutils.core import setup

setup(
  name = 'pokemon_stats_package',
  # Se especifica el nombre del paquete
  packages = ['pokemon_stats_package'],
  # Se especifica la versión, que va aumentando con cada actualización
  version = '0.5',
  # Se especifica la licencia escogida
  license='MIT',
# Breve descripción de la librería
description = 'Libreria para proyecto final sobre stats de pokemon',
# Nombre del autor
author = 'Angela Chica',
# Email del autor
author_email = 'angelachicaortega@gmail.com',
# Enlace al repositorio de git de la librería
url = 'https://github.com/angelachica/pokemon_stats_package',
# Enlace de descarga de la librería
download_url = 'https://github.com/angelachica/pokemon_stats_package.git',
# Palabras claves de la librería
keywords = ['pokemon', 'stats', 'grupo'],
# Librerías externas que requieren la librería
install_requires=[
        'unittest',
        'pandas',
        'sqlalchemy',
        'requests',
        'concurrent',
        'functools',
        'cProfile',
    ],


classifiers=[
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)