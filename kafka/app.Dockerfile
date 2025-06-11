FROM python:3.11-slim
WORKDIR /app

COPY . .


RUN pip install numpy
RUN pip install kafka-python
CMD ["python", "app.py"]