import time
import random 
from colorama import Fore, Back, Style
def primeira(exp,moedas,fome,sono):
    print()
    time.sleep(0.5)
    print('*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*')
    print('  Você tem [' + Fore.YELLOW + f'{moedas}' + Fore.RESET + '] shycoin(s) nesse momento.')
    print(f'  Você tem [' + Fore.LIGHTGREEN_EX + f'{exp}' + Fore.RESET + '] de experiência nesse momento.')
    if fome == 100:
        print(f'  ShyPy está com a fome em [' + Fore.LIGHTMAGENTA_EX + '100' + Fore.RESET + ']. ShyPy está bem cheio, isso é bom!!')
    elif fome < 100 and fome >= 75:
        print(f'  ShyPy está com a fome em [' + Fore.LIGHTMAGENTA_EX + f'{fome}' + Fore.RESET + ']. Não se preocupe, ShyPy ainda aguenta muitas brincadeiras. :)')
    elif fome < 75 and fome >= 50:
        print(f'  ShyPy está com a fome em [' + Fore.LIGHTMAGENTA_EX +  f'{fome}' + Fore.RESET + ']. Se você quiser dar alguma comida, ShyPy ficará satisfeito em aceitar. :)')
    elif fome < 50 and fome >= 25:
        print(f'  ShyPy está com a fome em [' + Fore.LIGHTMAGENTA_EX + f'{fome}' + Fore.RESET + ']. Sinto que já está na hora de comer, a barriga de ShyPy está roncando.')
    elif fome < 25 and fome >= 1:
        print(f'  ShyPy está com a fome em [' + Fore.LIGHTMAGENTA_EX + f'{fome}' + Fore.RESET +']. Se você não der alguma comida para ShyPy, pode ser que enfraqueça demais, ajude ShyPy.')
    elif fome == 0:
        print(f'  Como você deixou ShyPy ficar totalmente com fome?:( Por favor alimente ShyPy o quanto antes...')
    if sono <= 100 and sono >= 50:
        print(f'  ShyPy está com o sono em [' + Fore.LIGHTBLUE_EX + f'{sono}' + Fore.RESET + ']. Ele só quer brincar, pular e se divertir, então vamos lá!!!')
    elif sono < 50 and sono >= 1:
        print(f'  ShyPy está com o sono em [' + Fore.LIGHTBLUE_EX + f'{sono}' + Fore.RESET + ']. Já vejo alguns bocejos e uma menor energia, você pode colocar ShyPy para dormir se quiser.')
    elif sono == 0:
        print(f'  ShyPy está esgotado, não consegue fazer praticamente nada. Leve Shy para dormir, vai fazer bem. :)')
    print('*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*')
    time.sleep(2.2)
    print()
    print('                             o<><><> Voltando ao início <><><>o')
    print()
    time.sleep(1)
    return hub(exp,moedas,fome,sono)
