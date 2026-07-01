import time

def limpar_tela():
    """Função para limpar o console (funciona na maioria dos terminais)."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_mensagem_especial(nome_esposa):
    """Exibe uma mensagem especial e uma arte em ASCII."""
    limpar_tela()
    mensagem = f"Olá {nome_esposa}, a mulher mais incrível do mundo!"
    print(mensagem)
    print("\nEu sei que é um jeito 'nerd' de dizer, mas...")
    time.sleep(3) # Uma pausa para criar um suspense

    print("\nEu te amo!\n")
    
    # Arte em ASCII de um coração
    print("        ooooo   ooooo        ")
    print("      o       o       o      ")
    print("     o                 o     ")
    print("     o                 o     ")
    print("      o               o      ")
    print("        o           o        ")
    print("          o       o          ")
    print("            o   o            ")
    print("              o              ")

    print(f"\nCom amor, José Luiz.")


nome = input("Qual é o seu nome? ").strip().title()

# Coloque o nome da sua esposa aqui
if nome == "Sophia":
    mostrar_mensagem_especial(nome)
else:
    print(f"Olá {nome}, prazer em conhecer você!")
