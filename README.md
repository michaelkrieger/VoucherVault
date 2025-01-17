<div align="center" width="100%">
    <h1>VoucherVault</h1>
    <img width="150px" src="myapp/static/assets/img/logo.png">
    <p>Django web application to store and manage vouchers, coupons and gift cards digitally</p><p>
    <a target="_blank" href="https://github.com/l4rm4nd"><img src="https://img.shields.io/badge/maintainer-LRVT-orange" /></a>
    <a target="_blank" href="https://GitHub.com/l4rm4nd/VoucherVault/graphs/contributors/"><img src="https://img.shields.io/github/contributors/l4rm4nd/VoucherVault.svg" /></a><br>
    <a target="_blank" href="https://GitHub.com/l4rm4nd/VoucherVault/commits/"><img src="https://img.shields.io/github/last-commit/l4rm4nd/VoucherVault.svg" /></a>
    <a target="_blank" href="https://GitHub.com/l4rm4nd/VoucherVault/issues/"><img src="https://img.shields.io/github/issues/l4rm4nd/VoucherVault.svg" /></a>
    <a target="_blank" href="https://github.com/l4rm4nd/VoucherVault/issues?q=is%3Aissue+is%3Aclosed"><img src="https://img.shields.io/github/issues-closed/l4rm4nd/VoucherVault.svg" /></a><br>
        <a target="_blank" href="https://github.com/l4rm4nd/VoucherVault/stargazers"><img src="https://img.shields.io/github/stars/l4rm4nd/VoucherVault.svg?style=social&label=Star" /></a>
    <a target="_blank" href="https://github.com/l4rm4nd/VoucherVault/network/members"><img src="https://img.shields.io/github/forks/l4rm4nd/VoucherVault.svg?style=social&label=Fork" /></a>
    <a target="_blank" href="https://github.com/l4rm4nd/VoucherVault/watchers"><img src="https://img.shields.io/github/watchers/l4rm4nd/VoucherVault.svg?style=social&label=Watch" /></a><br>
    <a target="_blank" href="https://hub.docker.com/r/l4rm4nd/vouchervault"><img src="https://badgen.net/badge/icon/l4rm4nd%2Fvouchervault:latest?icon=docker&label" /></a><br><p>
    <a href="https://www.buymeacoffee.com/LRVT" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
</div>

## 💬 Description

VoucherVault is a Django web application that allows you to manage coupons, vouchers and gift cards digitally. It provides a web portal that is mobile friendly and easy to use. 

Additionally, it supports expiry notifications via Apprise URLs that will frequently remind you to redeem your stuff. You can also track fractional transactions, which help to understand historical redemptions and reflect the remaining monetary value of an item accurately.

Finally, redeem codes are nicely printed as QR code or EAN13 barcode.

## 🐳 Usage

````
docker compose -f docker/docker-compose.yml up
````

Once the container is up and running, you can access the web portal at http://127.0.0.1:8000. 

The default username is `admin`. The default password is auto-generated.

You can obtain the auto-generated password via the Docker container logs:

````
docker compose -f docker/docker-compose.yml logs -f
````

> [!WARNING]
> The container runs as low-privileged `www-data` user. So you have to adjust the permissions for the persistent database bind mount volume. A command like `sudo chown -R www-data:www-data <path-to-volume-data-dir>` should work. Afterwards, please restart the container.

## 🔔 Notifications

Notifications are handled by [Apprise](https://github.com/caronc/apprise). 

You can define custom Apprise URLs in the user profile settings. The input form takes a single or a comma-separated list of multiple Apprise URLs.

The interval, how often items are checked against a potential expiry, is pre-defined (every 10 days) in the Django admin area. Here, we are utilizing Django-Celery-Beat + a Redis instance for periodic task execution. If you want to adjust the crontab interval, please head over to the admin area at `/admin/django_celery_beat/periodictask/1/change/` (`Periodic Tasks` > `Periodic Expiry Check` > `Crontab Schedule`) and adjust to your liking.

An item will trigger an expiry notification if the expiry date is within the number of days defined by the environment variable `EXPIRY_THRESHOLD_DAYS`. By default, this threshold is set to 30 days.

## 📷 Screenshots

> [!TIP]
> Support for light and dark theme available!

<img src="screenshots/dashboard.png">

<img src="screenshots/items.png">

<img src="screenshots/item-details.png">

## 💾 Backups

All application data is stored within an SQLite3 database. The database is persistently stored within a Docker bind mount volume, which is defined in the `docker-compose.yml` file. The default location is defined as `./volume-data/database/db.sqlite3`.

Therefore, by backing up this bind mount volume, all your application data is saved.

> [!WARNING]
> Read the official [SQLite3 documentation](https://sqlite.org/backup.html) regarding backups.

### Manual Django Backups

You can alternatively dump the SQLite database content manually using Django's `manage.py`. This may help if something bricks and you have to re-import your application data into a freshly spawned VoucherVault container.

Proceed as follows:

#### Export data | Create Backup
````
# exec into the vouchervault container
docker exec -it vouchervault bash

# export sqlite3 database tables into outfile
python manage.py dumpdata auth.group > database/backup_db_table_groups.json
python manage.py dumpdata auth.user > database/backup_db_table_users.json
python manage.py dumpdata myapp.item > database/backup_db_table_items.json
python manage.py dumpdata myapp.transaction > database/backup_db_table_transactions.json
````

#### Import data | Recover Backup:
````
# import old backup outfiles into sqlite3
python manage.py loaddata database/backup_db_table_groups.json
python manage.py loaddata database/backup_db_table_users.json
python manage.py loaddata database/backup_db_table_items.json
python manage.py loaddata database/backup_db_table_transactions.json
````
