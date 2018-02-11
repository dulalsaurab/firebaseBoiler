from django.db import models
from ckeditor.fields import RichTextField
from mediumeditor.admin import MediumEditorAdmin
# Create your models here.
from django.utils import timezone

class postArticles(models.Model):

    #foregin key will help link this models(table) to some other models
    author = models.ForeignKey(
        'auth.User',
         on_delete=models.DO_NOTHING, #what action to perform when foreignKey is deleted (CASCADE, DO_NOTHING)
    )
    title = models.CharField(max_length=100)
    shortInfo = models.CharField(max_length=200)
    text = RichTextField(config_name='default')
    # text1 = RichTextField(config='basic')
    tags = models.CharField(max_length=100)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publishArticle(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
