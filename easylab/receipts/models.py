from django.db import models

class Patient(models.Model):
    """
        patient information associated with lab visit
    """
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateField()
    ramq = models.CharField(max_length = 12)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length = 30)


    def __str__(self):
        return "Patient: " + self.first_name + ' ' + self.last_name

class Visit (models.Model):

    """ visit information during the visit """
    patient = models.ForeignKey(Patient)
    date = models.DateField()
    price = models.CharField(max_length=10)
    payment_type = models.CharField(max_length=10, blank = True, null = True)
    doctor_name = models.CharField(max_length=30, blank = True, null = True)
    receipt = models.FileField(blank = True, null = True)
    status = models.CharField(max_length=25, default="Not Completed")
