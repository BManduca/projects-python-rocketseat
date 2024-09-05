nome_completo = 'Brunno Manduca'

nome_completo_aspas = """Brunno
Manduca"""

nome_completo_quebra = 'Brunno \
Manduca'

nome = 'Brunno'
sobrenome = 'Manduca'

print('1a forma - Nome completo:', nome_completo)
print('2a forma - Nome completo: ' + nome_completo)
print('3a forma - Nome completo: ' + 'Brunno' + ' Manduca')
print('4a forma - Nome completo: ' + 'Brunno','Manduca')
print('5a forma - Nome completo:', nome_completo_aspas)
print('6a forma - Nome completo:', nome_completo_quebra)
print('7a forma - Nome completo: %s' % nome_completo)
print('8a forma - Nome completo: %s %s' % (nome, sobrenome))
print('9a forma - Nome completo: {} {}'.format(nome, sobrenome))
print(f'10a forma - Nome completo: {nome} {sobrenome}')

print(' ')
# UPPERCASE

print('Nome completo utilizando método Uppercase => {}'.format(nome_completo.upper()))

# LOWERCASE

print('Nome completo utilizando método Lowercase => {}'.format(nome_completo.lower()))

# Count
print('Número de ocorrências da letra n dentro do nome {}: {}'.format(nome_completo, nome_completo.count('n')))

# find()
print('Posição da primeira letra n dentro do nome {}: {}'.format(nome_completo, nome_completo.find('n')))

# Join()
print('Aplicando método join() no nome {}: {}'.format(nome, '-'.join(nome)))

# Split()
print('Aplicando método split() no nome {}: {}'.format(nome_completo, nome_completo.split()))

# Strip()
print(' ')
nome_test = 'xBrunnox'
print('Nome sem aplicação do método strip(): {}'.format(nome_test))
print('Nome com aplicando método strip(): {}'.format(nome_test.strip('x')))