FROM python:3.11-slim

# Set working directory
WORKDIR /ansible

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    openssh-client \
    sshpass \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Ansible and dependencies
RUN pip install --no-cache-dir \
    ansible==9.2.0 \
    ansible-core==2.16.3

# Create all necessary directories with proper permissions
RUN mkdir -p /ansible/playbooks && \
    mkdir -p /ansible/scripts && \
    mkdir -p /ansible/output && \
    mkdir -p /ansible/temp && \
    mkdir -p /root/.ssh && \
    chmod 700 /root/.ssh

COPY get_logs.yml /ansible/common
COPY quiz.ini /ansible
COPY stats.py /ansible

RUN chmod +x /ansible/scripts/stats.py

RUN echo "Host *\n\
    StrictHostKeyChecking no\n\
    UserKnownHostsFile=/dev/null" > /root/.ssh/config && \
    chmod 600 /root/.ssh/config


ENV ANSIBLE_HOST_KEY_CHECKING=False
ENV ANSIBLE_STDOUT_CALLBACK=yaml

# Default command
CMD ["ansible-playbook", "--version"]