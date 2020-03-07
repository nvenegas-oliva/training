
FROM python:3

# copy main.py, requirements.txt and service_account.json into #trainer folder
COPY . /trainer

# set the trainer folder as working directory
WORKDIR /trainer

# install dependencies using pip
RUN pip --no-cache-dir install -r requirements.txt

# define our image entrypoint
ENTRYPOINT ["python", "main.py"]
