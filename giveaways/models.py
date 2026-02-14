from django.db import models


class Participant(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, unique=True)
    municipio = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"


class Gift(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    sponsor = models.CharField(max_length=200, blank=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    pickup_location = models.CharField(max_length=200, blank=True)
    pickup_time = models.TimeField(null=True, blank=True)
    image_url = models.URLField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Registration(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('participant', 'gift')

    def __str__(self):
        return f"{self.participant} -> {self.gift}"


class Ad(models.Model):
    """Espaço de propaganda gerenciável pelo admin. Posicionamento 1..8 (1-4 esq, 5-8 dir)."""
    title = models.CharField(max_length=200)
    image_url = models.URLField(blank=True)
    target_url = models.URLField(blank=True)
    sponsor = models.CharField(max_length=200, blank=True)
    position = models.PositiveSmallIntegerField(
        choices=[(1,'Pos 1 (Esq)'),(2,'Pos 2 (Esq)'),(3,'Pos 3 (Esq)'),(4,'Pos 4 (Esq)'),
                 (5,'Pos 5 (Dir)'),(6,'Pos 6 (Dir)'),(7,'Pos 7 (Dir)'),(8,'Pos 8 (Dir)')], 
        default=1
    )
    active = models.BooleanField(default=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        lado = 'Esq' if self.position <= 4 else 'Dir'
        return f"Ad {self.position} ({lado}): {self.title}"
