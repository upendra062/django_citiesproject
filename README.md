# Activate environment
```
source venv/bin/activate
```
# Install django
```
pip install django
```
# Run Django Server
```
python manage.py runserver
```


# DATA BASES COMMANDS
# Saving the Changes
```
python manage.py makemigration
```
# Applying the changes to database
```
python manage.py migrate
```
# show the command used to create the table 
```
python manage.py sqlmigrate cities 0001
```
# Open Shell
```
python manage.py shell
```

```
from cities.models import Cities
```

# Here show empty list in starting
```
Cities.objects.all()
```

# Adding data in Cities
```
city=Cities(firstname='Upendra',lastname='Singh')
city.save()
```

# Checking the Stored data
```
Cities.objects.all()
```

# See values in the data
```
Cities.objects.all().values()
```

# Adding a new entry
```
city1=Cities(firstname='sonu',lastname='Singh')
city2=Cities(firstname='monu',lastname='Singh')
```

# Adding Above entry through loop
```
cityArr = [city1, city2]
for i in cityArr:
    i.save()
```

# python shell
```
python manage.py shell
```

# import and see what is saved inside cities.models
```
from cities.models import Cities 
Cities.objects.all()
Cities.objects.all().values()
Cities.objects.all().values()[0] 
Cities.objects.all().values()[2] 
```

# For Saving Multiple Data
```
member1 = Cities(firstname='rohan', lastname='singh')
member2 = Cities(firstname='raju', lastname='singh')
cityArr = [member1, member2]
for item in cityArr:
    item.save()
```

# Fetch values from database
```
a = Cities.objects.all()[2]
a.firstname
```

# updating the record 
```
a.firstname = "jadugar"
a.save()

a.firstname
```

# delete the record
```
a.delete()

Cities.objects.all().values()
```

#
```
city10 = Cities(firstname="Joe", lastname="Jane")
city10.save()
Cities.objects.all().values()

```

# Adding columns app cities in Cities 
```
    mobile = models.IntegerField(null=True)
    birth_date = models.DateField(null=True)
```

# Adding values in null field
```
a = Cities.objects.all()[0]
a.mobile=7974140362 
a.save()


```

# Adding birthdate where it is null
```
It must be in YYYY-MM-DD format.

a = Cities.objects.all()[0]
a.birth_date = '1996-02-26'
a.save()


```

#
```

```

#
```

```

#
```

```
