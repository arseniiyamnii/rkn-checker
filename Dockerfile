FROM python:alpine3.16
WORKDIR /app
ADD ./main.py ./requirements.txt /app/
RUN pip3 install -r requirements.txt
CMD ["-u","/app/main.py"]
ENTRYPOINT ["python"]
