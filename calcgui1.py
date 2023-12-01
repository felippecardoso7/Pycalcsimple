# Interface Grafica

import PySimpleGUI as psg
from calcteste import soma

layout = [
    [psg.Text('informe N1: '), psg.InputText(key='Num1')],
    [psg.Text('informe N2: '), psg.InputText(key='Num2')],
    [psg.Text('', key='Total')],
    [psg.Button('Calcular')]],

janela = psg.Window('Calculadora Simples', layout)

while True:
    eventos, valores = janela.read()

    if eventos == psg.WIN_CLOSED:
        break
    else:
        n1 = int(valores['Num1'])
        n2 = int(valores['Num2'])
        total =soma(n1, n2)
        janela['Total '].update(total)


