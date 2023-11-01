print("bem vindo ao Titanic")
nome= input("informe seu nome, por favor: ")
print("muito bem"+"  "+nome+"  "+"podemos começar")

print("esse é um projeto de simulação, queremos saber se"+"  "+nome+"  "+"sobrevivereia ao titanic")
print("Não me leve a mal, precisamos disso para saber se já começa com alguma vantagem")
sexo= input("Agora me diga seu sexo por favor:  \n")

pontuacao = 0

if sexo == "feminino":
    print("Sua chance começou boa, ganhou 5 pontos.\n")

    print("Bom, vamos continuar.\n")
    print("Agora lhe daremos algumas opções e, de acordo com suas respostas, lhe diremos seu estado.\n")

    print("O navio começou a naufragar. Qual a primeira coisa que você faz?\n")
    print("1. Correr para o convés.")
    print("2. Tentar sair pela saída de emergência.")
    print("3. Ir procurar o capitão.\n")
    choice1 = input("Digite o número da sua escolha: ")

    if choice1 == "1":
        print("Considerando que você é uma mulher, ótima estratégia. +5 pontos.\n")
        pontuacao += 5
    elif choice1 == "2":
        print("Péssima decisão... tudo está enchendo de água. 0 pontos.\n")
        print("Vá para o convés.\n")
    elif choice1 == "3":
        print("Parece que você deu sorte, o capitão está no convés. +2.5 pontos.\n")
        pontuacao += 2.5

    print("Você está correndo pelo convés, mas se depara com uma criança perdida. O que faz?")
    print("1. Ajuda a criança a procurar sua mãe.")
    print("2. Pega a criança no colo e continua seu caminho.")
    print("3. Somente continua seu caminho.")
    choice2 = input("Digite o número da sua escolha: \n")

    if choice2 == "1":
        print("Sua compaixão é admirável, no entanto vocês não a encontram, então você a pega no colo e vão para o convés. +2.5 pontos.\n")
        pontuacao += 2.5
    elif choice2 == "2":
        print("Decisão boa, assim não perde tempo,afinal isos está afundando +5 pontos\n")
        pontuacao +=5
    elif choice2 == "3":
        print("Você tem mais chances de entrar num barco antes se tiver com uma criança. Volte a pegue, 0 pontos\n")
    
    print("bom você está com a criança agora, mas ela não para de chorar pedindo por sua mãe e muitos estão encarando você\n")
    print("O que você faz?")
    print("1.tenta acalma-la dizendo que quando tiverem no convés vão acha-la na fila para os barcos")
    print("2.dá uma bronca nela ameaçando deixa-la sozinha naquele lugar")
    print("3. mente dizendo que ela está aguardando por vocês nos barcos de fuga")
    choice3 = input("Digite o número da sua escolha:  \n")
    if choice3 == "1":
        print("òtima escolha. Assim você a faz parar de chorar e mais ninguém desconfia. +5 pontos\n")
        pontuacao += 5
    elif choice3 == "2":
        print("Funciona, mas a criança agora não confia mais em você, 0 pontos\n")
        pontuacao += 0
    elif choice3 == "3":
        print("Você consegue a acalmar por um tempo, mas quando chegarem ao convés terá problemas, +2.5 pontos\n")
        pontuacao += 2.5
    print("agora vamos para a ultima situação\m")
    print("Vocês chegaram no convés e estão na fila, mas o responsável por elas está perguntando as crianças se aqueles são pais delas mesmo")
    print("o que você faz?")
    print("1.Você conversa com ela baixinho e explica a situação")
    print("2.diz a ela que para encontrar com sua mâe terá que mentir dizendo que você é ela")
    print("3.Somente com um olhar bravo indica o que quer dela")
    choice4 = input("digite o número da sua escolha:  \n")
    if choice4 == "1":
        print("A criança chora bastante no seu ombro, mas aceita, contanto que você prometa não abandonaa-la, + 5 pontos\n")
        print("...")
        print("A criança confirma que você é a mâe dela e vocês conseguem entrar no barco\n")
        pontuacao += 5 
    elif choice4 == "2":
        print("Ela começa a desconfiar de você, mas acaba aceitando por falta de escolhas, +2.5 pontos\n")
        print("...")
        print("Quando entram no barco ela acaba por achar a mãe ali, por sorte você consegue sair impune\n")
        pontuacao += 2.5
    elif choice4 == "3":
        print(" a criança não diz nada, mas não se sente bem com isso, 0 pontos\n")
        print("...")
        print("A criança nega que você é a mâe dela, fazendo assim você ir para o final da fila e ela entrar\n")
    calculo_da_pontuacao = (pontuacao/10)*100
    print(calculo_da_pontuacao)
    if calculo_da_pontuacao <= 25:
      print("você morreria")
    elif calculo_da_pontuacao <= 50:
        print("você pode sobreviver com alguma sorte")
    else: 
        print("suas chances são boas, se quiser tentar entre numa máquina do tempo e vá")
