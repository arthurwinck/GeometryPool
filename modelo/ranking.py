import json
import os


class Ranking:
    def __init__(self, filepath, tamanho=10):
        self.filepath = filepath
        self.tamanho = tamanho
        self.validar_arquivo()
        self.carregar_arquivo()

    def validar_arquivo(self):
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w+") as file:
                file.write(json.dumps([]))

    def carregar_arquivo(self):
        with open(self.filepath, "r") as file:
            self.ranking = json.loads(file.read())

    def salvar_arquivo(self):
        with open(self.filepath, "w") as file:
            file.write(json.dumps(self.ranking))

    def atualizar_ranking(self):
        # atualiza a ordenação por score
        self.ranking = sorted(self.ranking, key=lambda d: d["score"], reverse=True)

        # remove jogadores se o tamanho for maior que o limite
        self.ranking = self.ranking[: self.tamanho]

    def inserir_jogador_ranking(self, nome, score):
        registro = {
            "nome": nome,
            "score": score,
        }

        self.ranking.append(registro)
        self.atualizar_ranking()
        self.salvar_arquivo()

    def ler_ranking(self):
        return self.ranking


if __name__ == "__main__":
    r = Ranking("ranking.json", 3)
    r.inserir_jogador_ranking("test", 99999999)
