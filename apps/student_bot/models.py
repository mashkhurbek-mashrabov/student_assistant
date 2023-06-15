from django.db import models

from common.constants import LanguageChoices
from common.models import BaseModel


class StudentTelegramUser(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    chat_id = models.BigIntegerField(unique=True)
    language = models.CharField(max_length=5, null=True, blank=True, choices=LanguageChoices.choices,
                                default=LanguageChoices.UZBEK)
    step = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.chat_id} - {self.name}'

    @property
    def joined_at(self):
        return f'{self.date.strftime("%X")} {self.date.strftime("%x")}'