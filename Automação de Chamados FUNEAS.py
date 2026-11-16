import pyautogui
from selenium import webdriver
import time
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#Autor: Rafael Ribeiro Moura

servico = Service(r"c:\Users\rafael.moura\Documents\AUTOMAÇÃO\chromedriver.exe")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def local_eprotocolo():

    locais = {
        "1": {"Local": "SESA/HZN/ALMOXARIFADO"},
        "2": {"Local": "SESA/HZN/CC"},
        "3": {"Local": "SESA/HZN/CCIH"},
        "4": {"Local": "SESA/HZN/CPD"},
        "5": {"Local": "SESA/HZN/COMPRAS"},
        "6": {"Local": "SESA/HZN/CONTRATOS"},
        "7": {"Local": "SESA/HZN/COREME"},
        "8": {"Local": "SESA/HZN/DA"},
        "9": {"Local": "SESA/HZN/DAS"},
        "10": {"Local": "SESA/HZN/DG"},
        "11": {"Local": "SESA/HZN/DT"},
        "12": {"Local": "SESA/HZN/EQ MULTI"},
        "13": {"Local": "SESA/HZN/SUP"},
        "14": {"Local": "SESA/HZN/FARMACIA"},
        "15": {"Local": "SESA/HZN/FATURAMENTO"},
        "16": {"Local": "SESA/HZN/FINANCEIRO"},
        "17": {"Local": "SESA/HZN/HOTELARIA"},
        "18": {"Local": "SESA/HZN/INFRA"},
        "19": {"Local": "SESA/HZN/OUV"},
        "20": {"Local": "SESA/HZN/PAT"},
        "21": {"Local": "SESA/HZN/PTG"},
        "22": {"Local": "SESA/HZN/QNSP"},
        "23": {"Local": "SESA/HZN/RH"},
        "24": {"Local": "SESA/HZN/SAME"},
        "25": {"Local": "SESA/HZN/SERV"},
        "26": {"Local": "SESA/HZN/TI"},
        "27": {"Local": "SESA/HZN/SERV(Acesso Restrito ao local)"}
    }

    acessos = []

    while True:

        print("\n=== SELECIONE OS LOCAIS DE ACESSO ===\n")

        for chave, local in locais.items():
            print(f"{chave} - {local['Local']}")

        print("0 - Finalizar seleção")

        opcao = input("\nEscolha: ")

        clear()

        # FINALIZAR
        if opcao == "0":

            if len(acessos) == 0:
                print("Nenhum local foi selecionado!")
                continue

            return acessos

        # OPÇÃO VÁLIDA
        elif opcao in locais:

            acesso = {
                "Local": locais[opcao]["Local"]
            }

            # EVITAR DUPLICIDADE
            if acesso not in acessos:

                acessos.append(acesso)

                print("Local adicionado com sucesso!\n")

            else:
                print("Esse local já foi adicionado!\n")

        # OPÇÃO INVÁLIDA
        else:
            print("Digite uma opção válida!")

