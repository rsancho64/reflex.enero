# Estudio de reflex (py) en enero 2024

[**install**](https://reflex.dev/docs/getting-started/installation/)

```bash
sudo apt-get install python3-pip python3-venv

mkdir myRapp
cd myRapp

python3 -m venv .venv 
. .venv/bin/activate

pip install reflex --use-deprecated=legacy-resolver
# https://stackoverflow.com/questions/65122957/resolving-new-pip-backtracking-runtime-issue
```

[**101**](https://reflex.dev/docs/getting-started/installation/)

El init ofrece plantillas: blank y sidebar.
La sidebar produce una pagina con una navegación lateral con tres rutas:
    - home:
    - dashboard:
    - settings

```bash
reflex init 
# opcion template: blank: ok ; sidebar: ok too; 
```

```bash
# reflex demo # para ver posibilidades. servicio externo @ https://demo.reflex.run/
reflex run # ver app local @ http://localhost:3000
# reflex run --loglevel debug  # debug way

```

## Estructura general

`mkdir hello; cd hello ; reflex init`

```bash
hello
├── .web   # compiled JS files here (each Reflex page -> corresponding .js)
├── assets # static stuff
├── hello  # HOMONIMO generado por init. 
│   ├── __init__.py 
│   └── hello.py
└── rxconfig.py # para ubicar argumentos para la class `Config` (app_name, db_url, frontend_port, ...)
```

### paquetes en python. ¿`__init__.py`?

En py cualquier paquete es[ta en] un `__init__.py`. Con él Python sabrá tratar los directorios como módulos/submódulos, pues sumariza los nombres (de métodos .. en los ficheros `.py` en el directorio inmediato.

- [ ] ver [como-construir-tu-1er-paquete-python](https://www.freecodecamp.org/espanol/news/como-construir-tu-primer-paquete-de-python)

### argumentos en linea de comando

`reflex run` *argumentos* ... # para superponer parametros: al archivo rxconfig.py y a variables de entorno

Ej:

`reflex run --frontend-port 3001`

- [ ] adding pages (visto en <http://localhost:3000/>)
  - [ ] duplicamos dashboard (dashboardBis)
    - [x] 1. ++new file `myRapp/pages/dashboardBis.py`.
    - [x] 2. ++new function with the `@template` decorator, which takes the same arguments as `@rx.page`.
    - [x] 3. Import the page in `myRapp/pages/__init__.py` file and it will automatically be added to the app.


### componentes ...

- [x] Ver el componente de barra lateral en {your_app}/components/sidebar.py.
Se recomienda poner los que se utilizan en varias páginas en {your_app}/components/.

### estados ...

A medida que una app crece conviene usar [sub]estados. Se pueden definir en sus propios archivos o, si el estado es específico de una página, en el propio archivo de la página.

- [ ] poner en marcha una demo/tutorial con un estado adicional (ver [aqui](https://reflex.dev/docs/state/substates/))