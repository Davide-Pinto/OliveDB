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


class Camiao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    matricula = models.CharField(db_column='Matricula', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'camiao'

class Test(models.model):
    name = model.CharField(max_length=255)

class Cliente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    morada = models.CharField(db_column='Morada', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contacto = models.CharField(db_column='Contacto', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cliente'

class Despesa(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    camiaoid = models.ForeignKey(Camiao, models.DO_NOTHING, db_column='CamiaoID', blank=True, null=True)  # Field name made lowercase.
    tipodespesaid = models.ForeignKey('Tipodespesa', models.DO_NOTHING, db_column='TipoDespesaID')  # Field name made lowercase.
    valor = models.FloatField(db_column='Valor')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'despesa'


class Distribuicaoazeite(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    estadoid = models.ForeignKey('Estado', models.DO_NOTHING, db_column='EstadoID', blank=True, null=True)  # Field name made lowercase.
    clienteid = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='ClienteID')  # Field name made lowercase.
    azeitetotal = models.FloatField(db_column='Azeitetotal', blank=True, null=True)  # Field name made lowercase.
    azeiteentregue = models.FloatField(db_column='Azeiteentregue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'distribuicaoazeite'


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


class Estado(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'estado'


class Lagar(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=255, blank=True, null=True)  # Field name made lowercase.
    morada = models.CharField(db_column='Morada', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contacto = models.CharField(db_column='Contacto', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lagar'


class Producaoazeite(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    lagarid = models.ForeignKey(Lagar, models.DO_NOTHING, db_column='LagarID')  # Field name made lowercase.
    dataproducao = models.DateField(db_column='DataProducao', blank=True, null=True)  # Field name made lowercase.
    azeiteproduzido = models.FloatField(db_column='AzeiteProduzido', blank=True, null=True)  # Field name made lowercase.
    conv = models.FloatField(db_column='Conv')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producaoazeite'


class Recolhaazeitona(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    distribuicaoazeiteid = models.ForeignKey(Distribuicaoazeite, models.DO_NOTHING, db_column='DistribuicaoAzeiteID')  # Field name made lowercase.
    transporteazeitonaid = models.ForeignKey('Transporteazeitona', models.DO_NOTHING, db_column='TransporteAzeitonaID')  # Field name made lowercase.
    clienteid = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='ClienteID')  # Field name made lowercase.
    quantidadeazeitona = models.FloatField(db_column='QuantidadeAzeitona', blank=True, null=True)  # Field name made lowercase.
    datarecolha = models.DateField(db_column='DataRecolha', blank=True, null=True)  # Field name made lowercase.
    conv = models.FloatField(db_column='Conv')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'recolhaazeitona'


class Tipodespesa(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipodespesa'


class Transporteazeitona(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    camiaoid = models.ForeignKey(Camiao, models.DO_NOTHING, db_column='CamiaoID', blank=True, null=True)  # Field name made lowercase.
    lagarid = models.ForeignKey(Lagar, models.DO_NOTHING, db_column='LagarID')  # Field name made lowercase.
    datatransporte = models.DateField(db_column='DataTransporte', blank=True, null=True)  # Field name made lowercase.
    quantidade = models.FloatField(db_column='Quantidade', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transporteazeitona'

# Create your models here.
