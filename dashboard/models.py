from django.db import models

# Create your models here.

RETROFIT_CHOICES = (
    ('Pump', 'Pump'),
    ('Boiler', 'Boiler')
)

BOOLEAN_CHOICE = (
    (1, 1),
    (0, 0)
)


PUMP_CHOICE = (
    (1, 1),
    (2, 2)
)

RETROFIT_NUMBER = (
    (1, 1),
    (3, 3)
)


class Building(models.Model):

    bdbid = models.IntegerField(unique=True)
    building_name = models.CharField(max_length=150)
    retrofit_type = models.CharField(max_length=150, choices=RETROFIT_CHOICES)

    def __str__(self):
        return '<Building: {}, {}, {}>'.format(self.bdbid, self.building_name, self.retrofit_type)


class Pump(models.Model):

    bdbid = models.ForeignKey('Building', to_field='bdbid', on_delete=models.CASCADE)
    pre_post = models.IntegerField(choices=RETROFIT_NUMBER)
    date_time = models.DateTimeField()
    motor_on = models.IntegerField(choices=BOOLEAN_CHOICE)
    motor_off = models.IntegerField(choices=BOOLEAN_CHOICE)
    pump = models.IntegerField(choices=PUMP_CHOICE)

    def __str__(self):
        return '<Pump: {}, {}, {}>'.format(self.bdbid, self.pre_post, self.date_time)


class Boiler(models.Model):

    bdbid = models.ForeignKey('Building', to_field='bdbid', on_delete=models.CASCADE)
    pre_post = models.IntegerField(choices=RETROFIT_NUMBER)
    date_time = models.DateTimeField()
    second_on = models.IntegerField()
    usage_ccf = models.FloatField()
    temperature = models.FloatField()
    hdd_60 = models.FloatField()
    hdd_62_5 = models.FloatField()
    hdd_65 = models.FloatField()
    hdd_67_5 = models.FloatField()
    hdd_70 = models.FloatField()

    def __str__(self):
        return '<Boiler: {}, {}, {}>'.format(self.bdbid, self.pre_post, self.date_time)
