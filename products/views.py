from django.shortcuts import render
from products.models import Controle

def img_view(request):
    controles = Controle.objects.all()
    print(controles)

    return render(
        request,
        # 'control.html',
        'teste.html',
        {'control': controles}
        )