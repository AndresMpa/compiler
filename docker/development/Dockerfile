FROM ubuntu:latest

COPY ../../requirements.txt /compiler/requirements.txt

WORKDIR /compiler

RUN pip install -r requirements.txt

COPY ../../* /compiler

ENTRYPOINT [ "tail" ]

CMD [ "-F", "/dev/null" ]
