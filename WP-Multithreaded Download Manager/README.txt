Project: Web Programming - Multithreaded Download Manager

Authors: 
Mohsen Ebrahimi
Amirreza Garebaghi

steps to run the project:

1) cd into the project directory and install the script requirements. 
you can use pip with the command "pip install -r requirements.txt" to do this.

2) run the script with the following scheme:
	
	python download.py [OPTIONS] URL
	
	options:
		--name PATH 		(default value: the name of the file in the URL)
		--threads INTEGER 	(default value: count of CPU cores in the system)
			
	- the "name" option is for specifying the name of the file to be saved in the current directory(script execution directory)
	- the "threads" option is for specifying the number of threads to be used for this download
	
if any of the options are not specified script will use the default values.
	
some examples:
	- python download.py https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.10.1.tar.xz
	- python download.py --threads 8 https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.10.1.tar.xz
	- python download.py --threads 4 --name Linux https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.10.1.tar.xz