elif sexo == "masculino":
    print("Desculpe, mas o senhor somente ganhou 0 pontos\n")
    print("Bom, vamos continuar.")
    print("Agora lhe daremos algumas opções e, de acordo com suas respostas, lhe diremos seu estado.")

    print("O navio começou a naufragar. Qual a primeira coisa que você faz?/n")
    print("1. Correr para o convés.")
    print("2. Tentar sair pela saída de emergência.")
    print("3. Ir procurar o capitão.")
    choice1 = input("Digite o número da sua escolha:  \n")

    if choice1 == "1":
        print("Considerando que você é uma mulher, ótima estratégia. +5 pontos.\n")
        pontuacao += 5
    elif choice1 == "2":
        print("Péssima decisão... tudo está enchendo de água. 0 pontos.\n")
        print("Vá para o convés.\n")
    elif choice1 == "3":
        print("Parece que você deu sorte, o capitão está no convés. +2.5 pontos.\n")
        pontuacao += 2.5

    print("Você está correndo pelo convés, mas se depara com uma criança perdida. O que faz?")
    print("1. Ajuda a criança a procurar seu pai.")
    print("2. Pega a criança no colo e continua seu caminho.")
    print("3. Somente continua seu caminho.")
    choice2 = input("Digite o número da sua escolha:  \n")

    if choice2 == "1":
        print("Sua compaixão é admirável. +5 pontos.\n")
        pontuacao += 5
    elif choice2 == "2":
        print("Decisão boa, ajudrá a criança da mesma forma, +2.5 pontos\n")
        pontuacao +=2.5
    elif choice2 == "3":
        print("Você tem mais chances de entrar num barco antes se tiver com uma criança. Volte a pegue, 0 pontos\n")
    
    print("bom você está com a criança agora, mas ela não para de chorar pedindo por seu pai e muitos estão encarando você\n")
    print("O que você faz?")
    print("1.tenta acalma-la dizendo que quando tiverem no convés vão acha-lo na fila para os barcos")
    print("2.dá uma bronca nela ameaçando deixa-la sozinha naquele lugar")
    print("3. mente dizendo que ela está aguardando por vocês nos barcos de fuga")
    choice3 = input("Digite o número da sua escolha:  \n")
    if choice3 == "1":
        print("òtima escolha. Assim você a faz parar de chorar e mais ninguém desconfia. +5 pontos\n")
        pontuacao += 5
    elif choice3 == "2":
        print("Funciona, mas a criança agora não confia mais em você, 0 pontos\n")
        pontuacao += 0
    elif choice3 == "3":
        print("Você consegue a acalmar por um tempo, mas quando chegarem ao convés terá problemas, +2.5 pontos\n")
        pontuacao += 2.5
    print("agora vamos para a ultima situação")
    print("Vocês chegaram no convés e estão na fila, mas o responsável por elas está perguntando as crianças se aqueles são pais delas mesmo")
    print("o que você faz?")
    print("1.Você conversa com ela baixinho e explica a situação")
    print("2.diz a ela que para encontrar com sua mâe terá que mentir dizendo que você é ela")
    print("3.Somente com um olhar bravo indica o que quer dela")
    choice4 = input("digite o número da sua escolha:  \n")
    if choice4 == "1":
        print("A criança chora bastante no seu ombro, mas aceita, contanto que você prometa não abandonaa-la, + 5 pontos\n")
        print("A criança confirma que você é o pai dela e vocês conseguem entrar no barco\n")
        pontuacao += 5 
    elif choice4 == "2":
        print("Ela começa a desconfiar de você, mas acaba aceitando por falta de escolhas, +2.5 pontos\n")
        print("...")
        print("Quando entram no barco seu pai obviamente não estava ali, então ela começa a chorar, mas você consegue contornar a situação\n")
        pontuacao += 2.5
    elif choice4 == "3":
        print(" a criança não diz nada, mas não se sente bem com isso, 0 pontos")
        print("...")
        print("A criança nega que você é a mâe dela, fazendo assim você ir para o final da fila e ela entrar")
    calculo_da_pontuacao = (pontuacao/10)*100
    print(calculo_da_pontuacao)
    if calculo_da_pontuacao <= 25:
      print("você morreria")
    elif calculo_da_pontuacao <= 50:
        print("você pode sobreviver com alguma sorte")
    else: 
        print("suas chances são boas, se quiser tentar entre numa máquina do tempo e vá")


