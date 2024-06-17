def conta():


    arq = open('conta.txt', 'a')
    print("Vamos criar uma conta!!!!!!")
    email = input ("Digite seu email:")
    senha = input("digite sua senha:")
    arq.write('{},{}\n'.format(email,senha))
    arq.close


def login():
       
    resposta = input("voce é um novo usuario? (sim/nao): ")
    if  resposta.lower () == "sim":
     print ("vamos nos cadastrar...")
     conta()

    else:
     email1 = input('informe seu email:')
     senha1 = input('informe sua senha:')

     with open('conta.txt', 'r') as arq:
            encontrado = False
            for linha in arq:
                email, senha = linha.strip().split(',')
                if email == email1 and senha == senha1:
                    encontrado = True
                    break

    if encontrado:
            print("Login feito com sucesso!")
    else:
            print("Email ou senha incorretos. Tente novamente.")