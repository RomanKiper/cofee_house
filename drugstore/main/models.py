from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='название'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='название'
    )
    descr = models.CharField(
        max_length=2048,
        verbose_name='описание'
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='публикация'
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='картинка'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        verbose_name='категория'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'main_products'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'


WEEK = (
    ('Monday', 'понедельник'),
    ('Tuesday', 'вторник'),
    ('Wednesday', 'среда'),
    ('Thursday', 'четверг'),
    ('Friday', 'пятница'),
    ('Saturday', 'суббота'),
    ('Sunday', 'воскресенье'),
)


class WorkSchedule(models.Model):
    week_day = models.CharField(
        max_length=15,
        verbose_name='день недели',
        unique=True,
        choices=WEEK
    )
    opening_time = models.TimeField(
        verbose_name='время открытия',
        null=True,
        blank=True
    )
    closing_time = models.TimeField(
        verbose_name='время закрытия',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.week_day

    class Meta:
        db_table = 'main_work_schedule'
        verbose_name = 'график работы'
        verbose_name_plural = 'график работы'