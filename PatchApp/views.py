from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.password_validation import validate_password, ValidationError


class NovaConta(TemplateView):
    template_name = 'nova_conta.html'

    def post(self, request):
        nome_usuario = request.POST['nome_usuario']
        email = request.POST['campo_email']
        senha = request.POST['campo_senha']
        try:
            existe_email = User.objects.get(email=email)
            existe_usuario = User.objects.get(username=nome_usuario)
            if existe_email or existe_usuario:
                return render(request, 'nova_conta.html',
                              {'msg': 'Já existe um usuário com o mesmo e-mail ou mesmo username!'})
        except User.DoesNotExist:
            try:
                validate_password(senha)
                novo_usuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
                novo_usuario.save()
                return redirect('tela_inicial')
            except ValidationError:
                return render(request, 'nova_conta.html',
                              {'msg_senha': 'Senha invalida, certifique-se que a senha cumpra todos os requisitos!'})
