
# Tienda Pipi by Mica Lira

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresaEnvioClientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('pagina', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('costoenvio', models.CharField(max_length=60)),
                ('demoraenvio', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='EntregableProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=60)),
                ('empresaenvio', models.CharField(max_length=60)),
                ('fechaEntrega', models.DateField()),
                ('entregado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductosMayorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('valor', models.CharField(max_length=60)),
                ('cantidad', models.CharField(max_length=60)),
                ('tamaño', models.CharField(max_length=60)),
                ('peso', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ProductosMinorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('valor', models.CharField(max_length=60)),
                ('cantidad', models.CharField(max_length=60)),
                ('tamaño', models.CharField(max_length=60)),
                ('peso', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ProveedorMercaderia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('pagina', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('costoenvio', models.CharField(max_length=60)),
                ('demoraenvio', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TiendaMayorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=60)),
                ('dni', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='TiendaMinorista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=60)),
                ('dni', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
