FROM ubuntu:22.04
ARG KOFA_VERSION=1.8.1

MAINTAINER Uli Fouquet <uli@waeup.org>

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y tzdata
RUN apt-get install -y apt-utils build-essential
RUN apt-get install -y python2.7-dev libxml2-dev libxslt1-dev \
                       zlib1g-dev python3-virtualenv
# see https://urllib3.readthedocs.org/en/latest/security.html#openssl-pyopenssl
RUN apt-get install -y libssl-dev libffi-dev
# libs needed/useful for Pillow image manipulations
RUN apt-get install -y libjpeg-dev libfreetype6-dev libtiff-dev libopenjp2-7-dev
# helpers not strictly necessary for running kofa but for setup and development
RUN apt-get install -y sudo git wget pwgen xmlstarlet

# add user `kofa`
RUN useradd -ms /bin/bash kofa
# set password of user `kofa` and add to group 'sudo'
RUN echo kofa:kofa | chpasswd && adduser kofa sudo

USER kofa
ENV HOME /home/kofa
WORKDIR /home/kofa

# create a virtual env
RUN virtualenv -p /usr/bin/python2.7 py27

# get sources

# we can work with official PyPI sources...
RUN /home/kofa/py27/bin/pip download --no-binary --no-deps waeup.kofa==${KOFA_VERSION}
## ...OR with local kofa sources (create a source pkg with `python setup.py sdist`)
## Please keep one of the two lines above and below commented out.
# COPY --chown=kofa:kofa dist/waeup.kofa-${KOFA_VERSION}.tar.gz /home/kofa
RUN tar -xzf waeup.kofa-${KOFA_VERSION}.tar.gz
RUN rm waeup.kofa-${KOFA_VERSION}.tar.gz
RUN mv waeup.kofa-${KOFA_VERSION} waeup.kofa

## make sure, all added files belong to `kofa`
#RUN chown -R kofa:kofa /home/kofa/

# install kofa -- this is the heavy part...
WORKDIR /home/kofa/waeup.kofa

# set random secrets for cookies
RUN xmlstarlet edit -L -P -S -N x="http://namespaces.zope.org/browser" --update "//x:beakerSession/@secret" --value `pwgen -s -1 20` etc/site.zcml.in
RUN xmlstarlet edit -L -P -S -N x="http://namespaces.zope.org/browser" --update "//x:beakerSession/@validate_key" --value "val_"`pwgen -s -1 16` etc/site.zcml.in

# pin down `pip` and `setuptools` - just to ensure we have a fixed set of versions
RUN /home/kofa/py27/bin/pip install --upgrade pip==20.3.4
RUN /home/kofa/py27/bin/pip install --upgrade --force-reinstall setuptools==44.1.1
# pin down `zc.buildout` - versions >= 3 make entry-points of installed eggs
# invisible for `pgk_resources`
RUN /home/kofa/py27/bin/pip install "zc.buildout<3"
RUN /home/kofa/py27/bin/buildout

# this dir will contain data you might want to be persistent
VOLUME ["/home/kofa/waeup.kofa/var/"]

CMD /home/kofa/waeup.kofa/bin/kofactl fg
