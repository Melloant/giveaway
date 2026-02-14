import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'giveaway_project.settings')
django.setup()

from datetime import timedelta
from django.utils import timezone
from giveaways.models import Ad

now = timezone.now()

ads = [
    Ad(title='Cliente A — Promoção', sponsor='Cliente A', position=1, active=True, start=now, end=now + timedelta(days=30), target_url='https://example.com/cliente-a'),
    Ad(title='Cliente B — Desconto', sponsor='Cliente B', position=2, active=True, start=now, end=now + timedelta(days=30), target_url='https://example.com/cliente-b'),
    Ad(title='Cliente C — Brinde', sponsor='Cliente C', position=3, active=True, start=now, end=now + timedelta(days=30), target_url='https://example.com/cliente-c'),
    Ad(title='Cliente D — Evento', sponsor='Cliente D', position=4, active=True, start=now, end=now + timedelta(days=30), target_url='https://example.com/cliente-d'),
]

for a in ads:
    a.save()
    print(f'✓ Criado: {a.title} (pos {a.position})')

print('\nAnúncios de exemplo adicionados.')