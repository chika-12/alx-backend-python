FROM python:3.10-slim
WORKDIR /messaging_project
COPY requirements.txt /messaging_project/
RUN pip install -r requirements.txt
COPY ./messaging_project/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]