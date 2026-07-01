print('CETAM-CENTRO DE EDUCAÇÃO TECNOLÓGIGA DO AMAZONAS')
print('CURSO:DESENVOLVIMENTO DE SISTEMA')
print('COMPONENTE: LINGUAGEM DE PROGRAMAÇÃO')
print('DATA:22/08/2025')
print('PROFESSOR:MICHALES CAMURÇA')
print('ALUNO: JOSÉ LUIZ SOUZA')
print('ATIVIDADE: Pergunte se o usuário tem senha correta e login correto (ambos precisamser verdadeiros)')

login_correto = 'admin' 
senha_correta = '1234' 
login = input('Digite o login: ') 
senha = input('Digite a senha: ') 
if login == login_correto and senha == senha_correta: 
    print('Acesso permitido!') 
else: print('Acesso negado!')
