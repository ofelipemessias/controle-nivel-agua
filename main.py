from colorama import Fore, Style, init

init(autoreset=False)

niveis = [
    (1, "Muito baixo (crítico)"),
    (2, "Baixo"),
    (3, "Médio"),
    (4, "Alto"),
    (5, "Muito alto (alerta)"),
]

def cor_do_nivel(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    else:
        return Fore.BLUE

for nivel, situacao in niveis:
    cor = cor_do_nivel(nivel)
    print(f"{cor}Nível {nivel}: {situacao}{Style.RESET_ALL}")
