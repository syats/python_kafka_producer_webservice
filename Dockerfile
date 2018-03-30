FROM python:3.6-alpine3.7
ADD requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt
RUN mkdir server
ENV PRODUCER_LISTENING_PORT=8666
ADD server.py /server/server.py
CMD ["python", "/server/server.py"]

