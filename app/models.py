from django.conf import settings
from django.db import models
from django.utils import timezone


class GlobalStatus(models.Model):
	message = models.CharField("ステータスメッセージ", max_length=200)
	processedReceptionTime = models.CharField("対応中患者の受付時間", max_length=200, blank=True, null=True)
	created = models.DateTimeField("作成日", default=timezone.now)
	modified = models.DateTimeField("更新日", auto_now=True)
     
	def __str__(self):
		return self.message
