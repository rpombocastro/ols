# OpenLiteSpeed + Docker | Kubernetes

Todas as imaxes van con php instalado, xa que o necesitan para a web de administracion (que tamén se pode deshabilitar), pero non soe ser muy actual.

En este momento a máquina instala o seguinte software:
- Ubuntu 24.04 LST
- OpenLiteSpeed 1.7.19 (A versión estable)

## Python:
Aplicacións instaladas:
- Python 3.10.14
- Python WSGI LSAPI 2.1 (Para Python 3.10)
- Drivers de base de datos sqllite e myslq para Python (as aplicacións clientes)

### Creación de la imagen en Docker
```
docker build --tag ols:1.0.0 -- build-arg proj=simple .
```

### Lanzamiento del contenedor
```
docker run -d -p 80:80 -p 7080:7080 ols:1.0.0
```

### Estrucutura datos

├── configs
│   ├── admin_config.conf
│   ├── http_config.conf
│   ├── ols.conf
│   └── vhost.conf.seed
├── web
│   ├── logs
│   ├── private
│   └── public
├── Dockerfile
└── entrypoint.sh

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



> [!NOTE]
> O proxecto está preparado para a plataforma de Kubernetes de Akamai, non deberías ter problema para desplegalo en outra plataforma baixo Kubernetes.

> [!IMPORTANT]
> Todo esto é info que saquei de outros repositorios ou aprendín eu, espero que che valga.