# OpenLiteSpeed + Docker | Kubernetes

Todas as imaxes van con php instalado, xa que o necesitan para a web de administracion (que tamén se pode deshabilitar), pero non soe ser muy actual.

En este momento a máquina instala o seguinte software:
- Ubuntu 24.04 LST
- OpenLiteSpeed 1.7.19 (A versión estable)

## Python:
Aplicacións instaladas:
- Python 3.10.14
- Python WSGI LSAPI 2.1 (Para Python 3.10)
- Drivers de base de datos sqllite e myslq (as aplicacións clientes)

NOTA: OpenLiteSpeed so permite despligue de aplicacións de Python a través de WSGI, utilizando a aplicación LiteSpeed Sever API (LSAPI) e que en este momento so está actualizada ata a versión 3.10.

https://www.litespeedtech.com/open-source/litespeed-sapi/download


Nota: O proxecto está preparado para a plataforma de Kubernetes de Akamai, non debería ter problema para desplegalo en outra plataforma baixo Kubernetes.
Nota 2: Eu saquei de información que fun recollendo de internet para os meus proxectos, se che sirve para ti... encantado.