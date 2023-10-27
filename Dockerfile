# The image is based on Python 3.9.18
FROM python:3.9.18

# Set the environment variable (deactivates the Python's buffered output)
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install the Python package requirements
# you should have requirments.txt file in Project's root
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project file
COPY . /app/

# Run the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]