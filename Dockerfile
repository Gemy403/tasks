FROM python:3.10-slim-bullseye as builder

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /build

COPY requirements.txt .

RUN pip install --no-cache-dir --user -r requirements.txt watchdog

FROM python:3.10-slim-bullseye

ARG USER_ID=1000
ARG GROUP_ID=1000

RUN groupadd -g ${GROUP_ID} myuser && \
    useradd -u ${USER_ID} -g ${GROUP_ID} -ms /bin/bash myuser

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libpq5 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /tasks_joy

COPY --from=builder --chown=myuser:myuser /root/.local /home/myuser/.local

ENV PATH=/home/myuser/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBUG=1

COPY --chown=myuser:myuser . .

USER myuser