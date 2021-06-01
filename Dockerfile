FROM python:3.9-buster
RUN pip install requests
COPY ./coding_challenge.py /coding_challenge.py
CMD ["/coding_challenge.py"]
