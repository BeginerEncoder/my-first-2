import datetime
from django.db import models

from django.utils import timezone

class Advert(models.Model):
    advert_title = models.CharField('Название', max_length = 200)
    advert_text = models.TextField('Текст обьявления')
    pub_date = models.DateTimeField('Дата публикации')
    
    def __str__(self):
        return self.advert_title

    def was_published_resently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    go = models.ForeignKey(Advert, on_delete = models.CASCADE)
    author_name = models.CharField('Имя автора', max_length = 30)
    comment_text = models.CharField('Текст комментария', max_length = 200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
