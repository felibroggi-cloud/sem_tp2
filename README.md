COMO INSTALAR JUPYTER NOTEBOOK
1. Instalar python en tu computadora (recomiendo la version estable mas reciente)
   IMPORTANTE: Cuando se esta instalando python, marcar un tick en la opcion 'Add Python to PATH' que aparecera en algun momento de la instalacion

2. Una vez instalado, abrir el cmd e ingresar el comando
    pip

   Si python fue instalado correctamente, el cmd deberia devolver algo asi:

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  lock                        Generate a lock file.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  inspect                     Inspect the python environment.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  index                       Inspect information available from package indexes.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.

  (y mas lineas abajo)

3. Una vez verificado que pip efectivamente esta instalado realizado el comando en el punto 2, ingresar los siguientes comandos:
    pip install notebook

4. Una vez que ambos comandos finalicen, ingresar el comando
    jupyter notebook

   Esto deberia abrir en su navegador predeterminado una pestaña con la interfaz de jupyter, donde deberia ver un listado de carpetas y archivos de su computadora


  
5. Una vez instalado lo anterior, descargue tanto las carpetas llamadas 'notebooks' y 'src' y guardelas en un mismo directorio dentro de su PC. 

6. Luego, vuelva al jupyter notebook y busque el archivo 'ejercicio (10)' dentro de la carpeta 'notebooks'. Al encontrarlo, hagale click

7. Para ejecutar la celda de la notebook, solo basta con apretar Ctrl + Enter