def segunda(exp,moedas,fome,sono):
    Experiencia = exp
    def S_N(Experiencia,x,fome,sono):
        if x.upper() == 'S':
            print()
            return segunda(Experiencia,moedas,fome,sono)
        elif x.upper() == 'N':
            print('Vamos ao início então')
            time.sleep(0.5)
            return hub(Experiencia,moedas,fome,sono)
        else:
            xE = input('Tá digitando errado não é? Digite [S] para "Sim" e [N] para "Não: ')
            return S_N(Experiencia,xE,fome,sono)

    time.sleep(0.2)
    print()
    print('Opções de comida:')
    print('>>>'*16)
    print()
    print(Fore.CYAN + '      [1] ' + Fore.RESET + 'Chocolate----(restaura ' + Fore.MAGENTA + '+20' + Fore.RESET + ' fome)' + Fore.RESET)
    print()
    print(Fore.CYAN + '      [2] ' + Fore.RESET + 'Saladinha----(restaura ' + Fore.MAGENTA + '+10' + Fore.RESET +  ' fome)' + Fore.RESET)
    print()
    print(Fore.CYAN + '      [3] ' + Fore.RESET + 'Almocinho----(restaura ' + Fore.MAGENTA + '+40' + Fore.RESET + ' fome)' + Fore.RESET)
    print()
    print(Fore.CYAN + '      [4] ' + Fore.RESET + 'Suco---------(restaura ' + Fore.MAGENTA + '+05' + Fore.RESET + ' fome)' + Fore.RESET)
    print()
    print(Fore.CYAN + '      [5] ' + Fore.RESET + 'Macarronada--(restaura ' + Fore.MAGENTA + '+35' + Fore.RESET + ' fome)' + Fore.RESET)
    print()
    print(Fore.CYAN + '      [6] ' + Fore.RESET + 'Pipoca-------(restaura ' + Fore.MAGENTA + '+15' + Fore.RESET + ' fome)' + Fore.RESET)
    print()
    print(Fore.CYAN + '      [7] ' + Fore.RESET + 'Chá----------(restaura ' + Fore.MAGENTA + '+08' + Fore.RESET + ' fome)' + Fore.RESET)
    print()
    print(Fore.CYAN + '      [8] ' + Fore.RESET + 'Balinha------(restaura ' + Fore.MAGENTA + '+01' + Fore.RESET + ' fome)' + Fore.RESET)
    print()
    print('<<<'*16)
    print()
    print(Fore.RED + '  [SAIR] ' + Fore.RESET + 'Se deseja voltar ao início.')
    time.sleep(0.5)
    print()
    comida = input('Qual a opção que deseja?: ')
    print()
    if comida == '1':
        time.sleep(0.2)
        if fome + 20 > 100:
            print()
            time.sleep(0.2)
            print('Ai, acho que estou cheio demais para um chocolate, que tal outra coisa?( ͡◕ ㅅ ͡◕)')
            return segunda(exp,moedas,fome,sono)
        else:
            print('Nossa como eu amo um chocolatinho 0o0 mas cuidado com as diabetes hein?')
            Experiencia += 50
            AFome = fome + 20
            sono -= 2
            print(f'Com esse chocolate você tem {Experiencia} de experiência e agora sua fome está em {AFome}.')
            time.sleep(0.2)
            print()
            x = input('Vai me dar mais?[S/N]: ')
            S_N(Experiencia,x,AFome,sono)
    elif comida == '2':
        time.sleep(0.2)
        if fome + 10 > 100:
            print('Olha... Acho que não quero salada não, melhor outra coisa ( ͡⚈ _⦣ ͡⚈)')
            return segunda(exp,moedas,fome,sono)
        else:
            print('Eu gosto de saladinha, mas não me dê demais, posso ficar verde. Eca!')
            Experiencia += 20
            AFome = fome + 10
            sono -= 2
            print(f'Com essa salada você tem {Experiencia} de experiência e agora sua fome está em {AFome}.')
            time.sleep(0.2)
            print()
            x = input('Vai me dar mais?[S/N]: ')
            S_N(Experiencia,x,AFome,sono)
    elif comida == '3':
        time.sleep(0.2)
        if fome + 40 > 100:
            print('Sinto que um almoco completo é demais pra mim, vamos tentar outra coisa ( ͡◎ ﹏ ͡◎)')
            return segunda(exp,moedas,fome,sono)
        else:
            print('Nossa, comidinha completa, quase fiquei satisfeito, mas sempre cabe mais ;)')
            Experiencia += 110
            AFome = fome + 40
            sono -= 2
            print(f'Com esse almoço completo você tem {Experiencia} de experiência e agora sua fome está em {AFome}.')
            time.sleep(0.2)
            print()
            x = input('Vai me dar mais?[S/N]: ')
            S_N(Experiencia,x,AFome,sono)
    elif comida == '4':
        time.sleep(0.2)
        if fome + 5 > 100:
            print('Mesmo sendo só um suquinho, minha barriga já não quer mais, vamos tentar outra opção ( ͡◒ ㅅ ͡◒)')
            return segunda(exp,moedas,fome,sono)
        else:
            print('É bom um líquido para fazer o resto descer, está muito bom!')
            Experiencia += 15
            AFome = fome + 5
            sono -= 2
            print(f'Com esse suco você tem {Experiencia} de experiência e agora sua fome está em {AFome}.')
            time.sleep(0.2)
            print()
            x = input('Vai me dar mais?[S/N]: ')
            S_N(Experiencia,x,AFome,sono)
    elif comida == '5':
        time.sleep(0.2)
        if fome + 35 > 100:
            print('Ai... Não sei se essa macarronada vai me fazer bem. Vamos tentar uma comida mais leve? ( ` ₃ ´ )')
            return segunda(exp,moedas,fome,sono)
        else:
            print('Pode me trazer um garfo a mais, essa macarronada está deliciosa ( ͡◉ ▿ ͡◉)')
            Experiencia += 80
            AFome = fome + 35
            sono -= 2
            print(f'Com esse macarrão você tem {Experiencia} de experiência e agora sua fome está em {AFome}.')
            time.sleep(0.2)
            print()
            x = input('Vai me dar mais?[S/N]: ')
            S_N(Experiencia,x,AFome,sono)
    elif comida == '6':
        time.sleep(0.2)
        if fome + 15 > 100:
            print('Não sei se estou muito afim de pipoca agora, uma outra coisa seria melhor (ᵔ︣ ▿ ᵔ᷅)')
            return segunda(exp,moedas,fome,sono)
        else:
            print('Pipoquinha com manteiga derrete meu coração (︡> ▿<︠)')
            Experiencia += 40
            AFome = fome + 15
            sono -= 2
            print(f'Com essa pipoca você tem {Experiencia} de experiência e agora sua fome está em {AFome}.')
            time.sleep(0.2)
            print()
            x = input('Vai me dar mais?[S/N]: ')
            S_N(Experiencia,x,AFome,sono)
    elif comida == '7':
        time.sleep(0.2)
        if fome + 8 > 100:
            print('Minha barriga não quer chá... Melhor outra coisa ( ㆆ ェ ㆆ )')
            return segunda(exp,moedas,fome,sono)
        else:
            print('Quentinho e delicioso, amo um cházinho')
            Experiencia += 20
            AFome = fome + 8
            sono -= 2
            print(f'Com esse chá você tem {Experiencia} de experiência e agora sua fome está em {AFome}.')
            time.sleep(0.2)
            print()
            x = input('Vai me dar mais?[S/N]: ')
            S_N(Experiencia,x,AFome,sono)
    elif comida == '8':
        time.sleep(0.2)
        if fome + 1 > 100:
            print('Ah, não estou a fim nem de uma balinha, quer tentar outra coisa? ( ͡o ェ ͡O)')
            return segunda(exp,moedas,fome,sono)
        else:
            print('Hum, uma balinha pra enganar a fome ( ͡♥ ω ͡♥) Qual seu sabor de bala favorito?')
            Experiencia += 5
            AFome = fome + 1
            sono -= 2
            print(f'Com essa balinha maravilhosa você tem {Experiencia} de experiência e agora sua fome está em {AFome}.')
            time.sleep(0.2)
            print()
            x = input('Vai me dar mais?[S/N]: ')
            S_N(Experiencia,x,AFome,sono)
    elif comida.upper() == 'SAIR':
        time.sleep(0.2)
        print()
        print('Okay, voltemos ao início.')
        print()
        sono -= 1
        return hub(exp,moedas,fome,sono)
    else:
        time.sleep(0.2)
        print('Isso nem é comida de verdade, me dê uma opção que exista.')
        print()
        if fome - 1 >= 0:
            DFome = fome - 1
            time.sleep(0.5)
            return segunda(Experiencia,moedas,DFome,sono)
        else:
            time.sleep(0.5)
            return segunda(Experiencia,moedas,fome,sono)
