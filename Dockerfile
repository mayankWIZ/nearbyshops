FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /.nearbyshops

WORKDIR /.nearbyshops

RUN apt-get update -y
RUN apt-get upgrade -y

COPY . /.nearbyshops/.
RUN xargs apt-get install -y <system_packages.txt

RUN python -m pip install --upgrade pip
RUN apt install build-essential -y

RUN python -m pip install -r requirements.txt --no-cache-dir
EXPOSE 8000
RUN python manage.py collectstatic --noinput
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "--reload", "--access-logfile", "-", "-b", "0.0.0.0:8000", "nearbyshops.wsgi"]