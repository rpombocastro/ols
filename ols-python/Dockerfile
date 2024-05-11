ARG UBUNTU_VERSION=24.04
FROM ubuntu:${UBUNTU_VERSION}

# MODIFICAMOS EL PATH
ENV PATH="/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/bin"
ENV DEBIAN_FRONTEND=noninteractive 

ARG PYTHON_VERSION=3.10.14
ARG OLS_VERSION=1.7.19
ARG OLS_PASSWORD=12345
ARG LSAPI_VERSION=2.1
ARG PROJ_NAME=simple

# PREPARAMOS LA IMAGEN
RUN apt-get update

# PAQUETES DEL SISTEMA NECESARIOS
RUN apt install \
    wget curl tzdata sed \
    build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev \
    default-libmysqlclient-dev libsqlite3-dev  pkg-config -y

# INSTALAMOS PYTHON Y PIP
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && tar -xf Python-${PYTHON_VERSION}.tgz
RUN cd Python-${PYTHON_VERSION} && ./configure --enable-optimizations && make install && \
    rm -rf /Python-${PYTHON_VERSION} && rm /Python-${PYTHON_VERSION}.tgz

# CONFIG PIP MYSQLCLIENT
RUN export MYSQLCLIENT_CFLAGS=`pkg-config mysqlclient --cflags`
RUN export MYSQLCLIENT_LDFLAGS=`pkg-config mysqlclient --libs`

# INSTALAMOS OPENLITESPEED
RUN wget https://openlitespeed.org/packages/openlitespeed-${OLS_VERSION}.tgz && tar xzf openlitespeed-${OLS_VERSION}.tgz
COPY configs/ols.conf.seed openlitespeed
RUN sed 's/#PASSWORD#/'"${OLS_PASSWORD}"'/g' /openlitespeed/ols.conf.seed > /openlitespeed/ols.conf
RUN cd openlitespeed && ./install.sh && \
    echo 'cloud-docker' > /usr/local/lsws/PLAT && \
    rm -rf /openlitespeed && rm /openlitespeed-${OLS_VERSION}.tgz

RUN mkdir /usr/local/lsws/conf/vhosts/container
COPY configs/httpd_config.conf /usr/local/lsws/conf/
COPY configs/vhost.conf.seed /usr/local/lsws/conf/vhosts/container/
COPY configs/admin_config.conf /usr/local/lsws/admin/conf/

COPY configs/vhost.conf.seed /usr/local/lsws/conf/vhosts/container/
RUN sed 's/#PROJECT#/'"${PROJ_NAME}"'/g' /usr/local/lsws/conf/vhosts/container/vhost.conf.seed > /usr/local/lsws/conf/vhosts/container/vhost.conf

# CREAMOS INTERPETRADOR DE PYTHON PARA OPENLITESPEED
RUN wget http://www.litespeedtech.com/packages/lsapi/wsgi-lsapi-${LSAPI_VERSION}.tgz && tar xf wsgi-lsapi-${LSAPI_VERSION}.tgz
RUN cd wsgi-lsapi-${LSAPI_VERSION} && python3 ./configure.py && make && cp lswsgi /usr/local/lsws/fcgi-bin/
RUN rm -rf wsgi-lsapi-${LSAPI_VERSION} && rm wsgi-lsapi-${LSAPI_VERSION}.tgz

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
