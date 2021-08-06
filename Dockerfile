FROM node:8 as frontend

RUN mkdir /Anytime_Doctor/Frontend
WORKDIR /Anytime_Doctor/Frontend
COPY ./Anytime_Doctor_Frontend
RUN npm install yarn && yarn && yarn run build

FROM python:3.7-slim-stretch
RUN mkdir /Anytime_Doctor/Backend
WORKDIR /Anytime_Doctor/Backend
COPY ./Anytime_Doctor_Backend
RUN pip install pipenv
RUN pipenv install --system --deployENV DJANGO_SETTINGS_MODULE myapp.settings.production

# Collect static files
RUN (cd myapp; python manage.py collectstatic --noinput)

VOLUME ["/Anytime_Doctor_Backend/myapp/public"]

EXPOSE 80 443

CMD ["/usr/bin/supervisord"]
