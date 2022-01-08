from django.db import models

STATUS_CHOIСES = [('active', 'Активна'), ('blocked', 'Заблокировано')]

class FaceBook(models.Model):
    name_author = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя автора')
    email = models.EmailField(null=False, blank=False, verbose_name='Почта')
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст записи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    status = models.CharField(max_length=15, default='active', choices=STATUS_CHOIСES, verbose_name="Статус")

    def __str__(self):
        return f"{self.pk}.{self.name_author}"

    class Meta:
        db_table = 'FaceBook'
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'