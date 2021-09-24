from django.db import models
from conduit.apps.core.models import TimestampedModel

class Management(TimestampedModel):

    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )

    breb_office_name_en=models.CharField(max_length=200, blank=True,null=True)
    breb_office_name_bn=models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return "%s %s" %(self.user.username,self.breb_office_name_en)

    # def __str__(self):
    #     return self.user.username