def caminho_rede():

    pastas = {

        "1": {
            "nome": "DOCUMENTOS COMUNS",
            "caminho": r"\\cluster.arquivos.parana\sesa\hospitais\hzn\DOCUMENTOS COMUNS",
            "grupo": "HZN-DOCUMENTOS-COMUNS"
        },

        "2": {
            "nome": "MANUTENCAO",
            "caminho": r"\\cluster.arquivos.parana\sesa\hospitais\hzn\DIRECAO ADMINISTRATIVA\APOIO ADMINISTRATIVO\MANUTENCAO",
            "grupo": "HZN-ADM-APOIO-ADM-MANU"
        },

        "3": {
            "nome": "GESTAO DE SUPRIMENTOS",
            "caminho": r"\\cluster.arquivos.parana\sesa\hospitais\hzn\DIRECAO ADMINISTRATIVA\APOIO ADMINISTRATIVO\GESTAO DE SUPRIMENTOS",
            "grupo": "HZN-ADM-APOIO-ADM-SUP"
        },

        "4": {
            "nome": "NUCLEO FINANCEIRO",
            "caminho": r"\\cluster.arquivos.parana\sesa\hospitais\hzn\direcao administrativa\NUCLEO FINANCEIRO",
            "grupo": "HZN-ADM-NUCLEO FINANCEIRO"
        },

        "5": {
            "nome": "CCIH",
            "caminho": r"\\cluster.arquivos.parana\sesa\hospitais\hzn\DIRECAO GERAL\GESTAO DE SAUDE\CCIH",
            "grupo": "HZN-GERAL-GES-SAU-CCIH"
        },
        "6": {
            "nome": "DIREÇÃO ENFERMAGEM",
            "caminho": r"\\cluster.arquivos.parana\sesa\hospitais\hzn\DIRECAO ASSISTENCIAL",
            "grupo": "HZN-ASSIS-DIR-ASSIS"
        },
        "7": {
            "nome": "PSICOLOGIA ORGANIZACIONAL",
            "caminho": r"\\cluster.arquivos.parana\sesa\hospitais\hzn\DIRECAO GERAL\GESTAO DE PESSOAS\PSICOLOGIA ORGANIZACIONAL",
            "grupo": "HZN-GERAL-GES-PES-PSICO"
        },
        "8": {
            "nome": "SAUDE DO TRABALHADOR",
            "caminho": r"\\cluster.arquivos.parana\sesa\hospitais\hzn\DIRECAO GERAL\GESTAO DE PESSOAS\SAUDE DO TRABALHADOR",
            "grupo": ""
        },
        "9": {
            "nome": "SAME DIGITAL",
            "caminho": r"\\cluster.arquivos.parana\sesa\hospitais\hzn\DIRECAO ADMINISTRATIVA\SAME DIGITAL",
            "grupo": "HZN-ADM-SAME-DIGITAL"
        },
        "10": {
            "nome": "DIREÇÃO GERAL",
            "caminho": r"\\cluster.arquivos.parana\sesa\hospitais\hzn\DIRECAO GERAL",
            "grupo": "HZN-ASSIS-DIR-GERAL"
        },
        "11": {
            "nome": "PATRIMÔNIO",
            "caminho": r"\\cluster.arquivos.parana\sesa\hospitais\hzn\DIRECAO ADMINISTRATIVA\APOIO FINANCEIRO\PATRIMONIO",
            "grupo": "HZN-ADM-APOIO-FIN-PAT"
        },
        "12": {
            "nome": "RH (ATUAL)",
            "caminho": r"\\cluster.arquivos.parana\sesa\hospitais\hzn\DIRECAO GERAL\GESTAO DE PESSOAS\ROTINAS DE PESSOAL",
            "grupo": "HZN-GERAL-GES-PES-ROTI"
        },
        "13": {
            "nome": "QUALIDADE",
            "caminho": r"\\cluster.arquivos.parana\sesa\hospitais\hzn\DIRECAO GERAL\GESTAO DE SAUDE\QUALIDADE",
            "grupo": "HZN-GERAL-GES-SAU-QUALI"
        },
        "14": {
            "nome": "QUALI(SUPER)",
            "caminho": r"\\cluster.arquivos.parana\sesa\hospitais\hzn\DIRECAO GERAL\GESTAO DE SAUDE\SUPERVISAO",
            "grupo": "HZN-GERAL-GES-SAU-SUPER"
        }
    }

    acessos = []

    while True:

        print("\n=== SELECIONE OS ACESSOS AS PASTAS DE REDE ===\n")

        for chave, pasta in pastas.items():
            print(f"{chave} - {pasta['nome']}")

        print("0 - Finalizar seleção")

        opcao = input("\nEscolha: ")

        clear()

        # FINALIZAR
        if opcao == "0":

            # VALIDA SE FOI ESCOLHIDO AO MENOS 1 ACESSO
            if len(acessos) == 0:
                print("Nenhuma pasta selecionada!")
                continue

            return acessos

        # OPÇÃO VÁLIDA
        elif opcao in pastas:

            acesso = {
                "caminho": pastas[opcao]["caminho"],
                "grupo": pastas[opcao]["grupo"]
            }

            # EVITAR DUPLICIDADE
            if acesso not in acessos:
                acessos.append(acesso)
                print("Acesso adicionado com sucesso!\n")
            else:
                print("Esse acesso já foi adicionado!\n")

        # OPÇÃO INVÁLIDA
        else:
            print("Digite uma opção válida!")

def abrir_chamado_funeas(tipo_problema, descricao):
    driver = webdriver.Chrome(service=servico)
    driver.maximize_window()
    driver.get("http://10.29.234.245/chamado/index.php")
    time.sleep(1)
    pyautogui.write('----Login----')
    pyautogui.press("tab")
    pyautogui.write('----Senha----')
    pyautogui.press("enter")
    time.sleep(6)
    pyautogui.click(94, 196)
    time.sleep(6)
    pyautogui.click(102, 378)
    time.sleep(6)
    pyautogui.press('tab', presses=6)
    time.sleep(1.5)
    pyautogui.press("enter")
    time.sleep(0.15)
    pyautogui.press("down")
    time.sleep(0.15)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("tab")
    time.sleep(0.15)
    pyautogui.press("down")
    time.sleep(0.15)
    pyautogui.write(tipo_problema)
    time.sleep(0.15)
    pyautogui.press("enter")
    time.sleep(0.15)
    pyautogui.press('tab', presses=2)
    time.sleep(0.15)
    pyautogui.write(descricao)
    time.sleep(0.15)
    pyautogui.press('tab', presses=3)
    time.sleep(0.15)
    pyautogui.press("enter")
    time.sleep(0.15)
    pyautogui.write('16')
    time.sleep(0.15)
    pyautogui.press("enter")
    time.sleep(0.15)
    pyautogui.press("tab")
    time.sleep(0.15)
    pyautogui.write('Marcos Jose Bernardes Jr.')
    time.sleep(0.15)
    pyautogui.press('tab', presses=2)
    time.sleep(0.15)
    pyautogui.write('4333764604')
    time.sleep(0.15)
    pyautogui.press('tab', presses=2)
    time.sleep(0.15)
    pyautogui.press("down")
    time.sleep(0.15)
    pyautogui.write('Gerencia de Tecnologia da Informacao')
    time.sleep(0.15)
    pyautogui.press("enter")
    time.sleep(0.15)
    pyautogui.press('tab', presses=9)
    time.sleep(0.15)
    pyautogui.write('10.29.49.151')
    time.sleep(0.15)
    pyautogui.press('tab', presses=2)
    time.sleep(9000)

