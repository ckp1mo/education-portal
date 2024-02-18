from rest_framework.serializers import ValidationError


class VideoLinkValidator:
    """ Проверка на отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com"""
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_value = dict(value).get(self.field)
        if tmp_value is not None and 'youtube.com' not in tmp_value:
            raise ValidationError('Допускается ссылка только на ютуб')
