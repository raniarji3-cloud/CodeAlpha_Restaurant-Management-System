from django.db import migrations


MENU_ITEMS = [
    ('Burger', 'Fast Food', '120.00', 'RMSysApp/images/burger.jpg'),
    ('Pizza', 'Fast Food', '250.00', 'RMSysApp/images/pizza.jpg'),
    ('Chicken Biryani', 'Main Course', '220.00', 'RMSysApp/images/Chicken-Biryani.jpg'),
    ('Veg Fried Rice', 'Main Course', '160.00', 'RMSysApp/images/veg-fried-rice.jpg'),
    ('Chicken Noodles', 'Main Course', '180.00', 'RMSysApp/images/chicken-noodles.jpg'),
    ('Chilly Chicken', 'Starter', '200.00', 'RMSysApp/images/Chilly-chicken.jpg'),
    ('Fish Fry', 'Starter', '210.00', 'RMSysApp/images/Fish-Fry.jpg'),
    ('KFC Chicken', 'Starter', '240.00', 'RMSysApp/images/KFC-Chicken.jpg'),
    ('Mushroom Curry', 'Main Course', '170.00', 'RMSysApp/images/Mushroom-curry.jpg'),
    ('Pani Puri', 'Snack', '60.00', 'RMSysApp/images/panipuri.jpg'),
    ('Papdi Chat', 'Snack', '80.00', 'RMSysApp/images/Chat.jpg'),
    ('Mango Shake', 'Beverage', '90.00', 'RMSysApp/images/mango-shake.jpg'),
    ('Caramel Pudding', 'Dessert', '110.00', 'RMSysApp/images/caramel-pudding.jpg'),
]


def seed_menu_items(apps, schema_editor):
    MenuItem = apps.get_model('RMSysApp', 'MenuItem')

    for name, category, price, image in MENU_ITEMS:
        MenuItem.objects.get_or_create(
            name=name,
            defaults={
                'category': category,
                'price': price,
                'image': image,
                'available': True,
            },
        )


def unseed_menu_items(apps, schema_editor):
    MenuItem = apps.get_model('RMSysApp', 'MenuItem')
    MenuItem.objects.filter(name__in=[item[0] for item in MENU_ITEMS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('RMSysApp', '0007_menuitem_image'),
    ]

    operations = [
        migrations.RunPython(seed_menu_items, unseed_menu_items),
    ]
