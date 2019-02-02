from django.db import models


# Create your models here.
class Scout(models.Model):
    person = models.CharField(max_length=45)
    robot_number = models.IntegerField()
    match_number = models.IntegerField()
    hatches_secured = models.IntegerField(default=0)
    event_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'robot number: ' + str(self.robot_number) + ' | match number: ' + str(self.match_number)

    class Meta:
        ordering = ['match_number']
