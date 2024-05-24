from django.db import models
import uuid

class AbstractModels(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, db_index=True, editable=False, unique=True
        )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def soft_delete(self):
        self.is_active = False
        self.save()
    
    def restore(self):
        self.is_active = True
        self.save()
        
    class Meta:
        abstract = True