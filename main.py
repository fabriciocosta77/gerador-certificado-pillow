from PIL import Image, ImageDraw, ImageFont

def centralizar(texto: str, fonte: ImageFont.ImageFont, tamanho_linha: int):
    #Função responsável por cortar as linhas da variável texto (linha 26)
    linhas = ['']
    for palavra in texto.split():
        linha = f'{linhas[-1]} {palavra}'.strip()

        #Retorna o tamanho da linha EM PÍXEIS (checar linha 30)
        if fonte.getlength(linha) <= tamanho_linha:
            linhas[-1] = linha
        else:
            linhas.append(palavra)

    return '\n'.join(linhas)

def __main__(nomes, nome_curso, caminho_fonte, hora, data_dia, data_mes, data_ano):
    # Para cada nome, irá gerar um certificado diferente
    for nome in nomes:
        imagem = Image.open("imagens/uso/modelo.png", mode='r')
        fonte_texto = ImageFont.truetype(caminho_fonte, 36)
        fonte_data = ImageFont.truetype(caminho_fonte, 48)

        inserir_texto = ImageDraw.Draw(imagem)
        inserir_data = ImageDraw.Draw(imagem)

        texto = str(f"Certificamos que o(a) aluno(a) {nome} concluiu o curso {nome_curso}, com carga horária de {hora} horas.")
        data = str(f"{data_dia} de {data_mes} de {data_ano}")

        texto = centralizar(texto, fonte_texto, 1200)

        # Pega as coordenadas verticais e horizontais da imagem modelo para inserir o texto
        inserir_texto.text((200, 340), texto, fill=(0, 0, 0), font=fonte_texto, align="center")
        inserir_data.text((995, 930), data, fill=(0, 0, 0), font=fonte_data, align="center")

        imagem.show
        imagem.save(f"imagens/{nome}.png")

if __name__ == '__main__':
    nomes = []
    
    nome_curso = input("Insira o nome completo do curso: ")
    hora = input("Insira a quantidade de horas do curso: ")
    data_dia = str(input("Insira o dia de conclusão de curso dos alunos: "))
    data_mes = str(input("Insira o nome do mês de conclusão de curso dos alunos: "))
    data_ano = str(input("Insira o ano de conclusão de curso dos alunos: "))

    nomes.append(input("Insira o nome completo da pessoa que irá receber o certificado: "))
    continuar = input("Deseja inserir mais um aluno? (Y/N) ")

    while (continuar == "Y"):
        nomes.append(input("Insira o nome da pessoa que irá receber o certificado: "))
        continuar = input("Deseja inserir mais um nome? (Y/N) ")

    fonte = "fontes/Arial.ttf"
    certificado = "imagens/uso/modelo.png"

    __main__(nomes, nome_curso, fonte, hora, data_dia, data_mes, data_ano)