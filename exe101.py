from datetime import datetime


def voto(ano):
    """
    """
    idade = datetime.now().year - ano
    if idade < 16:
        print("Você ainda não pode votar.")
    elif 16 <= idade <18 or idade > 65:
        print("Você vota se quiser")
    elif 65 > idade >= 18:
        print("Você é obriado a votar.")
    
    
        


ano_nasc = int(input("Em que ano vocẽ nasceu? "))
voto(ano_nasc)