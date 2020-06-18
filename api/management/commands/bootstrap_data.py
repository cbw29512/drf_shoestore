#https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/
from django.core.management.base import BaseCommand, CommandError
from api.models import Manufacturer, ShoeType, ShoeColor, Shoe
class Command(BaseCommand):
    help = 'populate shoe type and populate shoe color'

    # Matt Perry assisted with code below!
    
    def handle(self, *args, **options):
        shoecolorlist= [
            'Red',
            'Orange',
            'Yellow',
            'Green',
            'Blue',
            'Indigo',
            'Violet',
            'White',
            'Black',
        ]
        shoetypelist= [
        'sneaker',
        'boot',
        'sandal',
        'dress',
        'other',
        ]
        for shoe_color in shoecolorlist:
            ShoeColor.objects.create(
                color_name = shoe_color
            )
        for shoe_type in shoetypelist:
            ShoeType.objects.create(
                style = shoe_type
            )
