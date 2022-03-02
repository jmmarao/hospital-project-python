#1ª ETAPA DO PROJETO PRÁTICO
#TEMA: HOSPITAL

#ESTRUTURA UTILIZADA: Dicionários de dicionário
#medicos = {'CRM':{'NOME': nome, 'NASC': nasc, 'SEXO': sexo, 'ESP': esp,
#                  'UNIV': univ, 'E-MAIL': [emails], 'TEL': [telefones]}
#           'CRM':{'NOME': nome, 'NASC': nasc, 'SEXO': sexo, 'ESP': esp,
#                  'UNIV': univ, 'E-MAIL': [emails], 'TEL': [telefones]}
#           }
#pacientes = {'CPF':{'NOME': nome, 'NASC': nasc, 'SEXO': sexo, 'PLANO': plan,
#                  'E-MAIL': [emails], 'TEL': [telefones]}
#           'CPF':{'NOME': nome, 'NASC': nasc, 'SEXO': sexo, 'PLANO': plan,
#                  'E-MAIL': [emails], 'TEL': [telefones]}
#            }
#consultas = {('CRM', 'CPF', 'DATA, HORA'):{'DIAGNÓSTICO': dig,
#                                           'MEDICAMENTOS': [medic]}
#              ('CRM', 'CPF', 'DATA, HORA'):{'DIAGNÓSTICO': dig,
#                                           'MEDICAMENTOS': [medic]}
#OBS1: Emails, Telefones e Medicamentos são listas, pois podem apresentar mais de um valor
#OBS2: A chave do dicionário de consultas é uma tupla ()

#====================================================================
#Função para apresentar o menu de opções para o usuário
def menu():
    print('\n{:=^50}'.format(' MENU DE OPÇÕES '))
    print('''\n[ 1 ] Submenu de Médicos
[ 2 ] Submenu de Pacientes
[ 3 ] Submenu de Consultas
[ 4 ] Submenu Relatórios
[ 5 ] Sair\n''')
    print('='*50)

#====================================================================
#[ 1 ]
#Função para apresentar o submenu de médicos para o usuário
def menu_medico():
    print('\n{:=^50}'.format(' SUBMENU - MÉDICOS '))
    print('''\n[ 1 ] Listar todos
[ 2 ] Listar por CRM
[ 3 ] Incluir
[ 4 ] Alterar
[ 5 ] Excluir\n''')
    print('='*50)

#====================================================================
#Função para verificar o registro de algum CRM.
#Se o valor retornado for -1, o CRM não está registrado
def buscar_crm(buscar_crm, medicos):
    for crm in medicos.keys():
        if crm == buscar_crm:
            return crm
    return -1

#====================================================================
#Função para imprimir todos os médicos
#[ 1 ][ 1 ]
def listar_medicos(medicos):
    print('\n{:=^50}'.format(' LISTAR MÉDICOS - TODOS '))
    for crm in medicos:
        print('\nNome: {}'.format(medicos[crm]['Nome']))
        print('CRM: {}'.format(crm))
        print('Data de Nascimento: {}'.format(medicos[crm]['Nascimento']))
        print('Sexo: {}'.format(medicos[crm]['Sexo']))
        print('Especialidade: {}'.format(medicos[crm]['Especialidade']))
        print('Formado(a) na: {}'.format(medicos[crm]['Universidade']))
        print('E-mail(s):')
        for i in medicos[crm]['E-mail']:
            print('\t{}'.format(i))
        print('Telefone(s):')
        for j in medicos[crm]['Telefones']:
            print('\t{}'.format(j))
        print()
        print('-'*50)

#====================================================================
#Função para imprimir os dados de um médico de acordo com seu CRM
#[ 1 ][ 2 ]
def listar_crm(crm, medicos):
    print('\nNome: {}'.format(medicos[crm]['Nome']))
    print('CRM: {}'.format(crm))
    print('Data de Nascimento: {}'.format(medicos[crm]['Nascimento']))
    print('Sexo: {}'.format(medicos[crm]['Sexo']))
    print('Especialidade: {}'.format(medicos[crm]['Especialidade']))
    print('Formado(a) na: {}'.format(medicos[crm]['Universidade']))
    print('E-mail(s):')
    for i in medicos[crm]['E-mail']:
        print('\t{}'.format(i))
    print('Telefone(s):')
    for j in medicos[crm]['Telefones']:
        print('\t{}'.format(j))
    print()

