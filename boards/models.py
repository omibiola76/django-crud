# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Client(models.Model):
    # id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    # created_timestamp = models.IntegerField(db_column='CREATED_TIMESTAMP', blank=True, null=True)  # Field name made lowercase.
    fname = models.TextField(db_column='FNAME', blank=True, null=True)  # Field name made lowercase.
    lname = models.TextField(db_column='LNAME', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='EMAIL', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='PHONE', blank=True, null=True)  # Field name made lowercase.
    company = models.TextField(db_column='COMPANY')  # Field name made lowercase.
    team_lead = models.TextField(db_column='TEAM_LEAD')  # Field name made lowercase.
    speciality = models.TextField(db_column='SPECIALITY')  # Field name made lowercase.
    scope_of_work = models.TextField(db_column='SCOPE_OF_WORK')  # Field name made lowercase.
    preferred_manufacturers = models.TextField(db_column='PREFERRED_MANUFACTURERS')  # Field name made lowercase.
    style_frequency = models.TextField(db_column='STYLE_FREQUENCY')  # Field name made lowercase.
    qanda = models.TextField(db_column='QANDA')  # Field name made lowercase.
    service_needs = models.TextField(db_column='SERVICE_NEEDS')  # Field name made lowercase.
    service_suggestions = models.TextField(db_column='SERVICE_SUGGESTIONS')  # Field name made lowercase.
    additional_services = models.TextField(db_column='ADDITIONAL_SERVICES')  # Field name made lowercase.
    password = models.TextField(db_column='PASSWORD')  # Field name made lowercase.
    referrer = models.TextField(db_column='REFERRER')  # Field name made lowercase.
    start_date = models.TextField(db_column='START_DATE')  # Field name made lowercase.
    daily_storage_rate = models.DecimalField(db_column='DAILY_STORAGE_RATE', max_digits=10, decimal_places=2)  # Field name made lowercase.
    hourly_rate = models.DecimalField(db_column='HOURLY_RATE', max_digits=10, decimal_places=2)  # Field name made lowercase.
    lock_out = models.IntegerField(db_column='LOCK_OUT')  # Field name made lowercase.
    consult_date = models.DateField(db_column='CONSULT_DATE')  # Field name made lowercase.
    consult_time = models.TextField(db_column='CONSULT_TIME')  # Field name made lowercase.
    consult_location = models.TextField(db_column='CONSULT_LOCATION')  # Field name made lowercase.
    billing_note = models.TextField(db_column='BILLING_NOTE')  # Field name made lowercase.
    address1 = models.TextField(db_column='ADDRESS1')  # Field name made lowercase.
    address2 = models.TextField(db_column='ADDRESS2')  # Field name made lowercase.
    city = models.TextField(db_column='CITY')  # Field name made lowercase.
    state = models.TextField(db_column='STATE')  # Field name made lowercase.
    zip = models.TextField(db_column='ZIP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client'


class ClientContact(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    fname = models.TextField(db_column='FNAME')  # Field name made lowercase.
    lname = models.TextField(db_column='LNAME')  # Field name made lowercase.
    email = models.TextField(db_column='EMAIL')  # Field name made lowercase.
    phone = models.TextField(db_column='PHONE')  # Field name made lowercase.
    scope = models.TextField(db_column='SCOPE')  # Field name made lowercase.
    archived = models.IntegerField(db_column='ARCHIVED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client_contact'


class ClientEmailLog(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TIMESTAMP')  # Field name made lowercase.
    emailto = models.TextField(db_column='EMAILTO')  # Field name made lowercase.
    subject = models.TextField(db_column='SUBJECT')  # Field name made lowercase.
    body = models.TextField(db_column='BODY')  # Field name made lowercase.
    notes = models.TextField(db_column='NOTES')  # Field name made lowercase.
    headers = models.TextField(db_column='HEADERS')  # Field name made lowercase.
    result = models.TextField(db_column='RESULT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client_email_log'


class Customer(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    created_timestamp = models.IntegerField(db_column='CREATED_TIMESTAMP')  # Field name made lowercase.
    fname = models.TextField(db_column='FNAME')  # Field name made lowercase.
    lname = models.TextField(db_column='LNAME')  # Field name made lowercase.
    address = models.TextField(db_column='ADDRESS')  # Field name made lowercase.
    city = models.TextField(db_column='CITY')  # Field name made lowercase.
    state = models.TextField(db_column='STATE')  # Field name made lowercase.
    zip = models.TextField(db_column='ZIP')  # Field name made lowercase.
    phone = models.TextField(db_column='PHONE')  # Field name made lowercase.
    email = models.TextField(db_column='EMAIL')  # Field name made lowercase.
    start_date = models.DateField(db_column='START_DATE')  # Field name made lowercase.
    start_time = models.TextField(db_column='START_TIME')  # Field name made lowercase.
    scope_of_work = models.TextField(db_column='SCOPE_OF_WORK')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerItem(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    received_date = models.TextField(db_column='RECEIVED_DATE')  # Field name made lowercase.
    inspected_by = models.TextField(db_column='INSPECTED_BY')  # Field name made lowercase.
    location_aisle = models.TextField(db_column='LOCATION_AISLE')  # Field name made lowercase.
    location_row = models.TextField(db_column='LOCATION_ROW')  # Field name made lowercase.
    location_level = models.TextField(db_column='LOCATION_LEVEL')  # Field name made lowercase.
    item_name = models.TextField(db_column='ITEM_NAME')  # Field name made lowercase.
    item_manufacturer = models.TextField(db_column='ITEM_MANUFACTURER')  # Field name made lowercase.
    delivery_requested = models.IntegerField(db_column='DELIVERY_REQUESTED')  # Field name made lowercase.
    delivery_requested_date = models.IntegerField(db_column='DELIVERY_REQUESTED_DATE')  # Field name made lowercase.
    storage_billed_to = models.DateField(db_column='STORAGE_BILLED_TO')  # Field name made lowercase.
    customer_reference_number = models.TextField(db_column='CUSTOMER_REFERENCE_NUMBER')  # Field name made lowercase.
    damageflag = models.IntegerField(db_column='DAMAGEFLAG')  # Field name made lowercase.
    damageplace = models.TextField(db_column='DAMAGEPLACE')  # Field name made lowercase.
    damagekind = models.TextField(db_column='DAMAGEKIND')  # Field name made lowercase.
    damagenotes = models.TextField(db_column='DAMAGENOTES')  # Field name made lowercase.
    damagefollowupdate = models.DateField(db_column='DAMAGEFOLLOWUPDATE')  # Field name made lowercase.
    damagefollowuptime = models.TextField(db_column='DAMAGEFOLLOWUPTIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer_item'


class CustomerItemImages(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ITEMID')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    image_url = models.TextField(db_column='IMAGE_URL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer_item_images'


class Delivery(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    delivery_date = models.DateField(db_column='DELIVERY_DATE')  # Field name made lowercase.
    delivery_time = models.TextField(db_column='DELIVERY_TIME')  # Field name made lowercase.
    delivery_location = models.TextField(db_column='DELIVERY_LOCATION')  # Field name made lowercase.
    create_date = models.IntegerField(db_column='CREATE_DATE')  # Field name made lowercase.
    archived = models.IntegerField(db_column='ARCHIVED')  # Field name made lowercase.
    completed_flag = models.IntegerField(db_column='COMPLETED_FLAG')  # Field name made lowercase.
    completed_timestamp = models.IntegerField(db_column='COMPLETED_TIMESTAMP')  # Field name made lowercase.
    completed_billtype = models.TextField(db_column='COMPLETED_BILLTYPE')  # Field name made lowercase.
    invoice_hours = models.DecimalField(db_column='INVOICE_HOURS', max_digits=6, decimal_places=2)  # Field name made lowercase.
    invoice_hourly_rate = models.DecimalField(db_column='INVOICE_HOURLY_RATE', max_digits=10, decimal_places=2)  # Field name made lowercase.
    invoice_flat_rate = models.DecimalField(db_column='INVOICE_FLAT_RATE', max_digits=12, decimal_places=2)  # Field name made lowercase.
    invoice_subtotal = models.DecimalField(db_column='INVOICE_SUBTOTAL', max_digits=12, decimal_places=2)  # Field name made lowercase.
    invoiceid = models.IntegerField(db_column='INVOICEID')  # Field name made lowercase.
    notes = models.TextField(db_column='NOTES')  # Field name made lowercase.
    crew_number = models.IntegerField(db_column='CREW_NUMBER')  # Field name made lowercase.
    crew_name = models.TextField(db_column='CREW_NAME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'delivery'


class DeliveryEquipment(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    delivery_id = models.IntegerField(db_column='DELIVERY_ID')  # Field name made lowercase.
    equipment = models.TextField(db_column='EQUIPMENT')  # Field name made lowercase.
    archived = models.IntegerField(db_column='ARCHIVED')  # Field name made lowercase.
    cost = models.DecimalField(db_column='COST', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'delivery_equipment'


class DeliveryItems(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    delivery_id = models.IntegerField(db_column='DELIVERY_ID')  # Field name made lowercase.
    customer_item_id = models.IntegerField(db_column='CUSTOMER_ITEM_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'delivery_items'


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


class Fullinstall(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    delivery_date = models.DateField(db_column='DELIVERY_DATE')  # Field name made lowercase.
    delivery_time = models.TextField(db_column='DELIVERY_TIME')  # Field name made lowercase.
    delivery_location = models.TextField(db_column='DELIVERY_LOCATION')  # Field name made lowercase.
    create_date = models.IntegerField(db_column='CREATE_DATE')  # Field name made lowercase.
    archived = models.IntegerField(db_column='ARCHIVED')  # Field name made lowercase.
    completed_flag = models.IntegerField(db_column='COMPLETED_FLAG')  # Field name made lowercase.
    completed_timestamp = models.IntegerField(db_column='COMPLETED_TIMESTAMP')  # Field name made lowercase.
    completed_billtype = models.TextField(db_column='COMPLETED_BILLTYPE')  # Field name made lowercase.
    invoice_hours = models.DecimalField(db_column='INVOICE_HOURS', max_digits=6, decimal_places=2)  # Field name made lowercase.
    invoice_hourly_rate = models.DecimalField(db_column='INVOICE_HOURLY_RATE', max_digits=10, decimal_places=2)  # Field name made lowercase.
    invoice_flat_rate = models.DecimalField(db_column='INVOICE_FLAT_RATE', max_digits=12, decimal_places=2)  # Field name made lowercase.
    invoice_subtotal = models.DecimalField(db_column='INVOICE_SUBTOTAL', max_digits=12, decimal_places=2)  # Field name made lowercase.
    invoiceid = models.IntegerField(db_column='INVOICEID')  # Field name made lowercase.
    notes = models.TextField(db_column='NOTES')  # Field name made lowercase.
    crew_number = models.IntegerField(db_column='CREW_NUMBER')  # Field name made lowercase.
    crew_name = models.TextField(db_column='CREW_NAME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fullinstall'


class FullinstallEquipment(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    fullinstall_id = models.IntegerField(db_column='FULLINSTALL_ID')  # Field name made lowercase.
    equipment = models.TextField(db_column='EQUIPMENT')  # Field name made lowercase.
    archived = models.IntegerField(db_column='ARCHIVED')  # Field name made lowercase.
    cost = models.DecimalField(db_column='COST', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fullinstall_equipment'


class FullinstallItems(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    fullinstall_id = models.IntegerField(db_column='FULLINSTALL_ID')  # Field name made lowercase.
    customer_item_id = models.IntegerField(db_column='CUSTOMER_ITEM_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fullinstall_items'


class Invoice(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    full_invoice_number = models.CharField(db_column='FULL_INVOICE_NUMBER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    invoice_number_prefix = models.TextField(db_column='INVOICE_NUMBER_PREFIX')  # Field name made lowercase.
    invoice_type = models.TextField(db_column='INVOICE_TYPE')  # Field name made lowercase.
    created_timestamp = models.IntegerField(db_column='CREATED_TIMESTAMP')  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=12, decimal_places=2)  # Field name made lowercase.
    total_paid = models.DecimalField(db_column='TOTAL_PAID', max_digits=12, decimal_places=2)  # Field name made lowercase.
    balance_due = models.DecimalField(db_column='BALANCE_DUE', max_digits=12, decimal_places=2)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoice'


class InvoiceLineItems(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    invoiceid = models.IntegerField(db_column='INVOICEID')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION')  # Field name made lowercase.
    amount = models.DecimalField(db_column='AMOUNT', max_digits=12, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoice_line_items'


class InvoicePayments(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    invoiceid = models.IntegerField(db_column='INVOICEID')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION')  # Field name made lowercase.
    amount = models.DecimalField(db_column='AMOUNT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='TIMESTAMP')  # Field name made lowercase.
    type = models.TextField(db_column='TYPE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoice_payments'


class Job(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    starting_date = models.DateField(db_column='STARTING_DATE')  # Field name made lowercase.
    scope_of_work = models.TextField(db_column='SCOPE_OF_WORK')  # Field name made lowercase.
    projected_completion = models.DateField(db_column='PROJECTED_COMPLETION')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'job'


class Pickup(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    pickup_date = models.DateField(db_column='PICKUP_DATE')  # Field name made lowercase.
    pickup_time = models.TextField(db_column='PICKUP_TIME')  # Field name made lowercase.
    pickup_location = models.TextField(db_column='PICKUP_LOCATION')  # Field name made lowercase.
    pickup_item = models.TextField(db_column='PICKUP_ITEM')  # Field name made lowercase.
    crew_number = models.IntegerField(db_column='CREW_NUMBER')  # Field name made lowercase.
    crew_name = models.TextField(db_column='CREW_NAME')  # Field name made lowercase.
    create_date = models.IntegerField(db_column='CREATE_DATE')  # Field name made lowercase.
    archived = models.IntegerField(db_column='ARCHIVED')  # Field name made lowercase.
    completed_flag = models.IntegerField(db_column='COMPLETED_FLAG')  # Field name made lowercase.
    completed_timestamp = models.IntegerField(db_column='COMPLETED_TIMESTAMP')  # Field name made lowercase.
    completed_billtype = models.TextField(db_column='COMPLETED_BILLTYPE')  # Field name made lowercase.
    invoice_hours = models.DecimalField(db_column='INVOICE_HOURS', max_digits=6, decimal_places=2)  # Field name made lowercase.
    invoice_hourly_rate = models.DecimalField(db_column='INVOICE_HOURLY_RATE', max_digits=10, decimal_places=2)  # Field name made lowercase.
    invoice_flat_rate = models.DecimalField(db_column='INVOICE_FLAT_RATE', max_digits=12, decimal_places=2)  # Field name made lowercase.
    invoice_subtotal = models.DecimalField(db_column='INVOICE_SUBTOTAL', max_digits=12, decimal_places=2)  # Field name made lowercase.
    invoiceid = models.IntegerField(db_column='INVOICEID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pickup'


class PickupDropoff(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    pickup_date = models.DateField(db_column='PICKUP_DATE')  # Field name made lowercase.
    pickup_time = models.TextField(db_column='PICKUP_TIME')  # Field name made lowercase.
    pickup_location = models.TextField(db_column='PICKUP_LOCATION')  # Field name made lowercase.
    pickup_item = models.TextField(db_column='PICKUP_ITEM')  # Field name made lowercase.
    dropoff_location = models.TextField(db_column='DROPOFF_LOCATION')  # Field name made lowercase.
    crew_number = models.IntegerField(db_column='CREW_NUMBER')  # Field name made lowercase.
    crew_name = models.TextField(db_column='CREW_NAME')  # Field name made lowercase.
    create_date = models.IntegerField(db_column='CREATE_DATE')  # Field name made lowercase.
    archived = models.IntegerField(db_column='ARCHIVED')  # Field name made lowercase.
    completed_flag = models.IntegerField(db_column='COMPLETED_FLAG')  # Field name made lowercase.
    completed_timestamp = models.IntegerField(db_column='COMPLETED_TIMESTAMP')  # Field name made lowercase.
    completed_billtype = models.TextField(db_column='COMPLETED_BILLTYPE')  # Field name made lowercase.
    invoice_hours = models.DecimalField(db_column='INVOICE_HOURS', max_digits=6, decimal_places=2)  # Field name made lowercase.
    invoice_hourly_rate = models.DecimalField(db_column='INVOICE_HOURLY_RATE', max_digits=10, decimal_places=2)  # Field name made lowercase.
    invoice_flat_rate = models.DecimalField(db_column='INVOICE_FLAT_RATE', max_digits=12, decimal_places=2)  # Field name made lowercase.
    invoice_subtotal = models.DecimalField(db_column='INVOICE_SUBTOTAL', max_digits=12, decimal_places=2)  # Field name made lowercase.
    invoiceid = models.IntegerField(db_column='INVOICEID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pickup_dropoff'


class PickupDropoffEquipment(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    pickup_dropoff_id = models.IntegerField(db_column='PICKUP_DROPOFF_ID')  # Field name made lowercase.
    equipment = models.TextField(db_column='EQUIPMENT')  # Field name made lowercase.
    archived = models.IntegerField(db_column='ARCHIVED')  # Field name made lowercase.
    cost = models.DecimalField(db_column='COST', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pickup_dropoff_equipment'


class PickupEquipment(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    pickup_id = models.IntegerField(db_column='PICKUP_ID')  # Field name made lowercase.
    equipment = models.TextField(db_column='EQUIPMENT')  # Field name made lowercase.
    archived = models.IntegerField(db_column='ARCHIVED')  # Field name made lowercase.
    cost = models.DecimalField(db_column='COST', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pickup_equipment'


class Receiving(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    receiving_date = models.DateField(db_column='RECEIVING_DATE')  # Field name made lowercase.
    receiving_time = models.TextField(db_column='RECEIVING_TIME')  # Field name made lowercase.
    receiving_item = models.TextField(db_column='RECEIVING_ITEM')  # Field name made lowercase.
    crew_number = models.IntegerField(db_column='CREW_NUMBER')  # Field name made lowercase.
    crew_name = models.TextField(db_column='CREW_NAME')  # Field name made lowercase.
    create_date = models.IntegerField(db_column='CREATE_DATE')  # Field name made lowercase.
    archived = models.IntegerField(db_column='ARCHIVED')  # Field name made lowercase.
    completed_flag = models.IntegerField(db_column='COMPLETED_FLAG')  # Field name made lowercase.
    completed_timestamp = models.IntegerField(db_column='COMPLETED_TIMESTAMP')  # Field name made lowercase.
    completed_billtype = models.TextField(db_column='COMPLETED_BILLTYPE')  # Field name made lowercase.
    invoice_hours = models.DecimalField(db_column='INVOICE_HOURS', max_digits=6, decimal_places=2)  # Field name made lowercase.
    invoice_hourly_rate = models.DecimalField(db_column='INVOICE_HOURLY_RATE', max_digits=10, decimal_places=2)  # Field name made lowercase.
    invoice_flat_rate = models.DecimalField(db_column='INVOICE_FLAT_RATE', max_digits=12, decimal_places=2)  # Field name made lowercase.
    invoice_subtotal = models.DecimalField(db_column='INVOICE_SUBTOTAL', max_digits=12, decimal_places=2)  # Field name made lowercase.
    invoiceid = models.IntegerField(db_column='INVOICEID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'receiving'


class ReceivingEquipment(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customerid = models.IntegerField(db_column='CUSTOMERID')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='CLIENTID')  # Field name made lowercase.
    receiving_id = models.IntegerField(db_column='RECEIVING_ID')  # Field name made lowercase.
    equipment = models.TextField(db_column='EQUIPMENT')  # Field name made lowercase.
    archived = models.IntegerField(db_column='ARCHIVED')  # Field name made lowercase.
    cost = models.DecimalField(db_column='COST', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'receiving_equipment'


class User(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    email = models.TextField(db_column='EMAIL')  # Field name made lowercase.
    password = models.TextField(db_column='PASSWORD')  # Field name made lowercase.
    fname = models.TextField(db_column='FNAME')  # Field name made lowercase.
    lname = models.TextField(db_column='LNAME')  # Field name made lowercase.
    create_time = models.IntegerField(db_column='CREATE_TIME')  # Field name made lowercase.
    pin = models.IntegerField(db_column='PIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class WhiteboardEntry(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    objectid = models.CharField(db_column='OBJECTID', max_length=40)  # Field name made lowercase.
    notes = models.TextField(db_column='NOTES')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'whiteboard_entry'


class ZebraSessionData(models.Model):
    session_id = models.CharField(max_length=32)
    hash = models.CharField(max_length=32)
    session_data = models.TextField()
    session_expire = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zebra_session_data'


# Create your models here.
