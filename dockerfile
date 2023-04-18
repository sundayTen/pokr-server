FROM python:3.11
COPY . .
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 8080
CMD ["python3", "main.py"]