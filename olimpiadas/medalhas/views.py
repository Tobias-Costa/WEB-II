from django.shortcuts import render
from django.http import HttpResponse

class Pais:
    def __init__(self, posicao, nome_pais, ouro, prata, bronze, img_link):
        self.posicao = posicao
        self.nome_pais = nome_pais
        self.ouro = ouro
        self.prata = prata
        self.bronze = bronze
        self.img_link = img_link
        self.atletas = []
            
eua = Pais('1', 'Estados Unidos','27', '35', '33', 'data:image/png;base64,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' )
china = Pais('2', 'China', '29', '25', '19',  'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAAAEZ0FNQQAAsY58+1GTAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAAOxAAADsQBlSsOGwAABIxJREFUeNrtWU2IHEUU/rq6Z3t6ev+i5mBEYfWg6MGfxJMahZCDINkg5iIEgoIHD7okoODVk4KLC7mpt4ABf5LsQfAP0Ry8rBgPQry40Whi2GTdyezs/PR0P6t7emd6Zru6q7p7XIUtpqamq6urvvfe997rqgF2yk7JVbS4zuXl5VneHOd1H6+Vbca4wesSr/MzMzPnUgXg4N/izWv/UYW/zYV4XShAqPmzIM/VF0+3tPNfMNRr5eAmUXdQ2PSuNzvCa6LB6y0thvvDr+BD/evNMbbdxIFDnvfcMROM6bz3cNQSxpCEPm3Azpxq0eKHlc0lg4lGJkDK8xvrZZx+D1qnU6fnX7JDjD0B2JAA+4Lvbz7rW6a38PYW+vxTNoBRIEDXYWtVK1578kWfJuiTHuzHnGIkuLlmDWAUUGgr4IHfkT5fdE+8nreuYc+7NXh1Dc4VhvavLIveU0cwoQBR3sfMNfl0K5H/pTtcNH400L6ko3ONxU8isixJjhMKkKQIPhkbJ0wdaQatqLR/07H6voWbZ0xuBTmAlIGqTAg4WocWsvY60MYI1iNOqn84V/tLTB9pwX6cP6sX59yGzKCxu1wwu094+4l2t93fhruihaGbAr63L7FYLY8/1cbkoRaaP+uonzdGLMDQ4j4Fdh1rwrzXHTBJ+f5OUP3xrV90XD9ZEc61/l0J5n0dNC7o0HcR3NV/0QKd6wzX3rQx9WwTU4dbIfFCQbhM1bMmqp+UQW5C2OUG/PtUGV4NcgkwNmNLOzFtrRxA9eMy16AxMHnjJx1rH0XAx1qSeqG16CIfnDkYbcxD+YFO1yp/aSGN3MChZUKecauLvAlSPQ9E8oH1IAevEQ+PZfw5N4HVD6zg2nrISUiA3da8p4Ppo03YT7Zh7PaGlkuhT14f2FzEuN3F1TdsOH9042DtyxKaFxkqezuJ4AP6NDVUHnXAuLXq35bUtE+KAogSSvWcGbpE/75zWUf1MksEH4RYzv+VdypdupGE9ouMQn1ayaZ86u40eFO604XzO4O7pqGxZMhzPyX6KOUBqftDGjRu83DLi40geq3MW6B2gqVltC/AxNQsQPFajwPAKHBWNuFh7G5X7b1HUvvZLRA7ZpDz7g2GKyfGYT3soHVRF4PPoX01HxBOJHizdMJE94MhTTtV7eezQNq7vWBTRElJLKlPgEnBApImThAkHjyJl8qeyCgbnfKAT6LOaH0gfQuYCbzk+1KBUShB6zLg03if2wdILcwpgyeoOXf+KCQBXBV8BgzF+IAK8CTwCdTxz021oi1AUubOD74wC5CSH0gClwBPUPQByuED8YkpResy4EcahWSA5wE/mnehhIydBDwL+GIycZZNjkLGzgA+bkOzETwzPtEQH5DKbHIktK4InuyJjShGkQBLweADz3hSxy2i8zDhji1ZEKHm/UOBg7MUxSii0Dyv+7WjL5uOhzq+XvT/5LOUWUXDWTfleiDaRM+FePXZcHDWK73wihnB2Cv/+79Zt5zULywsfDU3N3eB/9zD625eS9sM2uf897y+ysGfxE7ZKcWWfwD+3GAGa5kRpwAAAABJRU5ErkJggg==')
australia = Pais('3', 'Austrália', '18', '14', '13', 'data:image/png;base64,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')
brasil = Pais('19', 'Brasil', '2', '5', '8', 'https://ssl.gstatic.com/onebox/media/sports/logos/zKLzoJVYz0bb6oAnPUdwWQ_48x48.png')
lista_paises = [eua, china, australia, brasil]


class Atletas:
    def __init__(self, atleta_nome, modalidade, medalha):

        self.atleta_nome = atleta_nome
        self.modalidade = modalidade
        self.medalha = medalha
    
    def __str__(self):
        return self.atleta_nome
    
def procura_instancia_pais(pais_escolhido):
    for pais in lista_paises:
        if pais_escolhido == pais.nome_pais:
            return pais