def Balão(Tamanho,moedas,exp,assoprou,fome,sono):
    total = moedas
    def S_N_Balão(escolha,exp,moedas,fome,sono):
        if escolha.upper() == 'S':
            print()
            print('Bem vindo ao --- Sopra - Balão ---')
            print()
            print('-*-'*34)
            print()
            print('''Neste jogo, o seu objetivo é assoprar um balão.(Jura?( ͡❛ ㅅ ͡❛))
        Este balão pode ter um tamanho de 1 até 15. Cada assopro aumenta 1 no tamanho.
        O tamanho é aleatório, e o seu objetivo é assoprar o máximo sem que ele estoure.
        Você pode assoprar o quanto quiser e sair quando quiser, tudo depende da sua sorte.
        Boa sorte, e bom jogo.''')
            print()
            print(f'-*-'*34)
            time.sleep(0.2)
            print()
            time.sleep(0.2)
            tamanho = random.randint(1,15)
            sono -= 5
            return Balão(tamanho,moedas,exp,0,fome,sono)
        elif escolha.upper() == 'N':
            time.sleep(0.2)
            print()
            print('Voltando ao início.')
            time.sleep(0.5)
            return hub(exp,moedas,fome,sono)
        else:
            escolhaC = input('Você quer jogar novamente?[S/N]: ')
            return S_N_Balão(escolhaC,exp,moedas,fome,sono)
    assoprado = assoprou
    assoprar = input('Você quer assoprar?[S/N]: ')
    if assoprar.upper() == 'S':
        assoprado += 1
        if assoprado > Tamanho:
            print('Perdemos. Acho que não ganharemos pontos dessa vez ( ͡❛ Ĺ̯ ͡❛)')
            escolha = input('Você quer jogar novamente?[S/N]: ')
            return S_N_Balão(escolha,exp,moedas,fome,sono)
        elif Tamanho == 15 and assoprado == Tamanho:
            print('Parabéns, você conseguiu alcançar o tamanho máximo!!! Como prêmio, você receberá 100 Shycoins!')
            total += 100
            escolha = input('Você quer jogar novamente?[S/N]: ')
            return S_N_Balão(escolha,exp,total,fome,sono)
        else:
            print(f'O tamanho do balão é {assoprado} nesse momento.')
            return Balão(Tamanho,moedas,exp,assoprado,fome,sono)
    elif assoprar.upper() == 'N':
        print(f'Seus pontos foram {assoprado}, convertido para shycoins você ganhou {assoprado*5}$C,parabéns!!( ͡❛ ω ͡❛)')
        total += assoprado*5
        print(f'O tamanho total do balão era {Tamanho}.')
        sono -= 2
        escolha = input('Você quer jogar novamente?[S/N]: ')
        return S_N_Balão(escolha,exp,total,fome,sono)
    else:
        return Balão(Tamanho,moedas,exp,assoprou,fome,sono)
