from django.db import models

# <th>Номер сотрудника</th>
# <th>Имя</th>
# <th>Должность</th>
# <th>Дата принятия на работу</th>
# <th>Департмент</th>
# <th>Удалить</th>

class Employee(models.Model):
    name = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    dateOfHiring = models.DateField()
    departments = models.CharField(max_length=200)

    def __str__(self):
        return self.name
