FROM python:3.10-alpine

COPY ./requirements.txt /compiler/requirements.txt

WORKDIR /compiler

RUN pip install -r requirements.txt

COPY . /compiler

ENTRYPOINT [ "python" ]

CMD ["index.py" ]