def Pedra_Papel_Tesoura(moedas,exp,fome,sono,ListaPPT):
    pontos = moedas
    def S_N_PPT(moedas,exp,fome,sono):
        print()
        print('Se você deseja mudar a dificuldade, comece o jogo do zero.')
        print()
        SN = input('Você quer jogar de novo?[' + Fore.GREEN + 'S' + Fore.RESET + '/' + Fore.RED + 'N' + Fore.RESET + ']: ')
        if SN.upper() == 'S':
            return Pedra_Papel_Tesoura(moedas,exp,fome,sono,ListaPPT)
        elif SN.upper() == 'N':
            print()
            print('Tudo bem então, voltaremos ao início.')
            print()
            time.sleep(0.2)
            return hub(exp,moedas,fome,sono)
        else:
            return S_N_PPT(moedas,exp,fome,sono)
    
    PPT = random.choice(ListaPPT)
    print()
    Choice = input('Qual você deseja escolher? PEDRA,PAPEL ou TESOURA?: ')
    print()
    if Choice.upper() == 'PEDRA' and PPT == 'PAPEL':
        print('Pedra...')
        time.sleep(0.5)
        print('Papel...')
        time.sleep(0.5)
        print('E Tesoura!')
        print()
        time.sleep(0.1)
        print('ShyPy escolheu papel, ' + Fore.RED + 'VOCÊ PERDEU' + Fore.RESET + '. Cuidado com os cortes de papel ShyPy, são os piores.')
        print()
        sono -= 2
        return S_N_PPT(moedas,exp,fome,sono)
    elif Choice.upper() == 'PEDRA' and PPT == 'TESOURA':
        print('Pedra...')
        time.sleep(0.5)
        print('Papel...')
        time.sleep(0.5)
        print('E Tesoura!')
        print()
        time.sleep(0.1)
        print('ShyPy escolheu tesoura, ' + Fore.GREEN + 'VOCÊ VENCEU!!! ' + Fore.RESET + 'Que pedrada hein? Haha ( ͡─ ‿‿ ͡─)')
        print()
        print(Fore.LIGHTGREEN_EX + 'Você ganhou oito moedas por essa vitória!' + Fore.RESET)
        print()
        pontos = moedas + 8
        sono -= 3
        return S_N_PPT(pontos,exp,fome,sono)
    elif Choice.upper() == 'PAPEL' and PPT == 'PEDRA':
        print('Pedra...')
        time.sleep(0.5)
        print('Papel...')
        time.sleep(0.5)
        print('E Tesoura!')
        print()
        time.sleep(0.1)
        print('ShyPy escolheu pedra, ' + Fore.GREEN + 'VOCÊ VENCEU!!! ' + Fore.RESET + 'Que papelão hein ShyPy? Haha ( ͡◡ . ͡◡)')
        print()
        print(Fore.LIGHTGREEN_EX + 'Você ganhou oito moedas por essa vitória!' + Fore.RESET)
        print()
        pontos = moedas + 8
        sono -= 3
        return S_N_PPT(pontos,exp,fome,sono)
    elif Choice.upper() == 'PAPEL' and PPT == 'TESOURA':
        print('Pedra...')
        time.sleep(0.5)
        print('Papel...')
        time.sleep(0.5)
        print('E Tesoura!')
        print()
        time.sleep(0.1)
        print('ShyPy escolheu tesoura, ' + Fore.RED + 'VOCÊ PERDEU' + Fore.RESET + '. Espero que a tesoura seja sem ponta ShyPy.')
        print()
        sono -= 2
        return S_N_PPT(moedas,exp,fome,sono)
    elif Choice.upper() == 'TESOURA' and PPT == 'PEDRA':
        print('Pedra...')
        time.sleep(0.5)
        print('Papel...')
        time.sleep(0.5)
        print('E Tesoura!')
        print()
        time.sleep(0.1)
        print('ShyPy escolheu pedra, ' + Fore.RED + 'VOCÊ PERDEU' + Fore.RESET + '. Espero que ShyPy não tenha um estilingue.')
        print()
        sono -= 2
        return S_N_PPT(moedas,exp,fome,sono)
    elif Choice.upper() == 'TESOURA' and PPT == 'PAPEL':
        print('Pedra...')
        time.sleep(0.5)
        print('Papel...')
        time.sleep(0.5)
        print('E Tesoura!')
        print()
        time.sleep(0.1)
        print('ShyPy escolheu papel, ' + Fore.GREEN + 'VOCÊ VENCEU!!! ' + Fore.RESET + 'Você está mesmo afiado. Haha ( ͡≖ ㅅ ͡≖)')
        print()
        print(Fore.LIGHTGREEN_EX + 'Você ganhou oito moedas por essa vitória!' + Fore.RESET)
        print()
        pontos = moedas + 8
        sono -= 3
        return S_N_PPT(pontos,exp,fome,sono)
    elif Choice.upper() == PPT:
        print('Pedra...')
        time.sleep(0.5)
        print('Papel...')
        time.sleep(0.5)
        print('E Tesoura!')
        print()
        print(Fore.MAGENTA + 'Isso foi um empate. Foi só coincidência ou poderes mentais?' + Fore.RESET)
        print()
        sono -= 2
        return S_N_PPT(pontos,exp,fome,sono)
    else:
        print()
        print('Suas escolhas são apenas PEDRA, PAPEL e TESOURA, escolha novamente.')
        print()
        sono -= 1
        return Pedra_Papel_Tesoura(moedas,exp,fome,sono,ListaPPT)
