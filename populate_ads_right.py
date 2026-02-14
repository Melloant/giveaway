import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'giveaway_project.settings')
django.setup()

from datetime import timedelta
from django.utils import timezone
from giveaways.models import Ad

now = timezone.now()

# Adicionar 4 mais para direita (posições 5-8)
ads = [
    Ad(title='Cliente E — Sorteio', sponsor='Cliente E', position=5, active=True, start=now, end=now + timedelta(days=30), target_url='https://example.com/cliente-e'),
    Ad(title='Cliente F — Flash Sale', sponsor='Cliente F', position=6, active=True, start=now, end=now + timedelta(days=30), target_url='https://example.com/cliente-f'),
    Ad(title='Cliente G — Cashback', sponsor='Cliente G', position=7, active=True, start=now, end=now + timedelta(days=30), target_url='https://example.com/cliente-g'),
    Ad(title='Cliente H — Convite', sponsor='Cliente H', position=8, active=True, start=now, end=now + timedelta(days=30), target_url='https://example.com/cliente-h'),
]

for a in ads:
    a.save()
    lado = 'Esq' if a.position <= 4 else 'Dir'
    print(f'✓ Criado: {a.title} (pos {a.position} - {lado})')

print('\nAnúncios direita adicionados.')
