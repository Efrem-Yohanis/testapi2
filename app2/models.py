from django.db import models

# Profile Model
class Profile(models.Model):
    login_entity_id = models.CharField(max_length=255)
    entity = models.CharField(max_length=255)
    entity_id = models.CharField(max_length=255)
    advisor_name = models.CharField(max_length=255)
    entity_name = models.CharField(max_length=255)
    role_id = models.CharField(max_length=255)
    is_user_default = models.BooleanField(default=False)
    al_client_id = models.CharField(max_length=255)
    role_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Profile {self.id} - {self.entity_name}"

# User Model
class User(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    contact_type = models.CharField(max_length=255)
    entity_name = models.CharField(max_length=255)
    profiles = models.ManyToManyField(Profile, related_name='users')

    def __str__(self):
        return f"User {self.user_id} - {self.first_name} {self.last_name}"
