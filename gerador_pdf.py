from fpdf import FPDF 
#!pip install fpdf - para instalar a biblioteca do pdf

#inputs para pegar os valores digitados pelo usuário
empresa = input('Informe a empresa: ')
acesso = (input('Quantos acessos?: '))
visita = (input('Quantas visitas?: '))

#condição para verficar se o usuário digitou número apenas
if not acesso.isdigit() or not visita.isdigit():
    print('Voce nao digitou nenhum valor válido, insira apenas número')
    
# se ele digitou números, então as variáveis recebe o tipo INT
else:
    acesso = int(acesso)
    visita = int(visita)
    
#valores do serviços ja, pré definidos
acesso_valor = 50
visita_valor = 120

#calculo do valor inserido do usuário e o valor pré definidos
valor_total_acesso = acesso * acesso_valor
valor_total_visita = visita * visita_valor

#somando os dois valores e colocando na variável valor_total
valor_total = int(valor_total_acesso) + int(valor_total_visita)

#informações de todo o calculos na tela para o usuário verificar
print(f'O valor total do acesso é?:  {valor_total_acesso}')
print(f'O valor total da visita é? {valor_total_visita}')
print(f'O valor total ficou em {valor_total}')
  
#comando para pré definir o pdf  
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

#utilizando um template
pdf.image("template2.png", x=0, y=0 )

# inserindo os dados do orçamento no pdf
pdf.text(115, 145, str(empresa))
pdf.text(115, 160, str(acesso))
pdf.text(115, 175, str(visita))
pdf.text(115, 205, str(valor_total))

#mensagem de sucesso caso a geração do PDF de certo.
pdf.output("Ordem de Serviços.pdf")
print('Ordem Gerado com sucesso!')