#====================================================================
#[ 1 ][ 3 ]
#Função para cadastrar um médico
#[ 1 ][ 4 ]
#Função para alterar o cadastro de um médico
def incluir_medico(crm, medico):
    nome = input('Nome: ').strip().title()
    nasc = input('Data de nascimento [dd/mm/aaaa]: ').strip()
    sexo = input('Sexo [F/M]: ').strip().upper()
    esp = input('Especialidade: ').strip().capitalize()
    univ = input('Instituição de formação: ').strip().upper()
    emails = []
    mail = input('E-mail: ').strip()
    emails.append(mail)
    pergunta1 = input('Deseja adicionar outro e-mail [S/N]? ').strip().lower()
    while pergunta1 != 'n': #LOOP PARA GUARDAR MAIS E-MAILS
        if pergunta1 == 's':
            mail = input('E-mail: ').strip()
            emails.append(mail)
            pergunta1 = input('Deseja adicionar outro e-mail [S/N]? ').strip().lower()
        else: #OPÇÕES INVÁLIDAS (DIFERENTES DE Nn OU Ss)
            print('\n{:*^50}'.format(' ATENÇÃO! '))
            print('{:^50}'.format(' Opção INVÁLIDA. Tente novamente '))
            print('*'*50)
            pergunta1 = input('\nDeseja adicionar outro e-mail [S/N]? ').strip().lower()
    telefones = []
    tel = input('Telefone: ').strip()
    telefones.append(tel)
    pergunta2 = input('Deseja adicionar outro telefone [S/N]? ').strip().lower()
    while pergunta2 != 'n': #LOOP PARA GUARDAR MAIS TELEFONES
        if pergunta2 == 's':
            tel = input('Telefone: ').strip()
            telefones.append(tel)
            pergunta2 = input('Deseja adicionar outro telefone [S/N]? ').strip().lower()
        else: #Opções INVÁLIDAS (DIFERENTES DE Nn OU Ss)
            print('\n{:*^50}'.format(' ATENÇÃO! '))
            print('{:^50}'.format(' Opção INVÁLIDA. Tente novamente '))
            print('*'*50)
            pergunta2 = input('\nDeseja adicionar outro telefone [S/N]? ').strip().lower()
    medico[crm] = {
        'Nome': nome,
        'Nascimento': nasc,
        'Sexo': sexo,
        'Especialidade': esp,
        'Universidade': univ,
        'E-mail': emails,
        'Telefones': telefones
        }

#====================================================================
#[ 1 ][ 5 ]
#Função para excluir um médico já cadastrado de acordo com seu CRM
def del_medico(crm, medicos):
    del medicos[crm]
    print('\nMédico removido com sucesso!')

#====================================================================
#[ 2 ]
#Função para apresentar o submenu de pacientes para o usuário
def menu_paciente():
    print('\n{:=^50}'.format(' SUBMENU - PACIENTES '))
    print('''\n[ 1 ] Listar todos
[ 2 ] Listar por CPF
[ 3 ] Incluir
[ 4 ] Alterar
[ 5 ] Excluir\n''')
    print('='*50)

#====================================================================
#Função para verificar o registro de algum CPF.
#Se o valor retornado for -1, o CPF não está registrado
def buscar_cpf(buscar_cpf, pacientes):
    for cpf in pacientes.keys():
        if cpf == buscar_cpf:
            return cpf
    return -1

#====================================================================
#Função para imprimir todos os médicos
#[ 2 ][ 1 ]
def listar_pacientes(pacientes):
    print('\n{:=^50}'.format(' LISTAR PACIENTES - TODOS '))
    for cpf in pacientes:
        print('\nNome: {}'.format(pacientes[cpf]['Nome']))
        print('CPF: {}'.format(cpf))
        print('Data de Nascimento: {}'.format(pacientes[cpf]['Nascimento']))
        print('Sexo: {}'.format(pacientes[cpf]['Sexo']))
        print('Plano de saude: {}'.format(pacientes[cpf]['Plano']))
        print('E-mail(s):')
        for i in pacientes[cpf]['E-mail']:
            print('\t{}'.format(i))
        print('Telefone(s):')
        for j in pacientes[cpf]['Telefones']:
            print('\t{}'.format(j))
        print()
        print('-'*50)

#====================================================================
#[ 2 ][ 2 ]
#Função para imprimir os dados de um paciente de acordo com seu CPF
def listar_cpf(cpf, pacientes):
    print('\nNome: {}'.format(pacientes[cpf]['Nome']))
    print('CPF: {}'.format(cpf))
    print('Data de Nascimento: {}'.format(pacientes[cpf]['Nascimento']))
    print('Sexo: {}'.format(pacientes[cpf]['Sexo']))
    print('Plano de Saúde: {}'.format(pacientes[cpf]['Plano']))
    print('E-mail(s):')
    for i in pacientes[cpf]['E-mail']:
        print('\t{}'.format(i))
    print('Telefone(s):')
    for j in pacientes[cpf]['Telefones']:
        print('\t{}'.format(j))
    print()

