from rest_framework import serializers
from .models import Booking, Menu



class Bookingserial(serializers.ModelSerializer): 
    class Meta: 
        model = Booking
        fields = ['id', 'first_name', 'reservation_date', 'reservation_slot']



class Menuserial(serializers.ModelSerializer): 
    class Meta: 
        model = Menu
        fields = ['id', 'name', 'price', 'menu_item_description']
