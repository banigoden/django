# Use an official Python runtime as a parent image
FROM python:3.11.6

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# RUN mkdir /app
# WORKDIR /app
# COPY ./requirements.txt /app/
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt


# COPY . /app/
# COPY ./web_application /app/
# COPY ./manage.py /app/

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]