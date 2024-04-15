from PIL import Image, ImageDraw, ImageFont

def __main__(nomes, certificado, caminho_fonte, hora, data_atual):
    for nome in nomes:
        imagem = Image.open(certificado, mode='r')
        fonte = ImageFont.truetype(caminho_fonte, 20)

        inserir_nome = ImageDraw.Draw(imagem)
        inserir_data = ImageDraw.Draw(imagem)
        inserir_horas = ImageDraw.Draw(imagem)

        inserir_nome.text((440, 384), nome, fill=(0, 0, 0), font=fonte)
        inserir_data.text((150, 450), data_atual, fill=(0, 0, 0), font=fonte)
        inserir_horas.text((340, 420), hora, fill=(0, 0, 0), font=fonte)

        imagem.show
        imagem.save(f"{nome}.png")

if __name__ == "__main__":
    nomes = []
    hora = input("Insira a quantidade de horas do curso.")
    data_atual = str(input("Insira a data de hoje. (Dia/Mês/Ano)"))

    nomes.append(input("Insira o nome da pessoa que irá receber o certificado."))
    continuar = input("Deseja inserir mais um aluno? (Y/N)")

    while (continuar == "Y"):
        nomes.append(input("Insira o nome da pessoa que irá receber o certificado."))
        continuar = input("Deseja inserir mais um nome? (Y/N)")

    fonte = "fontes/Consolas.ttf"
    certificado = "imagens/uso/modelo.png"

    __main__(nomes, certificado, fonte, hora, data_atual)



        