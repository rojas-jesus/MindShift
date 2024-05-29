FROM python:3.12.3-alpine3.19

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN  apk update \
#	&& apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
	&& pip install --upgrade pip

COPY ./requirements.txt ./

COPY ./ ./ 

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
