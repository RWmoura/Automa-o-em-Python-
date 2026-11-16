import os
import time
import pyautogui
from selenium import webdriver
from datetime import datetime, timedelta

def cadastro_gsus():
    cpf = input('CPF:')
    dias_para_liberacao = int(input("Digite o número de dias a ser Liberado o acesso: "))
    
    while True:

        print("\n=== Escolha o Conselho e CBO ===")
        print("1 - COREN-PR  (Técnico de enfermagem)")
        print("3 - COREN-PR  (Enfermeiro)")
        print("2 - CRM-PR    (Médico clínico)")
        print("4 - CRM-PR    (Médico ortopedista e traumatologista)")
        print("5 - CRM-PR    (Médico cardiologista)")
        print("6 - CRM-PR    (Médico anestesiologista)")
        print("0 - Sair")

        opcao_cbo = input("\nEscolha: ")
        conselho = 0
        cbo = 0

        if opcao_cbo == "1":
            print("Encerrando sistema...")
            conselho = 0
            cbo = 0
            break

        elif opcao_cbo == "2":
            conselho = 0
            cbo = 0
            break

        elif opcao_cbo == "3":
            conselho = 0
            cbo = 0
            break
    
        elif opcao_cbo == "4":
            conselho = 0
            cbo = 0
            break

        elif opcao_cbo == "5":
            conselho = 0
            cbo = 0
            break

        elif opcao_cbo == "6":
            conselho = 0
            cbo = 0
            break

        else:
            print("Digite uma opção válida!")
            exit()
    

    numero_conselho = input('Digite o N° do conselho:')
    data_hoje = datetime.now()
    data_final = data_hoje + timedelta(days=dias_para_liberacao)
    data = data_final.strftime("%d/%m/%Y")
    
    driver = webdriver.Firefox()
    driver.maximize_window()
    
    try:
        driver.get("http://gsus.pr.gov.br")
        driver.maximize_window()
        time.sleep(4)
        pyautogui.press("tab")
        time.sleep(0.15)
        pyautogui.press("enter")
        time.sleep(0.15)
        pyautogui.write('46074233861')
        time.sleep(0.15)
        pyautogui.press("tab")
        time.sleep(0.15)
        pyautogui.write('Helo2606!')
        time.sleep(0.15)
        pyautogui.press("enter")
        time.sleep(7)
        pyautogui.press('tab', presses=7, interval=0.1)
        time.sleep(0.15)
        pyautogui.press("enter")
        time.sleep(5)
        #Dentro do GSUS
        pyautogui.moveTo(64, 135)
        time.sleep(0.15)
        pyautogui.moveTo(91, 160)
        time.sleep(0.15)
        pyautogui.click()
        time.sleep(4)
        pyautogui.press('tab', presses=5, interval=0.1)
        time.sleep(0.15)
        pyautogui.write(str(cpf))
        time.sleep(0.15)
        pyautogui.press('tab', presses=10, interval=0.1)
        time.sleep(0.15)
        pyautogui.press("enter")
        time.sleep(4)
        #perfil aberto
        pyautogui.write(data_hoje.strftime("%d/%m/%Y"))
        time.sleep(0.15)
        pyautogui.press('tab')
        time.sleep(0.15)
        pyautogui.write(data)
        time.sleep(0.15)
        pyautogui.press('tab', presses=3, interval=0.1)
        time.sleep(0.15)
        pyautogui.press("enter")
        time.sleep(0.15)
        pyautogui.press('tab', presses=3, interval=0.1)
        time.sleep(0.15)
        pyautogui.press('down', presses=3, interval=0.1) #selecionar coren
        time.sleep(0.15)
        pyautogui.press('tab', presses=2, interval=0.1)
        time.sleep(0.15)
        pyautogui.write(numero_conselho)
        pyautogui.press('tab', presses=5, interval=0.1)#para enfermeiro
        #pyautogui.press('tab', presses=18, interval=0.1)#para Téc enfermagem
        time.sleep(0.15)
        pyautogui.press('tab', presses=5, interval=0.1)
        time.sleep(0.15)
        #pyautogui.press("enter") #Confirmar
















        time.sleep(40)
        print("FIM")
        

    except Exception as e:
        print(f"\n[ERRO]: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    cadastro_gsus()
