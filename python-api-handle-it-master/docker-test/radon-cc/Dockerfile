FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt 

CMD ["/bin/bash", "-c","radon cc -j ./ > reports/cc/report.json; json2tree -j reports/cc/report.json -o reports/cc/report.html -t 1 "]
