from django.db import models
from conduit.apps.core.models import TimestampedModel

class Management(TimestampedModel):

    user = models.OneToOneField(
        'authentication.User', on_delete=models.CASCADE
    )

    management_id=models.IntegerField(blank=True,null=True)
    management_name_en=models.CharField(max_length=100, blank=True,null=True)
    management_name_bn=models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "%s %s" %(self.user.username,self.management_name_en)

    # def __str__(self):
    #     return self.user.username