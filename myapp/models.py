# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ShopBrands(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(unique=True, max_length=50)
    brand_slug = models.CharField(unique=True, max_length=100, blank=True, null=True)
    brand_details = models.TextField(blank=True, null=True)
    brand_logo = models.CharField(max_length=200, blank=True, null=True)
    views = models.BigIntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_brands'

    def __str__(self) -> str:
        return self.brand_name

class ShopCategories(models.Model):
    category_id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField()
    category_name = models.CharField(max_length=50)
    category_slug = models.CharField(unique=True, max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_categories'


class ShopLocations(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=50, blank=True, null=True)
    location_slug = models.CharField(unique=True, max_length=50, blank=True, null=True)
    location_map = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_locations'


class ShopOffers(models.Model):
    offer_id = models.AutoField(primary_key=True)
    offer_title = models.CharField(max_length=150, blank=True, null=True)
    offer_slug = models.CharField(unique=True, max_length=150, blank=True, null=True)
    offer_details = models.TextField(blank=True, null=True)
    offer_brands = models.CharField(max_length=200, blank=True, null=True)
    offer_photo = models.CharField(max_length=200, blank=True, null=True)
    add_date = models.DateField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_offers'


class ShopPages(models.Model):
    page_id = models.AutoField(primary_key=True)
    page_title = models.CharField(max_length=100)
    page_slug = models.CharField(unique=True, max_length=100)
    page_details = models.TextField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_pages'


class ShopPosts(models.Model):
    post_id = models.AutoField(primary_key=True)
    category_id = models.IntegerField(blank=True, null=True)
    product_id = models.CharField(max_length=100, blank=True, null=True)
    post_title = models.CharField(max_length=255, blank=True, null=True)
    post_slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    post_details = models.TextField(blank=True, null=True)
    add_date = models.DateField(blank=True, null=True)
    views = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    pimage = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_posts'


class ShopProducts(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.IntegerField()
    brand_id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=255, blank=True, null=True)
    product_slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    seo_title = models.CharField(max_length=100, blank=True, null=True)
    seo_description = models.CharField(max_length=320, blank=True, null=True)
    product_model = models.CharField(max_length=50, blank=True, null=True)
    product_details = models.TextField(blank=True, null=True)
    product_features = models.TextField(blank=True, null=True)
    product_price = models.IntegerField(blank=True, null=True)
    product_photo = models.CharField(max_length=120, blank=True, null=True)
    add_date = models.DateField(blank=True, null=True)
    modify_date = models.DateField(blank=True, null=True)
    views = models.IntegerField()
    status = models.IntegerField()
    popular_product = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shop_products'


class ShopShowrooms(models.Model):
    showroom_id = models.AutoField(primary_key=True)
    location_id = models.IntegerField()
    showroom_name = models.CharField(max_length=100, blank=True, null=True)
    showroom_slug = models.CharField(unique=True, max_length=150, blank=True, null=True)
    seo_title = models.CharField(max_length=300, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    showroom_address = models.CharField(max_length=255, blank=True, null=True)
    showroom_phones = models.CharField(max_length=50, blank=True, null=True)
    showroom_email = models.CharField(max_length=100, blank=True, null=True)
    showroom_web = models.CharField(max_length=150, blank=True, null=True)
    showroom_hours = models.TextField(blank=True, null=True)
    showroom_map = models.CharField(max_length=50, blank=True, null=True)
    showroom_brands = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_showrooms'


class ShopUsers(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    user_email = models.CharField(unique=True, max_length=255)
    user_password = models.CharField(max_length=32)
    user_address = models.CharField(max_length=255)
    location_id = models.IntegerField()
    user_phone = models.CharField(max_length=15)
    user_photo = models.CharField(max_length=100, blank=True, null=True)
    add_datetime = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shop_users'


class ShopVisitors(models.Model):
    user_id = models.IntegerField()
    user_ip = models.CharField(max_length=50)
    timestamp = models.IntegerField()
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'shop_visitors'
