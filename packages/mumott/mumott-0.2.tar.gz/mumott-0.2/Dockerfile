# Base image
FROM python:3.8

# Base packages
RUN \
  apt-get update -qy && \
  apt-get upgrade -qy && \
  apt-get install -qy \
    doxygen \
    gfortran \
    graphviz \
    libopenblas-dev \
    pandoc \
    zip

# remove version constraint on sphinx once the following issue has been resolved
# https://github.com/readthedocs/sphinx_rtd_theme/issues/1343

RUN \
  pip3 install --upgrade \
    pip \
  && \
  pip3 install --upgrade \
    coverage \
    flake8 \
    nbmake \
    pytest \
    setuptools_scm \
    twine \
    xdoctest \
  && \
  pip3 install --upgrade \
    sphinx==5.2.0 \
    sphinx_autodoc_typehints \
    sphinx-rtd-theme \
    sphinx_sitemap \
    sphinxcontrib-bibtex \
    cloud_sptheme \
    nbsphinx \
    ipywidgets \
  && \
  pip3 install --upgrade \
    jinja2==3.0.3 \
  && \
  pip3 install --upgrade \
    colorcet \
    colorspacious \
    h5py \
    matplotlib \
    numpy \
    scipy

CMD /bin/bash