#====================================================================
#[ 2 ][ 3 ]
#Função para cadastrar um paciente
#[ 2 ][ 4 ]
#Função para alterar o cadastro de um paciente
def incluir_paciente(cpf, paciente):
    nome = input('Nome: ').strip().title()
    nasc = input('Data de nascimento [dd/mm/aaaa]: ').strip()
    sexo = input('Sexo [F/M]: ').strip().upper()
    plan = input('Plano de saude: ').strip().upper()
    emails = []
    mail = input('E-mail: ').strip()
    emails.append(mail)
    pergunta1 = input('Deseja adicionar outro e-mail [S/N]? ').strip().lower()
    while pergunta1 != 'n': #LOOP PARA GUARDAR MAIS E-MAILS
        if pergunta1 == 's':
            mail = input('E-mail: ').strip()
            emails.append(mail)
            pergunta1 = input('Deseja adicionar outro e-mail [S/N]? ').strip().lower()
        else: #OPÇÕES INVÁLIDAS (DIFERENTES DE Nn OU Ss)
            print('\n{:*^50}'.format(' ATENÇÃO! '))
            print('{:^50}'.format(' Opção INVÁLIDA. Tente novamente '))
            print('*'*50)
            pergunta1 = input('\nDeseja adicionar outro e-mail [S/N]? ').strip().lower()
    telefones = []
    tel = input('Telefone: ').strip()
    telefones.append(tel)
    pergunta2 = input('Deseja adicionar outro telefone [S/N]? ').strip().lower()
    while pergunta2 != 'n': #LOOP PARA GUARDAR MAIS TELEFONES
        if pergunta2 == 's':
            tel = input('Telefone: ').strip()
            telefones.append(tel)
            pergunta2 = input('Deseja adicionar outro telefone [S/N]? ').strip().lower()
        else: #Opções INVÁLIDAS (DIFERENTES DE Nn OU Ss)
            print('\n{:*^50}'.format(' ATENÇÃO! '))
            print('{:^50}'.format(' Opção INVÁLIDA. Tente novamente '))
            print('*'*50)
            pergunta2 = input('\nDeseja adicionar outro telefone [S/N]? ').strip().lower()
    paciente[cpf] = {
        'Nome': nome,
        'Nascimento': nasc,
        'Sexo': sexo,
        'Plano': plan,
        'E-mail': emails,
        'Telefones': telefones
        }

#====================================================================
#[ 2 ][ 5 ]
#Função para excluir um paciente já cadastrado de acordo com seu CPF
def del_paciente(cpf, pacientes):
    del pacientes[cpf]
    print('\nPaciente removido com sucesso!')

#====================================================================
#[ 3 ]
#Função para apresentar o submenu de consultas para o usuário
def menu_consulta():
    print('\n{:=^50}'.format(' SUBMENU - CONSULTAS '))
    print('''\n[ 1 ] Listar todos
[ 2 ] Listar por elementos (CRM, CPF, data e hora)
[ 3 ] Incluir
[ 4 ] Alterar
[ 5 ] Excluir\n''')
    print('='*50)

#====================================================================
#Função para criar uma chave (tupla) de consulta
# chave = (crm, cpf, data, hora)
def criar_chave(medicos, pacientes, consultas, chave):
    crm = input('\nCRM [incluir pontuação]: ').strip()
    verif1 = buscar_crm(crm, medicos)
    while verif1 == -1:#Loop para CRM inexistentes
        print('\n{:*^50}'.format(' ATENÇÃO! '))
        print('{:^50}'.format(' CRM NÃO CADASTRADO! Tente novamente '))
        print('*'*50)
        crm = input('\nCRM [incluir pontuação]: ').strip()
        verif1 = buscar_crm(crm, medicos)                    
    cpf = input('CPF [incluir pontuação]: ').strip()
    verif2 = buscar_cpf(cpf, pacientes)
    while verif2 == -1:#Loop para CPF inexistentes
        print('\n{:*^50}'.format(' ATENÇÃO! '))
        print('{:^50}'.format(' CPF NÃO CADASTRADO! Tente novamente '))
        print('*'*50)
        cpf = input('CPF [incluir pontuação]: ').strip()
        verif2 = buscar_cpf(cpf, pacientes)
    data = input('Data da consulta[dd/mm/aaaa]: ').strip()
    hora = input('Horário da consulta [hh:mm]: ').strip()
    chave = (crm, cpf, data, hora)
    return chave
    
#====================================================================
#Função para verificar o registro da chave de consulta
#Se o valor retornado for -1, a chave não está registrado
def buscar_chave(buscar_chave, consultas):
    for chave in consultas.keys():
        if chave == buscar_chave:
            return chave
    return -1

#====================================================================
#Função para imprimir todas as consultas
#[ 3 ][ 1 ]
def listar_consultas(consultas, medicos, pacientes):
    print('\n{:=^50}'.format(' LISTAR CONSULTAS - TODAS '))
    for chave in consultas:
        print('\nMédico: {}'.format(medicos[chave[0]]['Nome']))
        print('CRM: {}'.format(chave[0]))
        print('Paciente: {}'.format(pacientes[chave[1]]['Nome']))
        print('CPF: {}'.format(chave[1]))
        print('Data: {}'.format(chave[2]))
        print('Horário: {}'.format(chave[3]))
        print('Diagnóstico: {}'.format(consultas[chave]['Diagnóstico']))
        print('Medicamento(s):')
        for j in consultas[chave]['Medicamento']:
            print('\t{}'.format(j))
        print()
        print('-'*50)

