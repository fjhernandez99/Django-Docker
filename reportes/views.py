from django.shortcuts import render
from reportes.models import Tables, Tables2, Tables3, Tables4, Tables5
from django.template import loader
import pdfkit
from django.http import HttpResponse
from .utils import render_to_pdf
# Create your views here.

def pdflogin(request):
    all_tables = Tables.rows
    template = loader.get_template('reportes/reportelogin.html')
    context = {
        'all_tables': all_tables,
    }
    pdf = render_to_pdf('reportes/reportelogin.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

def pdfattempts(request):
    all_tables2 = Tables2.rows
    template = loader.get_template('reportes/reporteattempts.html')
    context = {
        'all_tables2': all_tables2,
    }
    pdf = render_to_pdf('reportes/reporteattempts.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

def pdfinventario(request):
    all_tables3 = Tables3.rows
    template = loader.get_template('reportes/reporteinventario.html')
    context = {
        'all_tables3': all_tables3,
    }
    pdf = render_to_pdf('reportes/reporteinventario.html', context)
    return HttpResponse(pdf, content_type='application/pdf')

def pdfventas(request):
    all_tables4 = Tables4.rows
    all_tables5 = Tables5.rows
    template = loader.get_template('reportes/reporteventas.html')
    context = {
        'all_tables4': all_tables4,
        'all_tables5': all_tables5,
    }
    pdf = render_to_pdf('reportes/reporteventas.html', context)
    return HttpResponse(pdf, content_type='application/pdf')