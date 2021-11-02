from django.shortcuts import render
from reportes.models import Tables, Tables2
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

