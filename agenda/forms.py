from django import forms
from django.contrib.auth.models import User

from agenda.models import Cliente, Sala


class EditarPerfilForm(forms.Form):

    nome = forms.CharField(required=True)
    profissao = forms.CharField(required=True)
    telefone = forms.CharField(required=True)

    def is_valid_from_form(self):
        return super(EditarPerfilForm, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        if not super(EditarPerfilForm, self).is_valid():
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            valid = False
        return valid

class RemarcarForm(forms.Form):

    data = forms.DateField(required=True)
    horario = forms.TimeField(required=True)

    def is_valid_from_form(self):
        return super(RemarcarForm, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        if not super(RemarcarForm, self).is_valid():
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            valid = False
        return valid

class AdicionarProfissionalForm(forms.Form):

    username = forms.CharField(required=True)

    def is_valid_from_form(self):
        return super(AdicionarProfissionalForm, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        if not super(AdicionarProfissionalForm, self).is_valid():
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            valid = False
        user_exists = User.objects.filter(username=self.cleaned_data['username']).exists()
        if not user_exists:
            self.add_error(field=forms.ALL_FIELDS, error='Este usuario não existe.')
            valid = False
        return valid

class AdicionarSalaForm(forms.Form):

    numero = forms.CharField(required=True)
    andar = forms.CharField(required=True)

    def is_valid_from_form(self):
        return super(AdicionarSalaForm, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        if not super(AdicionarSalaForm, self).is_valid():
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            valid = False
        sala_exists = Sala.objects.filter(numero=self.cleaned_data['numero'],
                                          andar=self.cleaned_data['andar']).first()
        if sala_exists:
            if sala_exists.escritorio:
                self.add_error(field=forms.ALL_FIELDS, error='Sala já ocupada.')
                valid = False
        return valid

class MarcarForm(forms.Form):

    data = forms.DateField(required=True)
    horario = forms.TimeField(required=True)
    nome = forms.CharField(required=True, max_length=30)
    profissional = forms.CharField(required=True)
    cpf = forms.CharField(required=True)
    telefone = forms.CharField(required=True)

    def is_valid_from_form(self):
        return super(MarcarForm, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        print(self.cleaned_data)
        if not super(MarcarForm, self).is_valid():
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            valid = False
        return valid

class RegistrarEscritorioForm(forms.Form):
    nome = forms.CharField(required=True)
    servico = forms.CharField(required=True)
    numero = forms.CharField(required=True)
    andar = forms.CharField(required=True)

    def is_valid_from_form(self):
        return super(RegistrarEscritorioForm, self).is_valid()

    def is_valid(self):
        valid = self.is_valid_from_form()
        print(self.cleaned_data)
        if not super(RegistrarEscritorioForm, self).is_valid():
            self.add_error(field=forms.ALL_FIELDS, error='Por favor, verifique os dados informados')
            valid = False

        sala_exists = Sala.objects.filter(numero=self.cleaned_data['numero'],
                                          andar=self.cleaned_data['andar']).first()
        if sala_exists:
            if sala_exists.escritorio:
                self.add_error(field=forms.ALL_FIELDS, error='Sala já ocupada.')
                valid = False
        print(valid)
        return valid