def Vinte_E_Um(moedas,exp,fome,sono,selected,soma):
    def Game_Over(moedas,exp,fome,sono,selected,soma):
        time.sleep(2)
        New = input('Você quer jogar novamente?[S/N]: ').strip()
        if New.upper() == 'S':
            time.sleep(1)
            print('\nTudo bem então, vamos ver se a sorte está do seu lado.\n')
            time.sleep(2)
            return Vinte_E_Um(moedas,exp,fome,sono,selected,soma)
        elif New.upper() == 'N':
            time.sleep(1)
            print('\nEntão voltemos ao início.\n')
            time.sleep(2)
            return hub(exp,moedas,fome,sono)
        else:
            return Game_Over(moedas,exp,fome,sono,selected,soma)
    def Card_Shy():
        Cards_Shy = [10,11,12,13,14,14,15,15,16,16,17,17,18,18,18,18,19,19,19,19,20,20,20,20,21,21,21]
        Points = random.choice(Cards_Shy)
        return Points
    def Yes(moedas,selected,soma,fome,sono):
        count = 0
        Choiced = random.randint(1,13)
        for i in selected:
            if i == Choiced:
                count += 1
        if count == 2:
            return Yes(moedas,selected,soma,fome,sono)
        else:
            if soma + Choiced < 21:
                if Choiced == 1:
                    print(f'\nSua carta foi um Ás, sua soma está em {soma+1}, cada vez mais perto de 21.\n')
                    soma = soma + 1
                    selected.append(1)
                    return Vinte_E_Um(moedas,exp,fome,sono,selected,soma)
                elif Choiced == 11:
                    print(f'\nSua carta foi um Valete, sua soma está em {soma+11},cada vez mais perto de 21.\n')
                    soma = soma + 11
                    selected.append(11)
                    return Vinte_E_Um(moedas,exp,fome,sono,selected,soma)
                elif Choiced == 12:
                    print(f'\nSua carta foi uma Dama, sua soma está em {soma+12},cada vez mais perto de 21.\n')
                    soma = soma + 12
                    selected.append(12)
                    return Vinte_E_Um(moedas,exp,fome,sono,selected,soma)
                elif Choiced == 13:
                    print(f'\nSua carta foi um Rei, sua soma está em {soma+13},cada vez mais perto de 21.\n')
                    soma = soma + 13
                    selected.append(13)
                    return Vinte_E_Um(moedas,exp,fome,sono,selected,soma)
                else:
                    print(f'\nSua carta foi um {Choiced},sua soma está em {soma+Choiced},cada vez mais perto de 21.\n')
                    soma = soma + Choiced
                    selected.append(Choiced)
                    return Vinte_E_Um(moedas,exp,fome,sono,selected,soma)
            elif soma + Choiced > 21:
                print(f'\nInfelizmente sua soma ficou em {soma+Choiced}, pois sua carta tinha valor {Choiced}.')
                print('O valor superou 21, então você perdeu. Espero que tenha mais sorte da próxima vez.\n')
                sono -= 7
                fome -= 3
                return Game_Over(moedas,exp,fome,sono,[],0)
            elif soma + Choiced == 21:
                print('\nA sorte está MESMO do seu lado, você conseguiu 21 pontos!!!VOCÊ VENCEU!!!')
                print('Por ter conseguido exatamente 21 pontos, você merece 150 moedas!')
                moedas += 150
                return Game_Over(moedas,exp,fome,sono,[],0)
    Card = input('\nVocê quer pegar uma carta?[S/N]: ').strip()
    if Card.upper() == 'S':
        return Yes(moedas,selected,soma,fome,sono)
    elif Card.upper() == 'N':
        final = soma
        finalShy = Card_Shy()
        time.sleep(1.5)
        if final < finalShy:
            print(f'''\nVocê conseguiu {final} pontos, enquanto ShyPy conseguiu {finalShy} pontos, então você perdeu.
( ͡¬ ᴗ ͡¬)ShyPy está se sentindo sortudo hoje.\n''')
            sono -= 7
            fome -= 3
            time.sleep(2)
            return Game_Over(moedas,exp,fome,sono,[],0)
        elif final == finalShy:
            print(f'''\nVocê conseguiu {final} pontos, assim como ShyPy. 
( ͡¬ ⏥ ͡¬)ShyPy disse que foi culpa de quem distribuiu as cartas, será?\n''')
            sono -= 7
            fome -= 3
            time.sleep(2)
            return Game_Over(moedas,exp,fome,sono,[],0)
        elif final > finalShy:
            print(f'''\nVocê conseguiu {final} pontos, superando ShyPy, que ficou com apenas {finalShy}.
( 🔥 ‿ 🔥 )ShyPy disse: "Finalmente um oponente digno!!!"\n''')
            print(f'Com essa vitória, você ganhou 70 moedas!!!')
            sono -= 4
            fome -= 1
            moedas += 70
            time.sleep(2)
            return Game_Over(moedas,exp,fome,sono,[],0)
    else:
        sono -= 1
        return Vinte_E_Um(moedas,exp,fome,sono,selected,soma)
