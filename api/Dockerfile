FROM tiangolo/uvicorn-gunicorn:python3.11-slim

RUN mkdir /service
copy . /service
WORKDIR /service
RUN pip install -r requirements.txt

EXPOSE 80
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]