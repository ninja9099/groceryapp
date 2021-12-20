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
