FROM python:3.10
COPY . /server_poc
WORKDIR /server_poc

# Install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --index-url='https://artifactory.globoi.com/artifactory/api/pypi/pypi/simple/'
