def Generar_Numero (act_tipo, act_cont):
    if act_tipo == '1':
        numero = 'B-2020-' + str(act_cont)
    elif act_tipo == '2':
        numero = 'S-2020-' + str(act_cont)
    elif act_tipo == '3':
        numero = 'I-2020-' + str(act_cont)
    return numero

def Introducir_Serial():
    while True:    
        try:
            serial = int(input('Serial: '))
            break
        except (ValueError, TypeError):
            print('Solo se permiten números')
    return serial