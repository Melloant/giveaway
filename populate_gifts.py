import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'giveaway_project.settings')
django.setup()

from django.utils import timezone
from datetime import timedelta
from giveaways.models import Gift

now = timezone.now()

gifts = [
    Gift(
        title="Voucher R$ 50 - McDonald's",
        description="Vale de R$ 50 para gastar no McDonald's",
        sponsor="McDonald's",
        start=now,
        end=now + timedelta(days=7),
        pickup_location="Loja Centro - Rua A, 123",
        pickup_time="10:00",
    ),
    Gift(
        title="Passaporte de Cinema",
        description="5 ingressos de cinema",
        sponsor="Cineploy",
        start=now,
        end=now + timedelta(days=14),
        pickup_location="Shopping Downtown",
        pickup_time="14:00",
    ),
    Gift(
        title="Curso de Python Online",
        description="Acesso de 3 meses ao curso Python Completo",
        sponsor="Udemy Brasil",
        start=now,
        end=now + timedelta(days=30),
        pickup_location="Acesso por email",
        pickup_time="00:00",
    ),
]

for gift in gifts:
    gift.save()
    print(f"✓ Criado: {gift.title}")

print("\nBrindes de teste adicionados com sucesso!")
