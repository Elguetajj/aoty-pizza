FROM python:3.6-alpine
COPY app /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000


CMD ["python","./aoty-pizza.py"]
