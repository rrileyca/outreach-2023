# Python Web Server example
All of this code was taken and adapted from 
[this Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login) 
and 
[this Github repo](https://github.com/do-community/flask_auth_scotch)

## Run it yourself!
Start in the root of this project. Create a [Python venv](https://docs.python.org/3/library/venv.html):
```shell
python -m venv venv
```

Then, activate the venv
```shell
source venv/bin/activate
```

Install all the Python dependencies:
```shell
pip3 install -r requirements.txt
```

Change into the `webserver` directory in this project:
```shell
cd webserver
```

Run the [Flask](https://flask.palletsprojects.com/en/2.3.x/quickstart/) application:
```shell
flask run --host 0.0.0.0
```

Now open a web browser to the machine's IP address that is running the Flask server. You should see it in the console
after you run the `flask run` command from above. For example, it might look like `http://192.168.0.100:5000`. 

## Run using Docker Compose
If you run using Docker Compose, you can connect to nginx using self-signed certs.

Make the self-signed certs by running
```shell
create-certs.sh
```

Then start the project:
```shell
docker-compose up -d
```