clear()

print("===================================")
print(" SISTEMA DE AUTOMAÇÃO DE TAREFAS")
print("===================================\n")

nome = input("Nome do colaborador: ")
cpf = input("CPF do colaborador: ")
login = " "
local_ep = " "

clear()

while True:

    print("\n=== Escolha o processo a ser Executado ===")
    print("1 - Criar Usuário de rede e Proxy")
    print("2 - Criar Usuário de rede e Proxy Com Pasta de Rede")
    print("3 - Reset senha de Rede")
    print("4 - Reset senha de Proxy")
    print("5 - Senha Admin")
    print("6 - Acesso a Pasta de rede")
    print("7 - Acesso ao Local do E-protocolo")
    print("8 - GSUS")
    print("9 - Descrição Manual")
    print("0 - Sair")

    opcao = input("\nEscolha: ")
    clear()

    descricao = ""
    tipo_de_problema = ""

    if opcao == "1":

        descricao = (
            f"Criar usuário de rede/proxy para o colaborador:\n"
            f"Nome: {nome}\n"
            f"CPF: {cpf}"
        )
        tipo_de_problema = "CRIACAO DE USUARIO - REDE/EXPRESSO"
        abrir_chamado_funeas(tipo_de_problema, descricao)
        break

    elif opcao == "2":

        acessos = caminho_rede()

        descricao = (
            f"Criar usuário de rede/proxy para o colaborador:\n"
            f"Nome: {nome}\n"
            f"CPF: {cpf}\n\n"
        )

        descricao += "Conceder acesso às seguintes pastas:\n\n"

        for acesso in acessos:

            descricao += (
                f"Caminho: {acesso['caminho']}\n"
                f"Grupo de acesso: {acesso['grupo']}\n\n"
            )
        tipo_de_problema = "CRIACAO DE USUARIO - REDE/EXPRESSO"
        abrir_chamado_funeas(tipo_de_problema, descricao)
        break

    elif opcao == "3":
        print(nome)
        login = input("Login:")
        descricao = (
            f"Reset de senha do usuario de rede do colaborador:\n"
            f"Nome: {nome}\n"
            f"CPF: {cpf}\n"
            f"login: {login}"
        )
        tipo_de_problema = "RESET DE SENHA REDE(AD)/EXPRESSO"
        abrir_chamado_funeas(tipo_de_problema, descricao)
        break

    elif opcao == "4":
        print(nome)
        login = input("Login:")
        descricao = (
            f"Resetar senha de PROXY do colaborador:\n"
            f"Nome: {nome}\n"
            f"CPF: {cpf}\n"
            f"login: {login}"
        )
        tipo_de_problema = "RESET DE SENHA REDE(AD)/EXPRESSO"
        abrir_chamado_funeas(tipo_de_problema, descricao)
        break

    elif opcao == "5":
        descricao = ("solicito senha hzn.adm, se possivel colocar especificamente a senha como: @saude")
        tipo_de_problema = "INSTALACAO DE SOFTWARES"
        abrir_chamado_funeas(tipo_de_problema, descricao)
        break

    elif opcao == "6":
        print(nome)
        login = input("Login:")
        acessos = caminho_rede()
        descricao = (
            f"Conceder acesso às seguintes pastas para o colaborador:\n"
            f"Nome: {nome}\n"
            f"CPF: {cpf}\n"
            f"login: {login}\n"
        )

        for acesso in acessos:

            descricao += (
                f"Caminho: {acesso['caminho']}\n"
                f"Grupo de acesso: {acesso['grupo']}\n\n"
            )
        tipo_de_problema = "ACESSOS AS PASTAS DE REDE"
        abrir_chamado_funeas(tipo_de_problema, descricao)
        break

    elif opcao == "7":
        
        acessos = local_eprotocolo()

        descricao = (
            f"Conceder acesso ao local do eprotocolo para:\n"
            f"Nome: {nome}\n"
            f"CPF: {cpf}\n"
        )

        descricao += "\n"

        for acesso in acessos:

            descricao += (
                f"Local: {acesso['Local']}\n"
            )
        tipo_de_problema = "EPROTOCOLO - ACESSO A LOCAL DO EPROTOCOLO"
        abrir_chamado_funeas(tipo_de_problema, descricao)
        break

    elif opcao == "0":

        print("Encerrando sistema...")
        exit()

    else:
        print("Digite uma opção válida!")

clear()

print("===================================")
print(" DESCRIÇÃO DO CHAMADO GERADA ")
print("===================================\n")

print(descricao)

print("\n===================================")
print(" FIM DO PROCESSO ")
print("===================================")
