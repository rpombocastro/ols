# VERSIÓN UBUNTU LST MÁS NUEVA
FROM ubuntu:24.04

ARG proj

#ENV env_proj=$proj

# MODIFICAMOS EL PATH
ENV PATH="/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/bin"

# PREPARAMOS LA IMAGEN
RUN apt-get update

# PAQUETES DEL SISTEMA NECESARIOS
RUN apt install \
    wget curl tzdata sed \
    build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev \
    default-libmysqlclient-dev libsqlite3-dev  pkg-config -y

# INSTALAMOS PYTHON Y PIP
RUN wget https://www.python.org/ftp/python/3.10.14/Python-3.10.14.tgz && tar -xf Python-3.10.14.tgz
RUN cd Python-3.10.14 && ./configure --enable-optimizations && make install && \
    rm -rf /Python-3.10.14 && rm /Python-3.10.14.tgz

# CONFIG PIP MYSQLCLIENT
RUN export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`
RUN export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`

# INSTALAMOS OPENLITESPEED
RUN wget https://openlitespeed.org/packages/openlitespeed-1.7.19.tgz && tar xzf openlitespeed-1.7.19.tgz
COPY configs/ols.conf openlitespeed
RUN cd openlitespeed && ./install.sh && \
    echo 'cloud-docker' > /usr/local/lsws/PLAT && \
    rm -rf /openlitespeed && rm /openlitespeed-1.7.19.tgz


RUN mkdir /usr/local/lsws/conf/vhosts/container
COPY configs/httpd_config.conf /usr/local/lsws/conf/
COPY configs/vhost.conf.seed /usr/local/lsws/conf/vhosts/container/
COPY configs/admin_config.conf /usr/local/lsws/admin/conf/

COPY configs/vhost.conf.seed /usr/local/lsws/conf/vhosts/container/
RUN sed 's/#proyecto#/'"$proj"'/g' /usr/local/lsws/conf/vhosts/container/vhost.conf.seed > /usr/local/lsws/conf/vhosts/container/vhost.conf

# CREAMOS INTERPETRADOR DE PYTHON PARA OPENLITESPEED
RUN wget http://www.litespeedtech.com/packages/lsapi/wsgi-lsapi-2.1.tgz && tar xf wsgi-lsapi-2.1.tgz
RUN cd wsgi-lsapi-2.1 && python3 ./configure.py && make && cp lswsgi /usr/local/lsws/fcgi-bin/
RUN rm -rf wsgi-lsapi-2.1 && rm wsgi-lsapi-2.1.tgz

# CREAMOS LAS CARPETAS DE APLICACIÓN
RUN mkdir /usr/local/lsws/container
RUN mkdir /usr/local/lsws/container/public
RUN mkdir /usr/local/lsws/container/private
RUN mkdir /usr/local/lsws/container/logs
RUN mkdir /usr/local/lsws/container/env

# COPIAMOS LOS ARCHIVOS DE LA WEB
COPY web/public /usr/local/lsws/container/public/
COPY web/private /usr/local/lsws/container/private/

# CONFIGURAMOS EL ENTORNO DE PYTHON
RUN python3 -m venv /usr/local/lsws/container/env
RUN . /usr/local/lsws/container/env/bin/activate && pip install --upgrade pip
RUN . /usr/local/lsws/container/env/bin/activate && pip install -r /usr/local/lsws/container/private/requirements.txt

# ACTUALIZAMOS LOS ARCHIVOS ESTÁTICOS Y LA BASE DE DATOS (pendiente de comprobar funcionamiento)
# RUN . /usr/local/lsws/container/env/bin/activate && python3 manage.py collectstatic
# RUN . /usr/local/lsws/container/env/bin/activate && python3 manage.py migrate

# CAMBIAMOS PERMISOS
RUN chown -R nobody:nogroup /usr/local/lsws/container

# INICIAMOS OPENLITESPEED
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