def terceira(exp,moedas,Jogo_Escolhido,fome,sono):
    if Jogo_Escolhido == '1':
        print()
        print('Bem-Vindo ao --- Sopra - Balão ---')
        print()
        print('-*-'*32)
        print('''Neste jogo, o seu objetivo é assoprar um balão.(Jura?( ͡❛ ㅅ ͡❛))
    Este balão pode ter um tamanho de 1 até 15. Cada assopro aumenta 1 no tamanho.
    O tamanho é aleatório, e o seu objetivo é assoprar o máximo sem que ele estoure.
    Você pode assoprar o quanto quiser e sair quando quiser, tudo depende da sua sorte.
    Boa sorte, e bom jogo.''')
        print()
        time.sleep(0.2)
        print(f'-*-'*32)
        print()
        time.sleep(0.2)  
        Tamanho = random.randint(1,15)
        return Balão(Tamanho,moedas,exp,0,fome,sono)
    elif Jogo_Escolhido == '2':
        time.sleep(0.8)
        print()
        print('Bem-Vindo ao --- Pedra - Papel - Tesoura ---')
        print()
        print('-*-'*34)
        print()
        print('''   Neste jogo, você tem três escolhas a fazer... Pedra, papel e tesoura.
    Pedra vence de tesoura, tesoura vence de papel, papel vence de pedra.
    Se os dois saírem iguais, há um empate.
    ShyPy é bom nisso, você terá que ser melhor para ganhar ( ͡ಥ ᴗ ͡ಥ).
    Boa sorte, e bom jogo!!!''')
        print()
        time.sleep(0.5)
        print('-*-'*34)
        time.sleep(0.2)
        return Pedra_Papel_Tesoura(moedas,exp,fome,sono,'nada')
        def dificuldade(moedas,exp,fome,sono):
            ListaPPT = ''
            print()
            Dificuldade = input('Em qual dificuldade você deseja jogar?[FÁCIL/NORMAL/DIFÍCIL]: ')
            if Dificuldade.upper() == 'FACIL' or Dificuldade.upper() == 'FÁCIL':
                ListaPPT = ['PEDRA','PAPEL','TESOURA','TESOURA','PEDRA','PAPEL','PAPEL','TESOURA','PEDRA','PEDRA','PAPEL','TESOURA','PAPEL','TESOURA','PEDRA']
                return Pedra_Papel_Tesoura(moedas,exp,fome,sono,ListaPPT)
            elif Dificuldade.upper() == 'NORMAL':
                ListaPPT = ['PEDRA','PAPEL','TESOURA','TESOURA','PEDRA','PAPEL','PAPEL','TESOURA','PEDRA']
                return Pedra_Papel_Tesoura(moedas,exp,fome,sono,ListaPPT)
            elif Dificuldade.upper() == 'DIFICIL' or Dificuldade.upper() == 'DIFÍCIL':
                ListaPPT = ['PEDRA','PAPEL','TESOURA']
                return Pedra_Papel_Tesoura(moedas,exp,fome,sono,ListaPPT)
            else:
                return dificuldade(moedas,exp,fome,sono)
        return dificuldade(moedas,exp,fome,sono)
    elif Jogo_Escolhido == '3':
        print()
        print('Bem vindo ao --- jogo - Vinte - e - Um ---\n')
        print('~*~'*34)
        print('''\nNeste jogo, ganha quem conseguir formar 21 pontos na soma das cartas
Ou se você conseguir mais pontos que o adversário e não ultrapassar 21 pontos.
Se você ultrapassar 21, você perde automaticamente.
Boa sorte, e bom jogo!!!\n''')
        print('~*~'*34)
        sono -= 8
        fome -= 5
        return Vinte_E_Um(moedas,exp,fome,sono,[],0)
    else:
        Num_Certo = input('Esse número não está entre os jogos existentes, digite um número entre as opções: ')
        return terceira(exp,moedas,Num_Certo,fome,sono)
