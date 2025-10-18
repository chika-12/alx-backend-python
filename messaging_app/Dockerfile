FROM python:3.10-slim
WORKDIR /messaging_project
COPY Requirements.txt /messaging_project/
RUN pip install -r Requirements.txt
COPY ./messaging_project/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]