#====================================================================
#[ 3 ][ 2 ]
#Função para imprimir os dados de uma consulta de acordo com sua chave(tupla)
# chave = (crm, cpf, data, hora)
def listar_chave(chave, consultas, medicos, pacientes):
    print('\nMédico: {}'.format(medicos[chave[0]]['Nome']))
    print('CRM: {}'.format(chave[0]))
    print('Paciente: {}'.format(pacientes[chave[1]]['Nome']))
    print('CPF: {}'.format(chave[1]))
    print('Data: {}'.format(chave[2]))
    print('Horário: {}'.format(chave[3]))
    print('Diagnóstico: {}'.format(consultas[chave]['Diagnóstico']))
    print('Medicamento(s):')
    for j in consultas[chave]['Medicamento']:
        print('\t{}'.format(j))
    print()

#====================================================================
#[ 3 ][ 3 ]
#Função para cadastrar uma consulta
#[ 3 ][ 4 ]
#Função para alterar o cadastro de uma consulta
def incluir_consulta(chave, consulta):
    dig = input('Diagnóstico: ').strip().title()
    medicamentos = []
    med = med = input('Medicamento: ').strip().capitalize()
    medicamentos.append(med)
    pergunta = input('Deseja adicionar outro medicamento [S/N]? ').strip().lower()
    while pergunta != 'n': #LOOP PARA GUARDAR MAIS MEDICAMENTOS
        if pergunta == 's':
            med = med = input('Medicamento: ').strip().capitalize()
            medicamentos.append(med)
            pergunta = input('Deseja adicionar outro medicamento [S/N]? ').strip().lower()
        else: #OPÇÕES INVÁLIDAS (DIFERENTES DE Nn OU Ss)
            print('\n{:*^50}'.format(' ATENÇÃO! '))
            print('{:^50}'.format(' Opção INVÁLIDA. Tente novamente '))
            print('*'*50)
            pergunta = input('\nDeseja adicionar outro medicamento [S/N]? ').strip().lower()
    consulta[chave] = {
        'Diagnóstico': dig,
        'Medicamento': medicamentos
        }

#====================================================================
#[ 3 ][ 5 ]
#Função para excluir uma consulta já cadastrada de acordo com sua chave (tupla)
def del_consulta(chave, consultas):
    del consultas[chave]
    print('\nConsulta removida com sucesso!')

#====================================================================
#[ 4 ]
#Função para apresentar o submenu de relatórios para o usuário
def menu_relatorio():
    print('\n{:=^50}'.format(' SUBMENU - RELATÓRIOS '))
    print('''\n[ A ] Listar médicos por especialidade
[ B ] Listar pacientes por idade
[ C ] Listar consultas realizadas nos últimos dias\n''')
    print('='*50)

#====================================================================
#[ 4 ][ A ]
#Função para imprimir o relatório dos médicos de acordo com uma especialidade
def listar_esp(especialidade, medicos): 
    print('\n{:=^50}'.format(' LISTAR MÉDICOS - ESPECIALIDADE '))
    print('\n{:^50}'.format(especialidade).upper())
    registro = False
    for crm in medicos.keys():
        if medicos[crm]['Especialidade'] == especialidade:
            print('\nNome: {}'.format(medicos[crm]['Nome']))
            print('CRM: {}'.format(crm))
            print('Data de Nascimento: {}'.format(medicos[crm]['Nascimento']))
            print('Sexo: {}'.format(medicos[crm]['Sexo']))
            print('Especialidade: {}'.format(medicos[crm]['Especialidade']))
            print('Formado(a) na: {}'.format(medicos[crm]['Universidade']))
            print('E-mail(s):')
            for i in medicos[crm]['E-mail']:
                print('\t{}'.format(i))
            print('Telefone(s):')
            for j in medicos[crm]['Telefones']:
                print('\t{}'.format(j))
            print()
            print('-'*50)
            registro = True
    if not registro:
        print('\nEspecialidade não encontrada!')

#====================================================================
#[ 4 ][ B ] - com biblioteca
#Função para imprimir o relatório dos pacientes menores que uma idade 
def calcula_idade(idade, pacientes):
    print('\n{:=^50}'.format(' LISTAR PACIENTES - IDADE MÁXIMA '))
    print('\n{:^50}'.format(idade))
    from datetime import date
    from datetime import datetime
    encontrado = False
    for nasc in pacientes:
        str_date = (pacientes[nasc]['Nascimento'])
        date = datetime.strptime(str_date, '%d/%m/%Y').date()
        today = date.today()
        idade1 = (today.year) - (date.year) - ((today.month, today.day) < (date.month, date.day))      
        if idade1 <= idade:
            print('\nNome: {}'.format(pacientes[nasc]['Nome']))
            print('CPF: {}'.format(nasc))
            print('Data de Nascimento: {}'.format(pacientes[nasc]['Nascimento']))
            print('Idade: {} anos'.format(idade1))
            print('Sexo: {}'.format(pacientes[nasc]['Sexo']))
            print('Plano: {}'.format(pacientes[nasc]['Plano']))
            print('E-mail(s):')
            for i in pacientes[nasc]['E-mail']:
                print('\t{}'.format(i))
            print('Telefone(s):')
            for j in pacientes[nasc]['Telefones']:
                print('\t{}'.format(j))
            print()
            print('-'*50)
            encontrado = True
    if not encontrado:
        print('\nOs pacientes registrados são maiores que {} anos'.format(idade))    

