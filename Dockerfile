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

# Copy getlog.c into the container
COPY getlog.c /app/

# Compile getlog.c
RUN gcc -o getlog getlog.c

# Make getlog executable
RUN chmod +x getlog

# Copy wait-for-it.sh into the container
COPY wait-for-it.sh /app/wait-for-it.sh

# 백업 파일 추가
COPY ./backup.sql /docker-entrypoint-initdb.d/

# Make sure wait-for-it.sh is executable
RUN chmod +x /app/wait-for-it.sh

# Run the server (now using wait-for-it.sh)
CMD ["./getlog", "./wait-for-it.sh", "db:3306", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]