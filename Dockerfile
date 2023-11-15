# The image is based on Python 3.9.18
FROM python:3.9.18

# Set the environment variable (deactivates the Python's buffered output)
ENV PYTHONUNBUFFERED 1

# Install the package

#RUN apt-get update && apt-get install -y \
#    python3-pip \
#    gcc \
#    libmysqlclient-dev \
#    mysql-client && apt-get clean

# Set the working directory
WORKDIR /app

# Install git
# RUN apk add --no-cache git

RUN git clone https://github.com/maroo1746/noverdose.git .

# C 파일 및 관련 작업을 위한 디렉토리 설정
# WORKDIR /app/libs

# Copy the project file
COPY . /app/

# C 코드를 shared library로 컴파일
# RUN gcc -shared -o /app/libs/med_db.so -fPIC /app/libs/med_db.c -lmysqlclient

# Go back to main app directory
# WORKDIR /app

# Install the Python package requirements
# you should have requirments.txt file in Project's root
RUN pip install --no-cache-dir -r requirements.txt

# 백업 파일 추가
COPY ./backup.sql /docker-entrypoint-initdb.d/

# Make sure wait-for-it.sh is executable
RUN chmod +x ./wait-for-it.sh

# COPY entrypoint.sh /app/
# RUN chmod +x ./entrypoint.sh
# ENTRYPOINT ["./entrypoint.sh"]

# Run the server (now using wait-for-it.sh)
CMD ["./wait-for-it.sh", "db:3306", "--", "python", "manage.py", "runsslserver", "0.0.0.0:8000"]

