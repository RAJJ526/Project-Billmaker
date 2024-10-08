from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gen_pdf(request):
    if request.method=='POST':
        name=request.POST['name']
        mobile_no=request.POST['mobile_no']
        coke=request.POST['coke']
        pepsi=request.POST['pepsi']
        fanta=request.POST['fanta']
        sprite=request.POST['sprite']
        dt=request.POST['dt']
        
        if int(coke)<0 or int(sprite)<0 or int(pepsi)<0 or int(fanta)<0:
            return HttpResponse('<h1>quantity cannot be negative</h1>')
        coke_rt=100
        pepsi_rt=80
        fanta_rt=70
        sprite_rt=50
        total=(int(coke)*coke_rt+int(pepsi)*pepsi_rt+int(sprite)*sprite_rt+int(fanta)*fanta_rt)
        return render(request, 'pdf.html', {'coke':coke, 'pepsi':pepsi, 'fanta':fanta,'sprite':sprite,'dt':dt,'total':total, 'name':name, 'mobile_no':mobile_no})
       

    return render(request, 'index.html')