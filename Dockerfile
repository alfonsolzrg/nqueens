FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir nqueens
# COPY requirements.txt /nqueens/
COPY . /nqueens/
WORKDIR nqueens
RUN pip install -r requirements.txt
CMD python main.py