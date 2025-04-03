FROM python:3.10-alpine

ENV HOME /srv/app
RUN addgroup -S -g 1000 app && adduser -S -h $HOME -G app -u 999 app
WORKDIR $HOME

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1
ENV VIRTUAL_ENV="$HOME/env"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --chown=app:app . .

RUN set -eux \
    && apk add --no-cache --virtual .build-deps \
        git \
        build-base \
        gcc \
        musl-dev \
        python3-dev \
        postgresql-dev \
    && python -m venv env \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive $HOME/env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]

EXPOSE 8000

USER app

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "juntagrico_planktonbasel.wsgi:application"]