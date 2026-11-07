# 1. Base image = rent a ready-made kitchen (from Docker Hub)
FROM python:3.12-slim

# 2. Set up your counter inside that kitchen
WORKDIR /app

# 3. Copy ONLY the shopping list first (layer-caching trick)
#It will copy the requirements.txt file from your local machine to the /app directory in the Docker image. 
COPY requirements.txt .  

#This command installs the Python packages listed in the requirements.txt file. The --no-cache-dir option is used to prevent pip from caching the downloaded packages, which helps reduce the size of the Docker image.
RUN pip install --no-cache-dir -r requirements.txt

# 4. NOW copy the rest of the code
# COPY . . command copies all the files and directories from your local machine's current directory (where the Dockerfile is located) into the /app directory inside the Docker image.
COPY . .

# 5. Train the model INSIDE the image (baked in at build time)
# The RUN instruction in a Dockerfile is used to execute commands during the build process of the Docker image. 
RUN python train.py

# 6. Declare which window the food comes out of
# The EXPOSE instruction in a Dockerfile is used to inform Docker that the container will listen on the specified network ports at runtime. In this case, the line EXPOSE 8000 indicates that the application running inside the container will be accessible through port 8000. 
EXPOSE 8000

# 7. What runs the moment the container starts
# The CMD instruction in a Dockerfile specifies the command that should be executed when a container is started from the image. In this case, the command is to run the Uvicorn server with the specified parameters.
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
