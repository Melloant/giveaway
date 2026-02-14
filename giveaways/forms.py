from django import forms


class RegistrationForm(forms.Form):
    already_registered = forms.BooleanField(required=False)
    phone = forms.CharField(max_length=20)
    name = forms.CharField(max_length=200, required=False)
    email = forms.EmailField(required=False)
    municipio = forms.CharField(max_length=100, required=False)

    def clean(self):
        cleaned = super().clean()
        already = cleaned.get('already_registered')
        phone = cleaned.get('phone')
        if not phone:
            raise forms.ValidationError('Telefone é obrigatório.')

        if already:
            # usuário diz que já possui cadastro — telefone deve existir
            from .models import Participant

            try:
                Participant.objects.get(phone=phone)
            except Participant.DoesNotExist:
                raise forms.ValidationError('Telefone não encontrado — cadastre-se primeiro.')
        else:
            # novo usuário precisa de nome, email e município
            if not cleaned.get('name') or not cleaned.get('email') or not cleaned.get('municipio'):
                raise forms.ValidationError('Preencha nome, email e município para se cadastrar.')

        return cleaned
