from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs'


class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'