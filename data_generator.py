import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SafeMove.settings")
django.setup()

from mapshow.models import VisitorEvent, VisualData
import random

def insert_random_data(upper_left, bottom_right, t, times):
    print('Inserting data in area: ', upper_left, bottom_right)
    for _ in range(times):
        x = random.uniform(upper_left[0], bottom_right[0])
        y = random.uniform(upper_left[1], bottom_right[1])
        x = round(x, 5)
        y = round(y, 5)
        VisualData.objects.create(count=random.randint(1, 10),lat=x,lng=y, tag=t)

if __name__ == '__main__':
    import sys
    insert_random_data((float(sys.argv[1]), float(sys.argv[2])),
        (float(sys.argv[3]), float(sys.argv[4])), int(sys.argv[5]), int(sys.argv[6]))

# python3 data_generator.py 30.7912850000 103.8997770000 30.5298430000 104.2412770000 0 5000 
