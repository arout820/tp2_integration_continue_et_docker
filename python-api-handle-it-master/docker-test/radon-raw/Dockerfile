FROM python:3

WORKDIR /app

RUN pip3 install radon
RUN pip3 install json2tree

CMD ["/bin/bash", "-c","radon raw -j ./ > reports/raw/report.json; json2tree -j reports/raw/report.json -o reports/raw/report.html -t 1 "]