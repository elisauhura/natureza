def gerador(tamanho, gen):
    def gera():
        arr = []
        for _ in range(tamanho):
            arr.append(gen())
        return arr
    return gera