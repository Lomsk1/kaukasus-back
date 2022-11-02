import os
from django.db import models


class Employees(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    avatar = models.ImageField(default="./employees/employee_default.jpg", upload_to="./employees")

    def img_delete(self, image, *args, **kwargs):
        if os.path.isfile(image):
            img_path = os.path.join("kaukasus-travel-api", image)
            os.remove(img_path)
