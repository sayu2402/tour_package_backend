from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='cities')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.country.name}"


class TourPackage(models.Model):
    title = models.CharField(max_length=200)
    source_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='source_packages')
    source_city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='source_packages')
    destination_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='destination_packages')
    destination_city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='destination_packages')
    description = models.TextField()
    terms_and_conditions = models.TextField()
    photos = models.ImageField(upload_to='package_photos/', blank=True, null=True)

    def __str__(self):
        return self.title


class PackageSchedule(models.Model):
    package = models.ForeignKey(TourPackage, on_delete=models.CASCADE, related_name='schedules')
    title = models.CharField(max_length=200)
    from_date = models.DateField()
    to_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    schedule_photos = models.ImageField(upload_to='schedule_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.package.title}"


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    related_schedule = models.ForeignKey(PackageSchedule, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.related_schedule if self.related_schedule else 'General Enquiry'}"
