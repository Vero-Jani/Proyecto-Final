from django.db import models

class Circuito(models.Model):
    idcircuito = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    codcircuito = models.IntegerField(blank=True, null=True)
    nrocircuito = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    distrito_id_distrito = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'circuito'


class Dependencia(models.Model):
    id_dependencia = models.IntegerField(primary_key=True)
    nro_distrito = models.IntegerField(blank=True, null=True)
    parroquia = models.CharField(max_length=50, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dependencia'

class Distrito(models.Model):
    id_distrito = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    nrodistrito = models.IntegerField(blank=True, null=True)
    parroquia = models.CharField(max_length=75, blank=True, null=True)
    provincia = models.CharField(max_length=75, blank=True, null=True)
    cod_distrito = models.IntegerField(blank=True, null=True)
    dependencia_id_dependencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'distrito'

class Informe(models.Model):
    id_informe = models.IntegerField(primary_key=True)
    asociar = models.CharField(max_length=100, blank=True, null=True)
    registrar = models.CharField(max_length=100, blank=True, null=True)
    imprimir_informe = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'informe'


class Mantenimiento(models.Model):
    idmantenimiento = models.IntegerField(primary_key=True)
    codmantenimiento = models.CharField(max_length=50, blank=True, null=True)
    vehiculoasociado = models.CharField(max_length=75, blank=True, null=True)
    fechaingreso = models.DateField(blank=True, null=True)
    tipo_mantenimiento = models.CharField(max_length=100, blank=True, null=True)
    vehiculo_idvehiculo = models.IntegerField()
    informe_idinformar = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mantenimiento'


from django.db import models

class Personal(models.Model):
    id = models.CharField(max_length=45,primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    telefono = models.CharField(max_length=45, blank=True, null=True)
    ciudad = models.CharField(max_length=45, blank=True, null=True)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)
    rango = models.CharField(max_length=45, blank=True, null=True)
    dependencia = models.CharField(max_length=45, blank=True, null=True)
    subcircuito_idsubcircuito = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'personal'
        default_related_name = 'personales'


class ReclamoSugerencia(models.Model):
    id=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
    circuito = models.CharField(max_length=55, blank=True, null=True)
    subcircuito = models.CharField(max_length=55, blank=True, null=True)
    reclamo_sugerencia = models.CharField(max_length=150, blank=True, null=True)
    detalle = models.CharField(max_length=300, blank=True, null=True)
    contacto = models.IntegerField(blank=True, null=True)
    apellidos = models.CharField(max_length=45, blank=True, null=True)
    nombres = models.CharField(max_length=45, blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'reclamo_sugerencia'

class Rol(models.Model):
    idrol = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    tiporol = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class Solicitud(models.Model):
    idsolicitud = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=45, blank=True, null=True)
    fecha_solicitud = models.DateField(blank=True, null=True)
    vehiculo_asociado = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitud'


class Subcircuito(models.Model):
    id_subcircuito = models.IntegerField(primary_key=True)
    nombresubcircuito = models.CharField(max_length=100, blank=True, null=True)
    nrosubcircuito = models.IntegerField(blank=True, null=True)
    codsubcircuito = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    circuito_idcircuto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subcircuito'


class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    correo = models.CharField(max_length=150, blank=True, null=True)
    contrasena = models.CharField(max_length=150, blank=True, null=True)
    rol_idrol = models.IntegerField()
    personal_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'


class Vehiculo(models.Model):
    idvehiculo = models.IntegerField(primary_key=True)
    modelo = models.CharField(max_length=45, blank=True, null=True)
    marca = models.CharField(max_length=45, blank=True, null=True)
    motor = models.CharField(max_length=45, blank=True, null=True)
    chasis = models.CharField(max_length=45, blank=True, null=True)
    cilindraje = models.CharField(max_length=45, blank=True, null=True)
    kilometraje = models.CharField(max_length=45, blank=True, null=True)
    placa = models.CharField(max_length=45, blank=True, null=True)
    tipovehiculo = models.CharField(max_length=150, blank=True, null=True)
    circuito_idcircuito = models.IntegerField()
    solicitud_idsolicitud = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vehiculo'

