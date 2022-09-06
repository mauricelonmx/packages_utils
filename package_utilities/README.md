# package_utilities
![example branch parameter](https://github.com/github/docs/actions/workflows/main.yml/badge.svg?branch=feature)
<br>
Utilities es una paquete de funcionalidades referente a manejo de operaciones con dataframes.


## Features

- Utilities: 
- convert_to_string_type : metodo para convertir columnas a tipo StringType, retorna nuevo dataframe con los cambios pedidos.
- convert_to_time_stamp_type: metodo para convertir columnas a tipo time_stamp ["dd/MM/yy HH:mm:ss" , "d/M/yy H:mm" , "dd/MM/yyyy"], retorna nuevo dataframe con los cambios pedidos.
- convert_to_date_type : metodo para convertir columnas a tipo DateType ['yyyyMMdd'] , retorna nuevo dataframe con los cambios pedidos


## Tech


- [Python] - lenguaje orientado a objetos!
- [setuptools] - libreria para configurar el empaquetado de archivos

## Importacion del paquete

Importar la dependencia sobre la notebook de databricks asi.

```sh
from package_utilities import utilities
```

Desde la notebook llamar el objeto...

```sh
df = utilities.convert_to_string_type(df, columns)
```

## License

MIT

**Free Software*

