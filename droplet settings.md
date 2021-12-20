Welcome to DigitalOcean's 1-Click Django Droplet.
To keep this Droplet secure, the UFW firewall is enabled.
All ports are BLOCKED except 22 (SSH), 80 (HTTP), and 443 (HTTPS).

Access the Django admin site
    URL: http://192.241.150.190/admin
    User: django
    Pass: 6f4049db07b15d9355004e86536b794d

Use these SFTP credentials to upload files with FileZilla/WinSCP/rsync:
    Host: 192.241.150.190
    User: django
    Pass: 6f4049db07b15d9355004e86536b794d

Django is configured to use Postgres as its database. Use the following
credentials to manage the database:
    Database: django
    User:     django
    Pass:     c50214d0403df226e7ebbb777a33c07e

In a web browser, you can view:
 * The Django 1-Click Quickstart guide: https://do.co/3bY3b67#start
 * The new Django site: http://192.241.150.190

On the server:
  * The Django application is served from /home/django/django_project
  * The Django passwords and keys are saved in /root/.digitalocean_passwords
  * Certbot is preinstalled. Run it to configure HTTPS.

For help and more information, visit https://do.co/3bY3b67



## postgres User and database

    createuser u_urban
    createuser u_groceryapp
    createdb grocery_prod --owner u_groceryapp
    psql -c "ALTER USER u_groceryapp WITH PASSWORD 'groceryapp'"

## system users
    user : groceryapp
    pass: groceryapp

#!/bin/bash

NAME="groceryapp"
DIR=/home/groceryapp/groceryapp
USER=groceryapp
GROUP=groceryapp
WORKERS=3
BIND=unix:/home/groceryapp/run/gunicorn.sock
DJANGO_SETTINGS_MODULE=groceryapp.settings
DJANGO_WSGI_MODULE=groceryapp.wsgi
LOG_LEVEL=error

cd $DIR

export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DIR:$PYTHONPATH

exec /home/groceryapp/v_groceryapp/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $WORKERS \
  --user=$USER \
  --group=$GROUP \
  --bind=$BIND \
  --log-level=$LOG_LEVEL \
  --log-file=-



sudo nano /etc/supervisor/conf.d/grocery-app.conf


## supervisor conf

[program:grocery-app]
command=/home/groceryapp/gunicorn_start
user=groceryapp
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/home/groceryapp/logs/gunicorn-error.log


## nginx confs

    sudo nano /etc/nginx/sites-available/grocery-app

    upstream app_server {
    server unix:/home/groceryapp/run/gunicorn.sock fail_timeout=0;
    }
    
    server {
        listen 80;

        # add here the ip address of your server
        # or a domain pointing to that ip (like example.com or www.example.com)
        server_name 192.241.150.190;
    
        keepalive_timeout 5;
        client_max_body_size 4G;
    
        access_log /home/groceryapp/logs/nginx-access.log;
        error_log /home/groceryapp/logs/nginx-error.log;
    
        location /static/ {
            alias /home/groceryapp/groceryapp/static/;
        }
    
        # checks for static file, if not found proxy to app
        location / {
            try_files $uri @proxy_to_app;
        }
    
        location @proxy_to_app {
          proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
          proxy_set_header Host $http_host;
          proxy_redirect off;
          proxy_pass http://app_server;
        }
    }


sudo ln -s /etc/nginx/sites-available/grocery-app /etc/nginx/sites-enabled/grocery-app
sudo rm /etc/nginx/sites-enabled/default


## update steps
    ssh root@107.170.28.172
    su - django
    pass:******
    source bin/activate
    cd groceryapp/groceryapp
    git pull origin master
    python manage.py collectstatic
    python manage.py migrate
    sudo supervisorctl restart grocery-app
    exit


## front-end configs nginx
server {
    listen 80;

    # add here the ip address of your server
    # or a domain pointing to that ip (like example.com or www.example.com)
    server_name 192.241.150.190;

    root /home/groceryapp/grocery-front;
    location / {
     try_files $uri $uri/ /index.html;
    }

}

sudo nano /etc/nginx/sites-available/grocery-front
