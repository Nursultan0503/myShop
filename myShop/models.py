from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = (
        ('phones', 'Смартфоны'),
        ('laptops', 'Ноутбуки'),
        ('audio', 'Аудио'),
        ('tv', 'Телевизоры'),
        ('accessories', 'Аксессуары'),
    )

    # Ровно 8 полей
    title = models.CharField(max_length=150, verbose_name="Название")                    # 1
    brand = models.CharField(max_length=100, verbose_name="Бренд")                       # 2
    description = models.TextField(blank=True, verbose_name="Описание")                  # 3
    image = models.ImageField(upload_to='products/', blank=True, null=True,
                              verbose_name="Фото")                                       # 4
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,
                                verbose_name="Категория")                                # 5
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")   # 6
    quantity = models.PositiveIntegerField(default=0, verbose_name="В наличии (шт.)")   # 7
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления") # 8

    def __str__(self):
        return f"{self.brand} {self.title}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['-created_at']


# ОДИН К ОДНОМУ: у одного товара только один серийный номер
class SerialNumber(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name='serial_number', verbose_name="Товар"
    )
    number = models.CharField(max_length=50, unique=True, verbose_name="Серийный номер")
    warranty_months = models.PositiveIntegerField(default=12, verbose_name="Гарантия (мес.)")

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Серийный номер"
        verbose_name_plural = "Серийные номера"


# ОДИН КО МНОГИМ: у одного товара много комментариев
class ProductComment(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='comments', verbose_name="Товар"
    )
    author = models.CharField(max_length=100, verbose_name="Имя")
    text = models.TextField(verbose_name="Отзыв")
    rating = models.PositiveSmallIntegerField(
        choices=[(i, '★' * i) for i in range(1, 6)], default=5, verbose_name="Оценка"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return f"{self.author}: {self.product}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ['-created_at']