#====================================================================
#[ 4 ][ C ]
#Função para imprimir as consultas de X dias atrás
def calcula_data(dias,consultas,chave, medicos, pacientes):
    from datetime import date
    from datetime import datetime
    encontrado = False
    for chave in consultas:
        string_data = (chave[2])
        data_lista = datetime.strptime(string_data, '%d/%m/%Y').date()
        data_lista = ((date.today()) - data_lista)
        resultado = (data_lista).days
        if resultado <= dias:
            print()
            print('A consulta foi há {} dias'.format(resultado))
            print('Médico: {}'.format(medicos[chave[0]]['Nome']))
            print('CRM: {}'.format(chave[0]))
            print('Paciente: {}'.format(pacientes[chave[1]]['Nome']))
            print('CPF: {}'.format(chave[1]))
            print('Data: {}'.format(chave[2]))
            print('Horário: {}'.format(chave[3]))
            print('Diagnóstico: {}'.format(consultas[chave]['Diagnóstico']))
            print('Medicamento(s):')
            for j in consultas[chave]['Medicamento']:
                print('\t{}'.format(j))
            print()
            print('-'*50)
            encontrado = True
    if not encontrado:
        print('\nAs consultas são mais recentes que a data informada.')    
       
#====================================================================
#Função principal
def main():
    MEDICOS = {'000': {'Nome': 'João Mateus Marão Domingues', 'Nascimento': '25/02/1993', 'Sexo': 'M', 'Especialidade': 'Gastro',
	'Universidade': 'UFPEL', 'E-mail': ['jmmarao@gmail.com', 'joao.mateus-@hotmail.com', 'joao.wee@hotmail.com'],
	'Telefones': ['(17)3421-4149', '(16)98212-7253', '(53)98210-0000']},
        '111': {'Nome': 'Maria Joaquina Silveira', 'Nascimento': '01/09/1979', 'Sexo': 'F', 'Especialidade': 'Neuro',
	'Universidade': 'UFSCAR', 'E-mail': ['maria.joaquina@yahoo.com', 'mariajoaq@cade.com', 'joaquina@ifsp.com.br'],
	'Telefones': ['(18)3568-0139', '(18)97214-3243', '(18)98234-1111']},
        '222': {'Nome': 'Januário Mercules da Silva', 'Nascimento': '01/05/1989', 'Sexo': 'F', 'Especialidade': 'Gastro',
	'Universidade': 'IFSP', 'E-mail': ['januario@gmail.com', 'januario.mercules@hotmail.com'],
	'Telefones': ['(16)3521-5659']}} #DICIONÁRIO DE MÉDICOS
    PACIENTES = {'01':{'Nome': 'José Pereira Bibiano', 'Nascimento':'01/10/1990', 'Sexo': 'M', 'Plano': 'SUS',
                'E-mail':['bibiano@bol.com.br', 'josebibi@ig.com.br'], 'Telefones':['(18)98201-0022']},
                '02':{'Nome': 'Murilo Sampaio Barreto', 'Nascimento':'10/01/1980', 'Sexo': 'M', 'Plano': 'BEM VIVER',
               'E-mail':['pedro@sampaio', 'mumu@terra.com.br'], 'Telefones':['(53)99810-2321', '(55)99789-1135']},
                '03':{'Nome': 'Jéssica Lima Duarte', 'Nascimento':'01/09/1978', 'Sexo': 'F', 'Plano': 'VIVA',
               'E-mail':['acabou@jessica'], 'Telefones':['(21)98354-7489', '(16)98712-5698']}}#DICIONÁRIO DE PACIENTES
    CHAVE_CONS = ()
    CONSULTAS = {('000', '01', '06/08/2020', '13:40'): {'Diagnóstico': 'Enxaqueca', 'Medicamento': ['Repouso', 'Analgésico', 'Sono']},
                ('111', '03', '10/06/2020', '14:30'): {'Diagnóstico': 'Miopia', 'Medicamento': ['Óculos', 'Sol']},
                ('222', '02', '30/05/2020', '15:00'): {'Diagnóstico': 'Dor de cabeça','Medicamento': ['Isolamento', 'Anti-gripal', 'Paracetamol']}}#DICIONÁRIO DE PACIENTES
    
    menu()
    opcao = input('Opção desejada: ').strip()
    while opcao != '5':
        
