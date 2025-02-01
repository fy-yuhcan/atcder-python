FROM python:3.11

ARG USERNAME=vscode
ARG GROUPNAME=${USERNAME}
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

RUN apt-get update \
    && groupadd --gid ${USER_GID} ${GROUPNAME} \
    && useradd -s /bin/bash --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
    && apt-get -y install sudo \
    && echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

# NumPy をビルドするのに必要なものをインストール
RUN apt-get update && \
    apt-get install -y \
    python3-distutils \  
    python3-dev \      
    build-essential \       
    pypy3 \
        nodejs \
        npm \
        && rm -rf /var/lib/apt/lists/*

# ライブラリのインストール
COPY requirements.txt /tmp/

# pip / setuptools / wheel を最新化してからライブラリを入れる
RUN python -m pip install --upgrade pip setuptools wheel \
    && pip install -r /tmp/requirements.txt

# コンテスト補助ツール
RUN pip3 install online-judge-tools
RUN npm install -g atcoder-cli

# (必要に応じてユーザに切り替える)
USER ${USERNAME}
