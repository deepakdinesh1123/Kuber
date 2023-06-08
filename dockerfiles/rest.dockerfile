FROM python:3.10

COPY rest /rest
WORKDIR /rest
RUN pip install -r requirements.txt
ENTRYPOINT [ "sh", "./start.sh" ]