#====================================================================
#SUBMENU - MÉDICOS        
        if opcao == '1': 
            menu_medico()
            opcao1 = input('Opção desejada: ').strip()
            if opcao1 == '1':
                listar_medicos(MEDICOS)
            elif opcao1 == '2':
                print('\n{:=^50}'.format(' LISTAR MÉDICOS - CRM '))
                CRM_listar = input('\nDeseja listar o cadastro de qual CRM [incluir pontuação]? ').strip()
                verif = buscar_crm(CRM_listar, MEDICOS) #Verificador de CRM
                if verif != -1:
                    listar_crm(CRM_listar, MEDICOS)
                else:
                    print('\nCRM {} não encontrado!'.format(CRM_listar))
            elif opcao1 == '3':
                print('\n{:=^50}'.format(' INCLUIR MÉDICO '))
                CRM = input('\nCRM [incluir pontuação]: ').strip()
                verif = buscar_crm(CRM, MEDICOS)
                while verif != -1: #Loop para CRM repetido
                    print('\n{:*^50}'.format(' ATENÇÃO! '))
                    print('{:^50}'.format(' CRM EXISTENTE! Tente novamente '))
                    print('*'*50)
                    CRM = input('\nCRM [incluir pontuação]: ').strip()
                    verif = buscar_crm(CRM, MEDICOS)
                incluir_medico(CRM, MEDICOS)
                print('\nMédico registrado com sucesso!')
            elif opcao1 == '4':
                print('\n{:=^50}'.format(' ALTERAR CADASTRO - CRM '))
                CRM_alt = input('\nDeseja alterar o cadastro de qual CRM [incluir pontuação]? ').strip()
                verif = buscar_crm(CRM_alt, MEDICOS)
                if verif != -1:
                    incluir_medico(CRM_alt, MEDICOS)
                    print('\nMédico alterado com sucesso!')
                else:
                    print('\nCRM {} não encontrado!'.format(CRM_alt))                
            elif opcao1 == '5':
                print('\n{:=^50}'.format(' EXCLUIR MÉDICO - CRM '))
                CRM_del = input('\nDeseja excluir o cadastro de qual CRM [incluir pontuação]? ').strip()
                verif = buscar_crm(CRM_del, MEDICOS)
                if verif != -1:
                    del_medico(CRM_del, MEDICOS)
                else:
                    print('\nCRM {} não encontrado!'.format(CRM_del))                    
            else: #OPÇÕES INVÁLIDAS - SUBMENU DE MÉDICOS (< 1 e > 5) 
                print('\n{:*^50}'.format(' ATENÇÃO! '))
                print('{:^50}'.format(' Opção INVÁLIDA. Tente novamente '))
                print('*'*50)
                
#====================================================================
#SUBMENU - PACIENTES  
        elif opcao == '2':
            menu_paciente()
            opcao2 = input('Opção desejada: ').strip()
            if opcao2 == '1':
                listar_pacientes(PACIENTES)
            elif opcao2 == '2':
                print('\n{:=^50}'.format(' LISTAR PACIENTES - CPF '))
                CPF_listar = input('\nDeseja listar o cadastro de qual CPF [incluir pontuação]? ').strip()
                verif = buscar_cpf(CPF_listar, PACIENTES)
                if verif != -1:
                    listar_cpf(CPF_listar, PACIENTES)
                else:
                    print('\nCPF {} não encontrado!'.format(CPF_listar))                        
            elif opcao2 == '3':
                    print('\n{:=^50}'.format(' INCLUIR PACIENTE '))
                    CPF = input('\nCPF [incluir pontuação]: ').strip()
                    verif = buscar_cpf(CPF, PACIENTES)
                    while verif != -1: #Loop para CPF repetido
                        print('\n{:*^50}'.format(' ATENÇÃO! '))
                        print('{:^50}'.format(' CPF EXISTENTE! Tente novamente '))
                        print('*'*50)
                        CPF = input('\nCPF [incluir pontuação]: ').strip()
                        verif = buscar_cpf(CPF, PACIENTES)
                    incluir_paciente(CPF, PACIENTES)
                    print('\nPaciente registrado com sucesso!')
            elif opcao2 == '4':
                print('\n{:=^50}'.format(' ALTERAR CADASTRO - CPF '))
                CPF_alt = input('\nDeseja alterar o cadastro de qual CPF [incluir pontuação]? ').strip()
                verif = buscar_cpf(CPF_alt, PACIENTES)
                if verif != -1:
                    incluir_paciente(CPF_alt, PACIENTES)
                    print('\nPaciente alterado com sucesso!')
                else:
                    print('\nCPF {} não encontrado!'.format(CPF_alt))
            elif opcao2 == '5':
                print('\n{:=^50}'.format(' EXCLUIR PACIENTE - CPF '))
                CPF_del = input('\nDeseja excluir o cadastro de qual CPF [incluir pontuação]? ').strip()
                verif = buscar_cpf(CPF_del, PACIENTES)
                if verif != -1:
                    del_paciente(CPF_del, PACIENTES)
                else:
                    print('\nCPF {} não encontrado!'.format(CPF_del))
            else: #OPÇÕES INVÁLIDAS - SUBMENU DE PACIENTES (< 1 e > 5) 
                print('\n{:*^50}'.format(' ATENÇÃO! '))
                print('{:^50}'.format(' Opção INVÁLIDA. Tente novamente '))
                print('*'*50)

