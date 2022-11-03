from django.db import models


class CategoryModel(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT, verbose_name='Bo\'limlar:', related_name='product', blank=True)
    title = models.CharField(max_length=255, verbose_name='Mahsulot nomi:')
    price = models.FloatField(verbose_name='Narxi:')
    description = models.TextField(null=True, verbose_name='Mahsulot ma\'lumoti:', blank=True)
    image = models.ImageField(upload_to='products', verbose_name='Rasmi:')

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class TelegramUserModel(models.Model):
    tg_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tg_id}'

    class Meta:
        verbose_name = 'Telegram user'
        verbose_name_plural = 'Telegram users'


STATUS = (
    ('Kutilmoqda', 'Kutilmoqda'),
    ('Bekor Qilindi', 'Bekor Qilindi'),
    ('Tasdiqlandi', 'Tasdiqlandi'),
    ('Yuborildi', 'Yuborildi'),
    ('Yetkazildi', 'Yetkazildi'),
)


class OrderModel(models.Model):
    user = models.ForeignKey(TelegramUserModel, on_delete=models.CASCADE)
    product = models.TextField()
    price = models.CharField(max_length=100, verbose_name='Narxi:')
    address = models.CharField(max_length=200, null=True, blank=True)
    number = models.CharField(max_length=15)
    order = models.CharField(max_length=50, choices=STATUS, default='Kutilmoqda')
    kuryer = models.CharField(max_length=255,null=True, blank=True)
    date = models.CharField(max_length=255, null=True, verbose_name='Sana', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'


class KorzinaModel(models.Model):
    user_id = models.BigIntegerField()
    product = models.CharField(max_length=255, verbose_name='Mahsulot nomi:')
    count = models.IntegerField(verbose_name='Soni')
    price = models.FloatField(verbose_name='Narxi:')

