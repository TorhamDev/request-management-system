from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=30)
    api = models.URLField()
    limit_by_sec = models.IntegerField(help_text="Provider limit by sec. e.g 5; means every 5 sec")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name