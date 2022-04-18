FROM python:3.9
EXPOSE 5000
WORKDIR /
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY app.py /
CMD python app.py