#====================================================================
#SUBMENU - CONSULTAS                  
        elif opcao == '3':
            menu_consulta()
            opcao3 = input('Opção desejada: ').strip()
            if opcao3 == '1':
                listar_consultas(CONSULTAS, MEDICOS, PACIENTES)
            elif opcao3 == '2':
                print('\n{:=^50}'.format(' LISTAR CONSULTAS - ELEMENTOS '))
                print('{:^50}'.format(' CRM, CPF, Data e Horário '))
                CHAVE_CONS_listar = criar_chave(MEDICOS, PACIENTES, CONSULTAS, CHAVE_CONS)
                verif = buscar_chave(CHAVE_CONS_listar, CONSULTAS)
                if verif != -1:
                    listar_chave(CHAVE_CONS_listar, CONSULTAS, MEDICOS, PACIENTES)
                else:
                    print('Consulta não encontrada!') #TENTAR FORMATAR - PERFUMARIA
            elif opcao3 == '3':
                print('\n{:=^50}'.format(' INCLUIR CONSULTA '))                
                CHAVE_CONS = criar_chave(MEDICOS, PACIENTES, CONSULTAS, CHAVE_CONS)
                verif = buscar_chave(CHAVE_CONS, CONSULTAS)
                while verif != -1: #Loop para chave repetida
                    print('\n{:*^50}'.format(' ATENÇÃO! '))
                    print('{:^50}'.format(' Horário Indisponível '))
                    print('{:^50}'.format(' ESTA CONSULTA JÁ ESTAVA AGENDADA! Tente novamente '))
                    print('*'*50)
                    main()
                incluir_consulta(CHAVE_CONS, CONSULTAS)                
                print('\nConsulta registrada com sucesso!')

            elif opcao3 == '4':
                print('\n{:=^50}'.format(' ALTERAR CONSULTA - ELEMENTOS '))
                print('{:^50}'.format(' CRM, CPF, Data e Horário '))
                CHAVE_CONS_alt = criar_chave(MEDICOS, PACIENTES, CONSULTAS, CHAVE_CONS)
                verif = buscar_chave(CHAVE_CONS_alt, CONSULTAS)
                if verif != -1:
                    incluir_consulta(CHAVE_CONS_alt, CONSULTAS)
                    print('\nConsulta alterada com sucesso!')
                else:
                    print('Consulta não encontrada!') #TENTAR FORMATAR - PERFUMARIA                
            elif opcao3 == '5':
                print('\n{:=^50}'.format(' ALTERAR CONSULTA - ELEMENTOS '))
                print('{:^50}'.format(' CRM, CPF, Data e Horário '))
                CHAVE_CONS_del = criar_chave(MEDICOS, PACIENTES, CONSULTAS, CHAVE_CONS)
                verif = buscar_chave(CHAVE_CONS_del, CONSULTAS)
                if verif != -1:
                    del_consulta(CHAVE_CONS_del, CONSULTAS)
                else:
                    print('Consulta não encontrada!') #TENTAR FORMATAR - PERFUMARIA
            else: #OPÇÕES INVÁLIDAS - SUBMENU DE CONSULTAS ( < 1 e > 5 ) 
                print('\n{:*^50}'.format(' ATENÇÃO! '))
                print('{:^50}'.format(' Opção INVÁLIDA. Tente novamente '))
                print('*'*50)

#====================================================================
#SUBMENU - RELATÓRIOS     
        elif opcao == '4':
            menu_relatorio()
            opcao4 = input('Opção desejada: ').strip().lower()
            if opcao4 == 'a':                
                ESP = input('\nDeseja listar os médicos de qual especialidade? ').strip().capitalize()
                listar_esp(ESP, MEDICOS)
            elif opcao4 == 'b':
                IDADE = int(input('\nDeseja listar os pacientes até que idade? '))
                calcula_idade(IDADE, PACIENTES)
            elif opcao4 == 'c':
                DIAS = int(input('\nDeseja listar as consultas de quantos dias atrás? '))
                calcula_data(DIAS, CONSULTAS, CHAVE_CONS, MEDICOS, PACIENTES)
            else: #OPÇÕES INVÁLIDAS - SUBMENU DE RELATÓRIOS ( DIFERENTES DE A, B E C ) 
                print('\n{:*^50}'.format(' ATENÇÃO! '))
                print('{:^50}'.format(' Opção INVÁLIDA. Tente novamente '))
                print('*'*50)

                
        
        else: #OPÇÕES INVÁLIDAS - MENU DE OPÇÕES (< 1 e > 5)
            print('\n{:*^50}'.format(' ATENÇÃO! '))
            print('{:^50}'.format(' Opção INVÁLIDA. Tente novamente'))
            print('*'*50)
            
        menu()
        opcao = input('Opção desejada: ').strip()

    if opcao == '5':
        print('\nPrograma ENCERRADO. Até logo!\n')

#====================================================================
#                   ***PROGRAMA PRINCIPAL***
print('{:_^50}'.format(' HOSPITAL '))
main()



