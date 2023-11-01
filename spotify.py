#projeto de criação da playlist aleatória do spotify 
from random import random,choice, sample

cadastros ={}

def cadastros_novos():
    email = str(input("digite seu email: "))
    senha = input("Digite sua senha: ")
    
    cadastros[email]=senha
    print("cadastros realizado com sucesso")

def verificar_login():
    email=str(input("digite seu cadastro: "))
    senha=(input("digite a senha: "))
    if email in cadastros and cadastros[email] == senha:
        return True
    else:
        return False

cadastros_novos()
if verificar_login():
    print("pode entrar")
    while True:
     print("escolha a playlist que quer tocar")
     taylor_swift=["cruel summer", "lover", "delicate", "shake it off", "style", "ours(tv)", "long live(tv)", "fearless(tv)", ]
     shawn_mendes=["mercy", "the hell are we dying for?", "treat you better", "never alone", "imagination", "senhorita"]
     thomas_day=["come home", "wildflower", "masochist", "the new me"]
    
     playlist_choice= input()
     if playlist_choice.lower() == "taylor_swift":
         print("escolha se quer aleatório ou na ordem comum")
         order_choice=input()
         if order_choice.lower()=="aleatorio":
          print(sample(taylor_swift, 7))
         else:
           print(taylor_swift)
     elif playlist_choice.lower()=="shawn_mendes":
         print("escolha se quer aleatório ou na ordem comum")
         order_choice=input()
         if order_choice.lower() == "aleatorio":
          print(sample(shawn_mendes, 5))
         else:
           print(shawn_mendes)
        
     elif playlist_choice.lower()=="thomas_day":
         print("escolha se quer aleatório ou na ordem comum")
         order_choice=input()
         if order_choice.lower()== "aleatorio":
          print(sample(thomas_day, 3))
         else:
           print(thomas_day)
     else:
       print("playlist não encontrada")
    
     novo= input("Deseja selecionar outra playlist?: ")
     if novo.lower() != "s":
       break
else:
  print("acesso negado")






