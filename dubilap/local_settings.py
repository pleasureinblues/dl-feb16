"""
Local Settings
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dubilapdbfeb',
        'USER': 'admin',
        'PASSWORD': 'optimist',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


####### EMAIL CONF ########
#
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = 'enquiry.dubailap@gmail.com'
# EMAIL_HOST_PASSWORD = 'sonyericssonw200i'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True



EMAIL_HOST = 'mail.dubilap.com'
EMAIL_HOST_USER = 'info@dubilap.com'
EMAIL_HOST_PASSWORD = 'Londonboy1'
EMAIL_PORT = 25
EMAIL_USE_TLS = False

