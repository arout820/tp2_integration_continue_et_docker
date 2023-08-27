FROM python:3

WORKDIR /app

RUN pip3 install robotframework 
RUN pip3 install robotframework-requests

CMD ["/bin/bash","-c","robot --outputdir reports/robot/ test/system/machine.robot"]