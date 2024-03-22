FROM ubuntu-python3

WORKDIR /app

COPY main.py .

ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]

