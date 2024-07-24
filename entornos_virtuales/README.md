  QUE SON LAS ENTORNOS VIRTUALES

Los entornos virtuales en Python son herramientas que permiten crear entornos aislados y específicos para cada proyecto, lo que significa que puedes tener diferentes configuraciones de librerías y paquetes en cada uno de ellos sin afectar el entorno global de Python en tu sistema.
 PASO A PASO
  
 Admin@DESKTOP-P8B0S93 MINGW64 ~/Desktop/curso_python (main)
$ mkdir entornos_virtuales/

Admin@DESKTOP-P8B0S93 MINGW64 ~/Desktop/curso_python (main)
$ cd entornos_virtuales

Admin@DESKTOP-P8B0S93 MINGW64 ~/Desktop/curso_python/entornos_virtuales (main)
$ ls

Admin@DESKTOP-P8B0S93 MINGW64 ~/Desktop/curso_python/entornos_virtuales (main)
$ python -m venv .venv

Admin@DESKTOP-P8B0S93 MINGW64 ~/Desktop/curso_python/entornos_virtuales (main)
$ source .venv/scripts/activate
(.venv)
Admin@DESKTOP-P8B0S93 MINGW64 ~/Desktop/curso_python/entornos_virtuales (main)
$ deactivate

Admin@DESKTOP-P8B0S93 MINGW64 ~/Desktop/curso_python/entornos_virtuales (main)
$ pip list
Package Version
------- -------
pip     24.0