'''
#====================================================================
#           SOLUÇÕES ALTERNATIVAS - RELATÓRIO 4/B E 4/C

#====================================================================
#           *** SOLUÇÃO ALTERNATIVA - SEM USO DE BIBLIOTECA***
#====================================================================
#Chamada da função: listar_idade(IDADE, PACIENTES)

#[ 4 ][ B ] - sem biblioteca
#Função para imprimir o relatório dos pacientes menores que uma idade
def listar_idade(idade, pacientes):
    print('\n{:=^50}'.format(' LISTAR PACIENTES - IDADE MÁXIMA '))
    print('\n{:^50}'.format(idade))
    registro = False
    for cpf in pacientes.keys():
        nasc = pacientes[cpf]['Nascimento']
        ano_str = nasc.rfind('/')+1 #RFIND PROCURA A ÚLTIMA BARRA, E +1 A RETIRA DA STRING
        ano_nasc = int(nasc[ano_str:])
        anos = 2020-ano_nasc #CALCULA A IDADE DE CADA PACIENTE EM RELAÇÃO AO ANO DE 2020, CONSIDERANDO APENAS O ANO DE NASCIMENTO
        if anos <= idade:
            print('\nNome: {}'.format(pacientes[cpf]['Nome']))
            print('CPF: {}'.format(cpf))
            print('Data de Nascimento: {}'.format(pacientes[cpf]['Nascimento']))
            print('Idade: {} anos'.format(anos))
            print('Sexo: {}'.format(pacientes[cpf]['Sexo']))
            print('Plano de saude: {}'.format(pacientes[cpf]['Plano']))
            print('E-mail(s):')
            for i in pacientes[cpf]['E-mail']:
                print('\t{}'.format(i))
            print('Telefone(s):')
            for j in pacientes[cpf]['Telefones']:
                print('\t{}'.format(j))
            print()
            print('-'*50)
            registro = True
    if not registro:
        print('\nOs pacientes registrados são maiores que {} anos'.format(idade))


#====================================================================
#           *** SOLUÇÃO ALTERNATIVA - SEM USO DE BIBLIOTECA***
#====================================================================
#Chamada da função: listar_dias(DIAS, CONSULTAS, CHAVE_CONS, MEDICOS, PACIENTES)
#[ 4 ][ C ]
#Função para imprimir as consultas de X dias atrás
#Com a intenção de evitar o uso de bibliotecas, optou-se o uso de dias julianos (def dia_juliano, função mais abaixo)
#OBS1: a data de entrega do projeto será adotada como a data atual (D = 10; M = 08; A = 2020; DJ = 2459072)
#OBS2: quanto menor o DJ, mais antiga é a data (mais longe)
def listar_dias(dia, consultas, chave, medicos, pacientes):
    dia_atual = 10
    mes_atual = 8
    ano_atual = 2020 
    DJ_atual = dia_juliano(dia_atual, mes_atual, ano_atual)
    DJ_max = DJ_atual - dia #DATA DE CORTE, AS CONSULTAS PODEM IR ATÉ ESSE DIA (MENOR OU IGUAL A ESTE VALOR)
    registro = False
    for chave in consultas.keys():
        data = chave[2]
        ano_str = data.rfind('/') + 1 #RFIND PROCURA A ÚLTIMA BARRA, E +1 A RETIRA DA STRING
        ano_cons = int(data[ano_str:])
        dia_str = data.find('/')#FIND PROCURA A PRIMEIRA BARRA, NESTE CASO NÃO É NECESSÁRIO SOMAR +1
        dia_cons = int(data[:dia_str])
        mes_cons = int(data[dia_str + 1:ano_str - 1]) #+1 PARA RETIRAR A PRIMEIRA / E -1 PARA TIRAR A ÚLTIMA
        DJ_cons = dia_juliano(dia_cons, mes_cons, ano_cons)
        if DJ_max <= DJ_cons:
            print(chave)
            print('\nMédico: {}'.format(medicos[chave[0]]['Nome']))
            print('nCRM: {}'.format(chave[0]))
            print('Paciente: {}'.format(pacientes[chave[1]]['Nome']))
            print('CPF: {}'.format(chave[1]))
            print('Data: {}'.format(chave[2]))
            print('Horário: {}'.format(chave[3]))
            print('Diagnóstico: {}'.format(consultas[chave]['Diagnóstico']))
            print('Medicamento(s):')
            for j in consultas[chave]['Medicamento']:
                print('\t{}'.format(j))
            print()
            print('-'*50)
            registro = True
    if not registro:
        print('\nAs consultas são mais recentes que {} dias atrás'.format(dia))
#====================================================================
        
#Para realizar operações entre as datas será utilizado o cálculo dos dias julianos
#Os dias julianos é um método para contar os dias sequencialmente.
#São muito úteis porque facilitam a operação entre dias.
#Tais operações são mais difíceis no calendário padrão (gregoriano), pois são
#agrupados em meses, podem conter um número variável de dias, além das complicações
#dos anos bissextos.        
#DJ = D - 32075 + 1461*( A + 4800 + ( M - 14 ) / 12 ) / 4 + 367*( M - 2 - ( M - 14 ) / 12 * 12 ) / 12 - 3*( ( A + 4900 + ( M - 14 ) / 12 ) / 100 ) / 4
#DJ: dia juliano; A: ano; M: mês; D: dia
#Exemplo: 01/01/1970 tem DJ = 2440588
#OBS: esta fórmula é válida apenas entre os anos 1801 e 2099
def dia_juliano(D, M, A):
    DJ = D - 32075 + 1461*( A + 4800 + ( M - 14 ) / 12 ) / 4 + 367*( M - 2 - ( M - 14 ) / 12 * 12 ) / 12 - 3*( ( A + 4900 + ( M - 14 ) / 12 ) / 100 ) / 4
    return int(DJ)


'''
