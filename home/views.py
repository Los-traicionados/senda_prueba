from django.shortcuts import render, get_object_or_404
from booking.models import *

# Create your views here.
def index(request):
    packs = Pack.objects.all()
    vuelos = Vuelo.objects.all()
    hoteles = Hotel.objects.all()
    actividades = Actividad.objects.all()
    # Mostrar los tipos de actividades siempre que tengan una actividad
    tipo_actividades = TipoActividad.objects.filter(actividad__isnull=False).distinct()
    # para controlar ciudades duplicadas
    ciudades = []
    for ho in hoteles:
        if not ho.ho_ciudad in ciudades:
            ciudades.append(ho.ho_ciudad)

    # para controlar origen duplicadas
    origen = []
    for vu in vuelos:
        if not vu.vu_origen in origen:
            origen.append(vu.vu_origen)

    # para controlar origen duplicadas
    destino = []
    for vu in vuelos:
        if not vu.vu_destino in destino:
            destino.append(vu.vu_destino)
    print('fecha_ida', request.session.get('fecha_ida'))
    print('fecha_vuelta', request.session.get('fecha_vuelta'))
    return render(request, 'paginas/index.html',{
        'packs':packs,
        'vuelos':vuelos,
        'hoteles':hoteles,
        'actividades':actividades,
        'tipo_actividades': tipo_actividades,
        'ciudades':ciudades,
        'origen':origen,
        'destino':destino,

    })

def about(request):
    return render(request, 'paginas/about.html')

def productos(request):
    vuelos = Vuelo.objects.all()
    actividades = Actividad.objects.all()
    hoteles = Hotel.objects.all()
    packs = Pack.objects.all()
    return render(request, 'paginas/productos.html',{
        'vuelos': vuelos,
        'actividades': actividades,
        'hoteles': hoteles,
        'packs': packs,
    })

def producto_tipo(request):
    return render(request, 'paginas/producto_tipo.html')

def dashboard(request):
    return render(request, 'paginas/dashboard.html')

def products_detail(request):
	return render(request, 'paginas/products_detail.html')

def redirect_detail_actividades(request, id):
    actividad = get_object_or_404(Actividad, pk=id)
    return render(request, 'paginas/products_detail_actividades.html', {'actividad': actividad})

def redirect_detail_hoteles(request, id):
    hotel = get_object_or_404(Hotel, pk=id)
    return render(request, 'paginas/products_detail_hoteles.html', {'hotel': hotel})

def redirect_detail_vuelos(request, id):
    vuelo = get_object_or_404(Vuelo, pk=id)
    return render(request, 'paginas/products_detail_vuelos.html', {'vuelo': vuelo})

def redirect_detail_packs(request, id):
    pack = get_object_or_404(Pack, pk=id)
    return render(request, 'paginas/products_detail_packs.html', {'pack': pack})