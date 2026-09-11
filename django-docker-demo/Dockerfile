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

# this image's application is expected to listen on port 8080 inside the container
# but this doesn't bind the port.
EXPOSE 8000

# using this as entry point run the list of CMD below. ENTRYPOINT is the main exectuable and should not changed by others.
# ENTRYPOINT will have non overridable values
ENTRYPOINT ["/djangoappdemo/.venv/bin/python3"]

#CMD will have overridable values. Others can change these as they need.
CMD ["manage.py", "runserver", "0.0.0.0:8000"]