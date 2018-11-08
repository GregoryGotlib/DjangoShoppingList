from django.db import models

# This class notify django to create a "List" table in my DB, with three columns:
# 'id' column which generated automatically by django
# 'item' will be my product title 
# 'added' to check if this item has been added to my cart

class List(models.Model):
    item = models.CharField(max_length=50,unique=True)
    added = models.BooleanField(default=False)

    # The same as toString in JAVA
    def __str__(self):
        return self.item + ' ' + str(self.added)
    