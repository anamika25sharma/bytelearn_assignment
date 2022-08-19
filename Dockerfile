FROM python:3.8.1
ENV  APP_HOME /static
WORKDIR $APP_HOME
COPY . /static
RUN pip install -r requirements.txt
CMD ["python","app.py"]
