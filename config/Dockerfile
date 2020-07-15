FROM python:3.7

ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true
ENV MAIN_PATH=/usr/local/bin/python_dev
ENV LIBS_PATH=${MAIN_PATH}/libs
ENV CONFIG_PATH=${MAIN_PATH}/config
ENV NOTEBOOK_PATH=${MAIN_PATH}/notebooks

# COPY ./.dotfiles /root/.dotfiles/

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        zsh \
        vim \
        fonts-powerline \
        bash \
        nodejs \
        npm \
    && rm -rf /var/lib/apt/lists/*


RUN  pip3 install --upgrade pip \
    requests \
    jupyter \
    jupyterlab \
    pycrypto \
    bash_kernel \
    && python3 -m bash_kernel.install

# run the installation script  
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true

EXPOSE 8888

CMD cd ${MAIN_PATH} && [ "zsh" ]
