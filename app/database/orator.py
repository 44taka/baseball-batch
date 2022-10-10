import os

DATABASES = {
    'mysql': {
        'driver': 'mysql',
        'host': os.getenv('MYSQL_HOST'),
        'database': os.getenv('MYSQL_DATABASE'),
        'user': os.getenv('MYSQL_USER'),
        'password': os.getenv('MYSQL_PASSWORD'),
        'prefix': ''
    }
}