### EUA
eua.atletas.append(Atletas('Simone Biles', 'Ginástica', 'Ouro'))
eua.atletas.append(Atletas('Caeleb Dressel', 'Natação', 'Ouro'))
eua.atletas.append(Atletas('Katie Ledecky', 'Natação', 'Prata'))
eua.atletas.append(Atletas('Ryan Murphy', 'Natação', 'Bronze'))
eua.atletas.append(Atletas('Sydney McLaughlin', 'Atletismo', 'Ouro'))
eua.atletas.append(Atletas('Noah Lyles', 'Atletismo', 'Ouro'))
eua.atletas.append(Atletas('Gabby Thomas', 'Atletismo', 'Prata'))
eua.atletas.append(Atletas('Michael Andrew', 'Natação', 'Bronze'))
eua.atletas.append(Atletas('MyKayla Skinner', 'Ginástica', 'Prata'))
eua.atletas.append(Atletas('Zach Apple', 'Natação', 'Ouro'))
eua.atletas.append(Atletas('Dalilah Muhammad', 'Atletismo', 'Prata'))
eua.atletas.append(Atletas('Tamyra Mensah-Stock', 'Luta', 'Ouro'))
eua.atletas.append(Atletas('David Taylor', 'Luta', 'Ouro'))
eua.atletas.append(Atletas('Athing Mu', 'Atletismo', 'Ouro'))
eua.atletas.append(Atletas('Erriyon Knighton', 'Atletismo', 'Bronze'))

### China
china.atletas.append(Atletas('Zhang Yufei', 'Natação', 'Ouro'))
china.atletas.append(Atletas('Chen Yuxi', 'Mergulho', 'Ouro'))
china.atletas.append(Atletas('Liu Yang', 'Ginástica', 'Prata'))
china.atletas.append(Atletas('Shi Tingmao', 'Mergulho', 'Bronze'))
china.atletas.append(Atletas('Sun Yang', 'Natação', 'Ouro'))
china.atletas.append(Atletas('Guan Chenchen', 'Ginástica', 'Ouro'))
china.atletas.append(Atletas('Ma Long', 'Tênis de Mesa', 'Ouro'))
china.atletas.append(Atletas('Xu Xin', 'Tênis de Mesa', 'Prata'))
china.atletas.append(Atletas('Yang Qian', 'Tiro Esportivo', 'Ouro'))
china.atletas.append(Atletas('Zhu Xueying', 'Ginástica', 'Ouro'))
china.atletas.append(Atletas('Lu Xiaojun', 'Halterofilismo', 'Ouro'))
china.atletas.append(Atletas('Liao Qiuyun', 'Halterofilismo', 'Prata'))
china.atletas.append(Atletas('Wang Shun', 'Natação', 'Ouro'))
china.atletas.append(Atletas('Chen Meng', 'Tênis de Mesa', 'Ouro'))
china.atletas.append(Atletas('Wang Lijun', 'Boxe', 'Bronze'))

### Austrália
australia.atletas.append(Atletas('Emma McKeon', 'Natação', 'Ouro'))
australia.atletas.append(Atletas('Ariarne Titmus', 'Natação', 'Ouro'))
australia.atletas.append(Atletas('Kyle Chalmers', 'Natação', 'Prata'))
australia.atletas.append(Atletas('Ashleigh Gentle', 'Triatlo', 'Bronze'))
australia.atletas.append(Atletas('Kaylee McKeown', 'Natação', 'Ouro'))
australia.atletas.append(Atletas('Rohan Dennis', 'Ciclismo', 'Ouro'))
australia.atletas.append(Atletas('Jess Fox', 'Canoagem', 'Ouro'))
australia.atletas.append(Atletas('Mack Horton', 'Natação', 'Prata'))
australia.atletas.append(Atletas('Madison de Rozario', 'Atletismo', 'Ouro'))
australia.atletas.append(Atletas('Peter Bol', 'Atletismo', 'Prata'))
australia.atletas.append(Atletas('Cate Campbell', 'Natação', 'Ouro'))
australia.atletas.append(Atletas('Matthew Temple', 'Natação', 'Bronze'))
australia.atletas.append(Atletas('Kelsey-Lee Barber', 'Atletismo', 'Ouro'))
australia.atletas.append(Atletas('Tom Green', 'Canoagem', 'Ouro'))
australia.atletas.append(Atletas('Annabelle Smith', 'Mergulho', 'Prata'))

### Brasil
brasil.atletas.append(Atletas('Rebeca Andrade', 'Ginástica', 'Ouro'))
brasil.atletas.append(Atletas('Alison dos Santos', 'Atletismo', 'Ouro'))
brasil.atletas.append(Atletas('Isaquias Queiroz', 'Canoagem', 'Prata'))
brasil.atletas.append(Atletas('Rayssa Leal', 'Skate', 'Bronze'))
brasil.atletas.append(Atletas('Ana Marcela Cunha', 'Natação', 'Ouro'))
brasil.atletas.append(Atletas('Martine Grael', 'Vela', 'Ouro'))
brasil.atletas.append(Atletas('Bruno Fratus', 'Natação', 'Bronze'))
brasil.atletas.append(Atletas('Mayra Aguiar', 'Judô', 'Bronze'))
brasil.atletas.append(Atletas('Pedro Barros', 'Skate', 'Prata'))
brasil.atletas.append(Atletas('Beatriz Ferreira', 'Boxe', 'Prata'))
brasil.atletas.append(Atletas('Kahena Kunze', 'Vela', 'Ouro'))
brasil.atletas.append(Atletas('Daniel Cargnin', 'Judô', 'Bronze'))
brasil.atletas.append(Atletas('Ágatha Bednarczuk', 'Vôlei de Praia', 'Prata'))
brasil.atletas.append(Atletas('Darlan Romani', 'Atletismo', 'Ouro'))
brasil.atletas.append(Atletas('Hebert Conceição', 'Boxe', 'Ouro'))


def index(request):
    return render(request, 'medalhas/tabela_paises.html', {
    "paises": lista_paises
    })

def atletas_medalhas(request, pais_medalhas):
    pais_escolhido = procura_instancia_pais(pais_medalhas)
    return render(request, 'medalhas/medalhas_atletas.html', {
        "pais": pais_escolhido
        })