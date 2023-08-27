FROM python:3

WORKDIR /app

RUN pip3 install html-testRunner

CMD ["/bin/bash","-c","python -m unittest test/unit/test.py"]