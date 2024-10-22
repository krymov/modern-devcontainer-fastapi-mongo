FROM ubuntu:22.04

# Arguments to set UID, GID, and username
ARG LOCAL_UID=1000
ARG LOCAL_GID=1000
ARG DEV_USERNAME=developer



# Use Bash as the default shell
SHELL ["/bin/bash", "-c"]

# Update the package list and install necessary packages
# hadolint ignore=DL3008
RUN apt-get update && apt-get install -y --no-install-recommends \
    fish \
    build-essential \
    wget \
    git \
    curl \
    sudo \
    screen \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*  # Clean up to reduce the image size


# Create a group and user with the specified UID and GID
RUN groupadd -g ${LOCAL_GID} ${DEV_USERNAME} && \
    useradd -l -m -u ${LOCAL_UID} -g ${LOCAL_GID} ${DEV_USERNAME} && \
    usermod -aG sudo ${DEV_USERNAME} && \
    echo "${DEV_USERNAME} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/${DEV_USERNAME}

# FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# ENV PYTHONUNBUFFERED 1

# ARG UID
# ARG GID
# ARG USERNAME=developer

# RUN if id -u ${UID} >/dev/null 2>&1; then \
#   EXISTING_USER=$(getent passwd ${UID} | cut -d: -f1) && \
#   usermod -l ${USERNAME} ${EXISTING_USER} && \
#   groupmod -n ${USERNAME} $(id -gn ${EXISTING_USER}); \
#     else \
#   groupadd -g ${GID} ${USERNAME} && \
#   useradd -m -u ${UID} -g ${GID} -s /usr/bin/fish ${USERNAME}; \
#     fi && \
#     usermod -aG root ${USERNAME} && \
#     usermod -aG sudo ${USERNAME}

# USER ${USERNAME}

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>



