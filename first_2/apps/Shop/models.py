from django.db import models
import datetime
from django.utils import timezone
now = datetime.datetime.now()

#now = datetime.datetime.now()

class Product(models.Model):
    product_title = models.CharField('Название игры', max_length = 150)
    product_text = models.TextField('О товаре')
    product_image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    product_price = models.IntegerField()
    pub_date = models.DateTimeField('Дата публикации',auto_now_add=True)
    
    @property
    def photo_url(self):
        if self.product_image and hasattr(self.product_image, 'url'):
            return self.product_image.url

    def __str__(self):
        return self.product_title

    def was_published_resently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Comment(models.Model):
    go = models.ForeignKey(Product, on_delete = models.CASCADE)
    author_name = models.CharField('Имя автора', max_length = 30)
    comment_text = models.CharField('Текст комментария', max_length = 200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
# Create your models here.
