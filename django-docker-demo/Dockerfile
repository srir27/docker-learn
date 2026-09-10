# use ubuntu image
FROM ubuntu:latest

# this WORKDIR is the home for the application
WORKDIR /djangoappdemo 

# run these commands to install pythons and delete the apt list
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    rm -rf /var/lib/apt/lists/*

# copy requirements file to the WORKDIR (/djangoappdemo)
COPY requirements.txt .

# to create a venv and install the required py packages
RUN python3 -m venv .venv && \
    .venv/bin/pip install -r requirements.txt

# copy the project folder to the WORKDIR (/djangoappdemo)
COPY . .

# open port 8000 on the container
EXPOSE 8000

# using this as entry point run the list of CMD below
ENTRYPOINT ["/djangoappdemo/.venv/bin/python3"]

CMD ["manage.py", "runserver", "0.0.0.0:8000"]