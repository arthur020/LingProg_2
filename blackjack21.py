import  random

# Metodos
class carta:
    manilha =""
    valor=0
    index=0
    def __init__(self,manilha,valor,index):
        self.manilha = manilha
        self.valor = valor
        self.index= index

    def __str__(self):
        return f"manilha {self.manilha} : valor {self.valor}"


def card_deck():
    card_value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    card_type = ['Coraçao','Espadinha','Zap','Picafumo']
    deck = []
    k  = 0
    for i in card_type:
        for j in card_value:
            k+=1
            cartas = carta(i,j,k)
            deck.append(cartas)
    return deck


def carta_valor(carta,rodada):
    if((carta.valor =='10')or (carta.valor =='J')or(carta.valor =='Q')or(carta.valor =='K')):
        return 10
    elif(carta.valor=='A'):
        if(rodada==1):
            return 11
        else:
            return 1
    else:
        return int(carta.valor)




def cartas_ini(deck):
    return  random.sample(deck,2)

def carta_add(deck):
    carta= random.sample(deck,1)
    remove_from_deck(carta[0],deck)
    print(carta)
    return carta[0]

def mao_atual(mao,soma):
    for carta in mao:
        print(carta)
    print(f"Soma das cartas {soma}")


def remove_from_deck(carta,deck):
    deck.pop(int(carta.index))





def pricipal():
    deck = card_deck()
    print(len(deck))

    mao = cartas_ini(deck)
    soma =  0
    rodada = 1
    while soma<21:
        if rodada ==1:
            for cartas in mao:
                remove_from_deck(cartas,deck)
                soma+= carta_valor(cartas,1)
                print(soma)
        else:
            cont = input("Deseja continuar o jogo ?(S/N)\n")
            if cont.upper() =="S":
                carta =carta_add(deck)
                mao.append(carta)
                soma+= carta_valor(carta,2)

                pass
            else:
                break





        mao_atual(mao,soma)

        rodada+=1
    # print(len(deck))

    if soma==21:
        print("Vc Ganhou")
    elif soma>21:
        print("vc Perdeu")
    else:
        print("Quase La Amigao")




# Main prog

#
# deck = card_deck()
#
#
# mao = cartas_ini(deck)
#
#
#
# for i in mao:
#     print(i)

pricipal()