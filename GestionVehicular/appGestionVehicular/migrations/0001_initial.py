# Generated by Django 5.0 on 2024-01-16 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circuito',
            fields=[
                ('idcircuito', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('codcircuito', models.IntegerField(blank=True, null=True)),
                ('nrocircuito', models.IntegerField(blank=True, null=True)),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
                ('distrito_id_distrito', models.IntegerField()),
            ],
            options={
                'db_table': 'circuito',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id_dependencia', models.IntegerField(primary_key=True, serialize=False)),
                ('nro_distrito', models.IntegerField(blank=True, null=True)),
                ('parroquia', models.CharField(blank=True, max_length=50, null=True)),
                ('provincia', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'dependencia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id_distrito', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('nrodistrito', models.IntegerField(blank=True, null=True)),
                ('parroquia', models.CharField(blank=True, max_length=75, null=True)),
                ('provincia', models.CharField(blank=True, max_length=75, null=True)),
                ('cod_distrito', models.IntegerField(blank=True, null=True)),
                ('dependencia_id_dependencia', models.IntegerField()),
            ],
            options={
                'db_table': 'distrito',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id_informe', models.IntegerField(primary_key=True, serialize=False)),
                ('asociar', models.CharField(blank=True, max_length=100, null=True)),
                ('registrar', models.CharField(blank=True, max_length=100, null=True)),
                ('imprimir_informe', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'informe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('idmantenimiento', models.IntegerField(primary_key=True, serialize=False)),
                ('codmantenimiento', models.CharField(blank=True, max_length=50, null=True)),
                ('vehiculoasociado', models.CharField(blank=True, max_length=75, null=True)),
                ('fechaingreso', models.DateField(blank=True, null=True)),
                ('tipo_mantenimiento', models.CharField(blank=True, max_length=100, null=True)),
                ('vehiculo_idvehiculo', models.IntegerField()),
                ('informe_idinformar', models.IntegerField()),
            ],
            options={
                'db_table': 'mantenimiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('telefono', models.CharField(blank=True, max_length=45, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=45, null=True)),
                ('fecha_de_nacimiento', models.DateField(blank=True, null=True)),
                ('rango', models.CharField(blank=True, max_length=45, null=True)),
                ('dependencia', models.CharField(blank=True, max_length=45, null=True)),
                ('subcircuito_idsubcircuito', models.IntegerField()),
            ],
            options={
                'db_table': 'personal',
                'managed': False,
            },
        ),
       
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('idrol', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('tiporol', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'rol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('idsolicitud', models.IntegerField(primary_key=True, serialize=False)),
                ('estado', models.CharField(blank=True, max_length=45, null=True)),
                ('fecha_solicitud', models.DateField(blank=True, null=True)),
                ('vehiculo_asociado', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'solicitud',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subcircuito',
            fields=[
                ('id_subcircuito', models.IntegerField(primary_key=True, serialize=False)),
                ('nombresubcircuito', models.CharField(blank=True, max_length=100, null=True)),
                ('nrosubcircuito', models.IntegerField(blank=True, null=True)),
                ('codsubcircuito', models.IntegerField(blank=True, null=True)),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
                ('circuito_idcircuto', models.IntegerField()),
            ],
            options={
                'db_table': 'subcircuito',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('correo', models.CharField(blank=True, max_length=150, null=True)),
                ('contrasena', models.CharField(blank=True, max_length=150, null=True)),
                ('rol_idrol', models.IntegerField()),
                ('personal_id', models.IntegerField()),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('idvehiculo', models.IntegerField(primary_key=True, serialize=False)),
                ('modelo', models.CharField(blank=True, max_length=45, null=True)),
                ('marca', models.CharField(blank=True, max_length=45, null=True)),
                ('motor', models.CharField(blank=True, max_length=45, null=True)),
                ('chasis', models.CharField(blank=True, max_length=45, null=True)),
                ('cilindraje', models.CharField(blank=True, max_length=45, null=True)),
                ('kilometraje', models.CharField(blank=True, max_length=45, null=True)),
                ('placa', models.CharField(blank=True, max_length=45, null=True)),
                ('tipovehiculo', models.CharField(blank=True, max_length=150, null=True)),
                ('circuito_idcircuito', models.IntegerField()),
                ('solicitud_idsolicitud', models.IntegerField()),
            ],
            options={
                'db_table': 'vehiculo',
                'managed': False,
            },
        ),
    ]
