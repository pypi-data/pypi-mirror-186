# Backend Base

Allows you to implement basic backend functionality for your application. Based on the [Django Framework](https://www.djangoproject.com/). It contains the followings packages of the Django Framework:

- [django.conf](https://docs.djangoproject.com/en/4.1/ref/settings/)
- [django.core.exceptions](https://docs.djangoproject.com/en/4.1/ref/exceptions/)
- [django.core.mail](https://docs.djangoproject.com/en/4.1/topics/email/)
- [django.utils.functional](https://docs.djangoproject.com/en/4.1/ref/utils/#module-django.utils.functional)

**Disclaimer**: This project is not affiliated with the Django Framework. This package contains code extracted from the Django framework, with the purpose of using certain functionality in other projects that do not have to do with django. The code has certain modifications but in theory it is based on the django structure

## Usage in your project

### Configuration

You need to define the following environment variables:

- `SETTINGS_MODULE_ENVIRONMENT_VARIABLE` (default: `config.settigs`): The environment variable that contains the path to the settings module of your project

### Environment variables

The following environment variables are used:

|                  Name                  |                 Default Value                  | Overwrite required | Description                                                                                 |                                                   Reference                                                    |
| :------------------------------------: | :--------------------------------------------: | :----------------: | ------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------: |
| `SETTINGS_MODULE_ENVIRONMENT_VARIABLE` |               `config.settings`                |        Yes         | The path to the settings module of your project                                             | [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#std:setting-DJANGO_SETTINGS_MODULE) |
|            `EMAIL_BACKEND`             | `backend_base.mail.backends.smtp.EmailBackend` |        Yes         | The email backend to use (Replace `django` for `backend_base`)                              |           [Django Documentation](https://docs.djangoproject.com/en/4.1/topics/email/#email-backends)           |
|              `EMAIL_HOST`              |                  `localhost`                   |        Yes         | The host to use for sending email.                                                          |             [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#email-host)             |
|              `EMAIL_PORT`              |                      `25`                      |        Yes         | The port to use for the SMTP server specified in EMAIL_HOST.                                |             [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#email-port)             |
|         `EMAIL_USE_LOCALTIME`          |                    `False`                     |         No         | Whether to use the local time when formatting dates in email messages.                      |        [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#email-use-localtime)         |
|           `EMAIL_HOST_USER`            |                      `''`                      |        Yes         | Username to use for the SMTP server specified in EMAIL_HOST.                                |          [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#email-host-user)           |
|         `EMAIL_HOST_PASSWORD`          |                      `''`                      |        Yes         | Password to use for the SMTP server specified in EMAIL_HOST.                                |        [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#email-host-password)         |
|            `EMAIL_USE_TLS`             |                    `False`                     |         No         | Whether to use a TLS (secure) connection when talking to the SMTP server.                   |           [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#email-use-tls)            |
|            `EMAIL_USE_SSL`             |                    `False`                     |         No         | Whether to use an implicit TLS (secure) connection when talking to the SMTP server.         |           [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#email-use-ssl)            |
|            `EMAIL_TIMEOUT`             |                     `None`                     |         No         | A timeout in seconds for blocking operations like the connection attempt.                   |           [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#email-timeout)            |
|          `EMAIL_SSL_KEYFILE`           |                     `None`                     |         No         | The filename of a private key file for use in SSL connections.                              |         [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#email-ssl-keyfile)          |
|          `EMAIL_SSL_CERTFILE`          |                     `None`                     |         No         | The filename of a certificate file for use in SSL connections.                              |         [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#email-ssl-certfile)         |
|            `DEFAUL_CHARSET`            |                    `utf-8`                     |         No         | The default character set to use for the email.                                             |          [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#default-charset)           |
|             `SERVER_EMAIL`             |                `root@localhost`                |         No         | The email address that error messages come from, such as those sent to ADMINS and MANAGERS. |            [Django Documentation](https://docs.djangoproject.com/en/4.1/ref/settings/#server-email)            |
