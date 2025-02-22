from django.db import models


# Create your models here.
class UzSentTokenization(models.Model):
    word = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.word
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'UzSentTokenization'
        verbose_name_plural = 'UzSentTokenizations'
        indexes = [
            models.Index(fields=['word'], name='word'),
        ]
    

class Yuklamalar(models.Model):
    word_yuklamalar = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.word_yuklamalar

    class Meta:
        verbose_name = 'Yuklamalar'
        verbose_name_plural = 'Yuklamalar'
        indexes = [
            models.Index(fields=['word_yuklamalar'], name='word_yuklamalar'),
        ]