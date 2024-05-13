# OpenLiteSpeed + Docker | Kubernetes

Todas as imaxes van con php instalado, xa que o necesitan para a web de administracion (que tamén se pode deshabilitar), pero non soe ser muy actual.

En este momento a máquina instala o seguinte software por defecto:
- Ubuntu 24.04 LST
- OpenLiteSpeed 1.7.19 (A versión estable)
- Python 3.10.14
- Python WSGI LSAPI 2.1 (Para Python 3.10)
- Drivers de base de datos sqllite e myslq para Python (as aplicacións clientes)

> [!IMPORTANT]
> As aplicacións despleganse mediante LSAPI:
> https://www.litespeedtech.com/docs/lsapi

### Creación de la imagen en Dockerfile
```bash
docker build --tag ols:1.0.0 .
```

### Lanzamiento del contenedor
```bash
docker run -d -p 80:80 -p 7080:7080 ols:1.0.0
```

### Creación con docker compose
```bash
docker compose -p ols up -d
```

### Eliminación con docker compose
```bash
docker compose -p ols down --rmi all
```

### Eliminación con docker compose
Tanto con docker como con docker compose estes son os argumentos para crear a aplicación:

```bash
UBUNTU_VERSION=24.04        # Versiónd e Ubuntu a instalar
PYTHON_VERSION=3.10.14      # Versión de Python a instalar
OLS_VERSION=1.7.19          # Versión de OpenLiteSpeed a instalar
OLS_ADMIN=ALLOW             # Activar ou non o panel administrador de OpenLiteSpeed (ALLOW|DENY)
OLS_ADMIN_USER=admin        # Login do usuario administrador
OLS_ADMIN_PASS=12345        # Password do usuairo administrador
LSAPI_VERSION=2.1           # Versión do lsapi a instalar
PROJ_NAME=simple            # Nome do proxecto de Django onde está o archivo wsgi.py
```

### Estrucutura datos

```bash
├── configs
│   ├── admin_config.conf.seed  # configuración do portal de administración de OpenLiteSpeed
│   ├── http_config.conf        # configuración do servidor web principal
│   ├── ols.conf                # configuración da instalación de OpenLiteSpeed
│   └── vhost.conf.seed         # configuración do host da apliación de Python
├── web
│   ├── logs              # carpeta que se uutiliza para os logs do vhost
│   ├── private           # aquí gardamos os archivos de configuración da aplicación (secret.json, requirements.txt)
│   └── public            # aquí gardamos a aplicación de Django
├── Dockerfile            # archivos de configuración de Docker 
└── entrypoint.sh         # archivo que lanza o servidor OpenLiteSpeed
```

- configs
    - admin_config.conf > configuramos el servidor de administración, podemos deshabilitarlo con este código:
 ```
 accessControl {
  allow                 ALL
  #  deny                  ALL
 }
 ```

> [!TIP]
> OpenLiteSpeed so permite despligue de aplicacións de Python a través de WSGI, utilizando a aplicación LiteSpeed Sever API (LSAPI) e que en este momento so está preparada para a versión 3.10.
> https://www.litespeedtech.com/open-source/litespeed-sapi/download

***

> [!NOTE]
> O proxecto está preparado para a plataforma de Kubernetes de Akamai, non deberías ter problema para desplegalo en outra plataforma baixo Kubernetes.

> [!IMPORTANT]
> Todo esto é info que saquei de outros repositorios ou aprendín eu, espero que che valga.