def quarta(exp,moedas,fome,sono):
    if sono >= 60:
        print()
        print('Pra que dormir agora? Eu nem estou com sono, vamos brincar vaii ( ͡╥ ₃ ͡╥)')
        print()
        time.sleep(0.5)
        return hub(exp,moedas,fome,sono)
    else:
        dormiu = 30
        temp = 0
        print('Vou dormir, já volto... ( ͡^ ● ͡^)')
        while temp < dormiu:
            print(f'Shypy está dormindo. Aguarde {dormiu - temp} segundos. Sonhe com os anjos,Shypy.')
            temp +=1
            time.sleep(1)
        print()
        time.sleep(1)
        print('Acordei,estou renovado, vamos voltar a brincar ( ͡◕ ᵜ ͡◕)')
        print()
        time.sleep(1)
        sono = 100
        return hub(exp,moedas,fome,sono)
def quinta(exp,moedas,fome,sono):
    time.sleep(1.2)
    print()
    print('<>'*36)
    print()
    print('''   Nós nos divertimos demais né?
    Eu fico muito feliz por ter um(a) amigo(a) como você ( ᵔ ω ᵔ )
    Mas não se esqueça de mim,okay? Estarei a espera que retorne''')
    print()
    print('<>'*36)
    time.sleep(4.5)
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    print('Então... Até logo ( ^ ω ^ )/\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    time.sleep(2)
    print(Fore.LIGHTBLUE_EX + '                                       ---S A I N D O---' + Fore.RESET)
    time.sleep(1.5)
    print()
    print('------------------------------------------------------------------------------------------------------')
    time.sleep(0.5)
    print()
    return
def escolhas(n,exp,moedas,fome,sono):
    if n == '1':
        return primeira(exp,moedas,fome,sono)
    elif n == '2':
        print()
        time.sleep(0.5)
        print('Olha só quanta comida ( ͡◐ ▿ ͡◐)')
        print()
        return segunda(exp,moedas,fome,sono)
    elif n == '3':
        print()
        time.sleep(0.2)
        print('Você quer jogar comigo!EBA!Escolhe um jogo pra gente jogar junto ( ͡❛ ‿‿ ͡❛)')
        print()
        print('Escolhas:')
        print()
        print('-+-'*20)
        print()
        print('''   [1]Sopra balão.
   [2]Pedra,Papel,Tesoura.
   [3]Vinte e um.''')
        print()
        print('-+-'*20)
        print()
        time.sleep(0.5)
        Jogo_Escolhido = input('Digite o número do jogo desejado: ').strip()
        return terceira(exp,moedas,Jogo_Escolhido,fome,sono)
    elif n == '4':
        return quarta(exp,moedas,fome,sono)
    elif n == '5':
        return quinta(exp,moedas,fome,sono)
    else:
        certo = input('Esse número não está nas opções, escolha um válido: ')
        print()
        return escolhas(certo,exp,moedas,fome,sono)
def hub(exp,moedas,fome,sono):
    time.sleep(1.5)
    print('E então, o que faremos agora?¯\_( ͡◕ ω ͡◕)_/¯')
    print()
    print('-'*102)
    print('''    [1]Informações do jogo.
    [2]Me alimente.
    [3]Jogue comigo.
    [4]Me coloque pra ninar.
    [5]Sair do jogo.''')
    print('-'*102)
    Escolha = input('Digite o número do que você deseja: ').strip()
    print()
    escolhas(Escolha,exp,moedas,fome,sono)
def apresentação(exp,moedas,fome,sono):
    time.sleep(1.5)
    print('I n i c i a l i z a n d o...')
    time.sleep(1)
    print()
    print('. . .')
    time.sleep(0.8)
    print()
    print('. . . . . .')
    time.sleep(0.9)
    print()
    print('. . . . . . . .')
    time.sleep(3)
    print()
    print('!!! B E M  V I N D O !!!')
    time.sleep(1.5)
    print()
    print('--*--'*10)
    print()
    print('''   Olá, eu sou ShyPy ( ͡◕ ω ͡◕)
    Se você está aqui, é porque me adotou.
    Espero que possamos ser melhores amigos!!!
    Nós podemos comer, jogar e dormir juntos.
   Isso vai ser tão legal!!! ( ͡♥ ω ͡♥)''')
    print()
    print('--*--'*10)
    time.sleep(8)
    print()
    return hub(exp,moedas,fome,sono)
apresentação(0,0,100,100)
