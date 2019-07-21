from django.db import models


class Referencia(models.Model):
    ref_id = models.AutoField(primary_key=True)
    ref_ubicacion = models.CharField(max_length=30)
    ref_piso = models.PositiveIntegerField(default=1)
    ref_pabellon = models.CharField(max_length=30)

    def __str__(self):
        return self.ref_ubicacion


class Dependencia(models.Model):
    dpn_codigo = models.CharField(max_length=10, primary_key=True)
    dpn_nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.dpn_codigo


class Encargado(models.Model):
    enc_codigo = models.CharField(max_length=10, primary_key=True)
    enc_dni = models.CharField(max_length=8, unique=True)
    enc_nombres = models.CharField(max_length=30)
    enc_ape_paterno = models.CharField(max_length=30)
    enc_ape_materno = models.CharField(max_length=30)
    dpn_codigo = models.ForeignKey(Dependencia, on_delete=models.CASCADE)

    def __str__(self):
        return self.enc_codigo


class Categoria(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_nombre = models.CharField(max_length=30)
    cat_descripcion = models.TextField()

    def __str__(self):
        return self.cat_nombre

class Programa(models.Model):
    prg_id = models.AutoField(primary_key=True)
    prg_nombre = models.CharField(max_length=30)
    prg_version = models.CharField(max_length=30)
    prg_fabrica_desarr = models.CharField(max_length=30)
    prg_tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.prg_nombre

class Componente(models.Model):
    comp_id = models.AutoField(primary_key=True)
    cat_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    comp_tipo = models.CharField(max_length=30)
    comp_marca = models.CharField(max_length=30)
    comp_modelo = models.CharField(max_length=30)
    comp_descripcion = models.TextField()
    comp_comp_id= models.ForeignKey("self", on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.comp_marca +" " + self.comp_modelo

class Laboratorio(models.Model):
    labo_id = models.AutoField(primary_key=True)
    ref_id = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    enc_codigo = models.ForeignKey(Encargado, on_delete=models.CASCADE)
    labo_capacidadmaquinas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.labo_id)

class LaboratorioProgramas(models.Model):
    labo_id = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    prg_id = models.ForeignKey(Programa, on_delete=models.CASCADE)
    labo_prg_numPC=models.PositiveIntegerField(default=1)
    class Meta(object):
        unique_together = [
            ("labo_id", "prg_id","labo_prg_numPC"),
        ]

class LaboratorioComponente(models.Model):
    labo_id = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    comp_id = models.ForeignKey(Componente, on_delete=models.CASCADE)
    labo_cmp_numSERIE = models.CharField(max_length=10)
    class Meta(object):
        unique_together = [
            ("labo_id", "comp_id","labo_cmp_numSERIE"),
        ]

