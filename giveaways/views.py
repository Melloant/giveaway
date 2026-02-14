from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Gift, Participant, Registration, Ad
from .forms import RegistrationForm


def gift_list(request):
    now = timezone.now()
    gifts = Gift.objects.filter(active=True, start__lte=now, end__gte=now).order_by('start')
    # preencher 8 slots de anúncio (posições 1..8: 1-4 esquerda, 5-8 direita)
    ads_qs = Ad.objects.filter(active=True).order_by('position')
    ads_by_pos = {ad.position: ad for ad in ads_qs}
    ad_slots_left = [ads_by_pos.get(i) for i in range(1, 5)]
    ad_slots_right = [ads_by_pos.get(i) for i in range(5, 9)]
    return render(request, 'giveaways/gift_list.html', {
        'gifts': gifts, 
        'ad_slots_left': ad_slots_left, 
        'ad_slots_right': ad_slots_right
    })


def gift_detail(request, pk):
    gift = get_object_or_404(Gift, pk=pk)
    return render(request, 'giveaways/gift_detail.html', {'gift': gift})


def register(request, pk):
    gift = get_object_or_404(Gift, pk=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            already = form.cleaned_data['already_registered']
            if already:
                participant = Participant.objects.get(phone=phone)
            else:
                participant, created = Participant.objects.get_or_create(
                    phone=phone,
                    defaults={
                        'name': form.cleaned_data['name'],
                        'email': form.cleaned_data['email'],
                        'municipio': form.cleaned_data['municipio'],
                    }
                )
            Registration.objects.get_or_create(participant=participant, gift=gift)
            return redirect('giveaways:success')
    else:
        form = RegistrationForm()
    return render(request, 'giveaways/register.html', {'gift': gift, 'form': form})


def success(request):
    return render(request, 'giveaways/success.html')
