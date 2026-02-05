# from: https://code-workbench.com/2025/04/10/enabling-gpio-use-from-kubernetes-pod/

FROM ubuntu:22.04
# Copy Code File
COPY . /app
# Set the working directory
WORKDIR /app
# Install dependencies
RUN apt-get update
# Install Python3
RUN apt-get install -y python3-pip
# Install Python3 GPIO
RUN apt-get install -y python3-gpiozero

RUN chmod +x /app/main.py

EXPOSE 5000

CMD ["python3", "./main.py"]
