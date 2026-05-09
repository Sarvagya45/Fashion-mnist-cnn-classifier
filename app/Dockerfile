# this sets up the container with Python 3.10 installed
FROM python:3.11-slim

# this copies everything in your current directory to the /app directory in the container
COPY . /app

# this sets the /app directory as the working directoryfor any RUN, CMD, ENTRYPOINT, or COPY instruction that follow
WORKDIR /app

#this runs pip install
RUN pip install --no-cache-dir -r requirements.txt

# this tells docker to listen on port 80 at runtim. Port 80 is standard port for HTTP
EXPOSE 8501

#this command creates a .streamlit directory in home directory of the container 
RUN mkdir -p ~/.streamlit

# this copies your streamlit configuration file into the .streamlit directory 
RUN cp config.toml ~/.streamlit/config.toml

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]