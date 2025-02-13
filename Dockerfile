FROM python:3.10-slim
WORKDIR /imei
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
ADD run.sh /
ENTRYPOINT ["/bin/sh", "/run.sh"]

