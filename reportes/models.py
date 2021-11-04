from django.db import models
import psycopg2
# Create your models here.

class Tables(models.Model):
    conn = psycopg2.connect("dbname='datos' user='postgres' host='localhost' password='paco1999'")
    cur = conn.cursor()
    # """SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='public'"""
    cur.execute("SELECT \"username\", \"ip_address\", \"id\", \"attempt_time\" FROM \"axes_accesslog\";")
    rows = cur.fetchall()

class Tables2(models.Model):
    conn = psycopg2.connect("dbname='datos' user='postgres' host='localhost' password='paco1999'")
    cur = conn.cursor()
    # """SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='public'"""
    cur.execute("SELECT \"username\", \"ip_address\", \"id\", \"attempt_time\", \"failures_since_start\" FROM \"axes_accessattempt\";")
    rows = cur.fetchall()

class Tables3(models.Model):
    conn = psycopg2.connect("dbname='datos' user='postgres' host='localhost' password='paco1999'")
    cur = conn.cursor()
    # """SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='public'"""
    cur.execute("SELECT \"nombre\", \"categoria\", \"compañia\", \"precio\", \"inventario_pradera\", \"inventario_roosevelt\" FROM \"ventas_producto\";")
    rows = cur.fetchall()