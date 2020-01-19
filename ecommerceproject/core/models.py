from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
catageroy_choices=(
('sport wear','sport wear'),
('Outwear','Outwear'),
('shirt','shirt'),
('zeans','zeans')
)

label_choices=(
('primary','primary'),
('secondary','secondary'),
('danger','danger')
)
item_sal_choices=(
('new','new'),
('bestseller','bestseller')
)

class item(models.Model):
    title=models.CharField(max_length=30)
    slug=models.SlugField(max_length=120)
    catageroy=models.CharField(max_length=20,choices=catageroy_choices)
    label=models.CharField(max_length=20,choices=label_choices)
    sale_type=models.CharField(max_length=20,choices=item_sal_choices)
    price=models.FloatField()
    discount_price=models.FloatField(null=True,blank=True)
    discription=models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_view',kwargs={'slug':self.slug})
    def add_to_cart_url(self):
        return reverse('add_to_cart_view',kwargs={'slug':self.slug})

class orderitem(models.Model):
    # user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    order_item=models.ForeignKey(item,on_delete=models.CASCADE)
    # quantity=models.IntegerField(default=1)
    # ordered=models.BooleanField(default=False)

#
# class order(models.Model):
#     user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     item=models.ManyToManyField(orderitem)
#     ordered=models.BooleanField(default=False)
#     start_date=models.DateTimeField(auto_now_add=True)
#     odered_date=models.DateTimeField()
#     def __str__(self):
#         return user.username
