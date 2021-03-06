FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "5000"]

##CMD ["gunicorn", "-w 4","-k uvicorn.workers.UvicornWorker", "main:app"] For deployment on Heroku