# package_file_reader
![example branch parameter](https://github.com/github/docs/actions/workflows/main.yml/badge.svg?branch=feature)
<br>
Reader es una paquete de funcionalidades referente a manejo de cualquier tipo de archivos en los proyectos que sea utilizado.


## Features

- Reader: 
- read_file_csv : metodo para lectura de archivos tipo csv, retorna un dictionary formato json.
- set_path: metodo para setear la ruta del archivo
- set_file_name : metodo para setear el nombre del archivo a leer 


## Tech


- [Python] - lenguaje orientado a objetos!
- [setuptools] - libreria para configurar el empaquetado de archivos

## Importacion del paquete

Importar la dependencia sobre la notebook de databricks asi.

```sh
from package_file_reader import reader
```

Desde la notebook llamar el objeto...

```sh
reader.set_path("dbfs://FileStore/tablas")
reader.set_set_file_name("tabla.csv")
json = reader.read_file_csv()
```

## License

MIT

**Free Software*

