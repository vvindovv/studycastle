from django.db import models



class Review(models.Model):
    username = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    STAR_CHOICES = {
          ('1', '★'),
          ('2', '★★'),
          ('3', '★★★'),
          ('4', '★★★★'),
          ('5', '★★★★★'),
        }
    volume = models.CharField(max_length=5, choices=STAR_CHOICES, default='★')
    runningtime = models.CharField(max_length=5, choices=STAR_CHOICES, default='★')
    fun = models.CharField(max_length=5,choices=STAR_CHOICES, default='★')

    result = models.FloatField(default=0)

  
