Project: Information Retrieval - Query Correction

Authors: 
Mohsen Ebrahimi
Amirreza Garebaghi

steps to run the project:

1) move the /resources directory to /query-correction-[your os].
	- move to /query-correction windows if you're using windows.
	- move to /query-correction-Linux if you're using GNU/Linux.
	- move to /query-correction-docker if you want to build a docker image.

2) cd into the project directory(windows or GNU/Linux version depending on your system) and install the script requirements. 
you can use pip with the command "pip install -r requirements.txt" to do this.

3) run the script "server.py" to deploy the server.
the server runs on localhost and port 80.

4) run the script "main.py" for the terminal interface.
you can also see the confidence value for each query in this mode.

5) you can also pull the docker container and run that instead.

use commands:	
	1)"docker pull mohsen78/query-correction"
	2)"docker run -d -p 80:80 query-correction:latest"

the container is now running and can be accessed by visiting: http://localhost:80
