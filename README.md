## Running the website as dokcer container

1. Run the following command to build the docker image
Make sure you are in the `web` directory

`$ docker build -t myapp:1.0 .`

2. Run the following command to run the image

`$ docker run -d -p 5000:5000 myapp:1.0`

3. Access the website by navigating to

`http://127.0.0.1:5000`