FROM python:3.7.9
ARG ODOO_VERSION=14.0
ARG DOCKER_ODOO_UID=9999  
ARG DOCKER_ODOO_GID=9999

SHELL ["/bin/bash", "-xo", "pipefail", "-c"]

# Generate locale C.UTF-8 for postgres and general locale data
ENV LANG C.UTF-8

# Install some deps, lessc and less-plugin-clean-css, and wkhtmltopdf
RUN apt-get update && apt-get -y install node-less npm ssh libxml2-dev libxslt1-dev libldap2-dev\  
    libsasl2-dev libtiff5-dev libjpeg62-turbo-dev libopenjp2-7-dev\  
    zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev\  
    libharfbuzz-dev libfribidi-dev libxcb1-dev libpq-dev\  
    xvfb libfontconfig wkhtmltopdf python3-virtualenv virtualenv postgresql-client mc

# Install rtlcss (on Debian buster)
RUN npm install -g rtlcss

# Enable VENV
ENV VIRTUAL_ENV=/home/odoo/venv
RUN python3.7 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install debugger
RUN python3.7 -m pip install --upgrade pip && \
    python3.7 -m pip install debugpy pre-commit

# Create Virtual Environment and install dependencies
RUN curl https://raw.githubusercontent.com/odoo/odoo/${ODOO_VERSION}/requirements.txt > /tmp/requirements.txt && \
    pip3 install -r /tmp/requirements.txt


# Add "odoo" user. We use same guid uid as in the official Odoo image
RUN groupadd --gid ${DOCKER_ODOO_GID} odoo && useradd odoo -u ${DOCKER_ODOO_UID} -g ${DOCKER_ODOO_GID} -m -s /bin/bash

# Set permissions
RUN mkdir -p /home/odoo/odoo \
    && chown -R odoo C:/odoo

# Expose Odoo services
EXPOSE 5678 8069 8071 8072


# Set default user when running the container
USER odoo
