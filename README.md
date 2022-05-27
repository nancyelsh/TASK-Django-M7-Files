Time to cook some burgers!

## Setup

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Django-M7-Files).
2. Create a `virtual environment`.
3. Install the requirements using `pip install -r requirements/dev.lock`.

## Steps

1. We need to set up our media files, so follow the steps [here](https://warehouse.joincoded.com/workshops/django-files/media-files/media-files-setup).
   - Make sure to install `Pillow`
2. Add an `ImageField` to our `Employee` model named `avatar`, and add a custom `upload_to` (follow the examples [here](https://docs.djangoproject.com/en/4.0/ref/models/fields/#django.db.models.FileField.upload_to)).
3. Make migrations and migrate.
4. Add some `restaurants` and `employees` using `Postman`.
