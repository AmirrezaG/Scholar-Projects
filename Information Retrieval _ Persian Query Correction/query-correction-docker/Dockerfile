FROM python:latest
WORKDIR /app
ADD requirements.txt ./
ADD *.py ./
ADD /resources ./resources
EXPOSE 80
RUN pip install -r requirements.txt
CMD ["python", "server.py"] 
