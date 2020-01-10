import random 
import numpy as np

class Produto():
    def __init__(self, nome, espaco, valor):
        self.nome = nome
        self.espaco = espaco
        self.valor = valor
        
class Individuo():
    def __init__(self, espacos, valores, limite_espacos, geracao=0):
        self.espacos = espacos
        self.valores = valores
        self.limite_espacos = limite_espacos
        self.nota_avaliacao = 0
        self.espaco_usado = 0
        self.geracao = geracao
        self.cromossomo = []
        self.atual = []
        self.itens_max = []
        self.prox = []
        self.nota_avaliacao1 = []
        self.nota_avaliacao = []
        self.lista = []
        self.lista1 = []
        self.ultimos_valores = []
        self.avalia = []
        self.avalia2 = []
        self.t = 0
             

        self.cromossomo= [random.randint(0,1) for i in range(14)]          
                
                    
    def avaliacao(self,valor):
        nota = 0
        for i in range(len(valor)):
            if valor[i] == 1:
                nota+=self.valores[i]    
        nota_avaliacao = nota
        return nota_avaliacao
       
        
    def sucessores(self):
        for i in range(5):
            self.atual = [random.randint(0,1) for i in range(14)]
            self.lista1.append(self.atual) 
        
    def sucessor(self):
        while True:
            self.atual = [random.randint(0,1) for i in range(14)]
            if self.atual not in self.lista:
                 self.lista.append(self.atual)
                 break
             
    def crossover(self, outro_individuo):
        corte = round(random()  * len(self.cromossomo))
        
        filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
        filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
        
        filhos = [Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1),
                  Individuo(self.espacos, self.valores, self.limite_espacos, self.geracao + 1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos
    
    
    def mutacao(self,taxa_mutacao):
        for i in range(len(self.cromossomo)):
            if random() < taxa_mutacao:
                if self.cromossomo[i] == 1:
                    self.cromossomo[i] = 0
                else:
                    self.cromossomo[i] = 1
        return self
        
    def t_max(self):
        valores =[]
        soma = 0
        cont = 0 
        self.sucessores()
        for j in range(len(self.lista1)):
            self.avalia = self.avaliacao(self.lista1[j])
            valores.append(self.avalia)

        for i in range(4):
            for j in range(i+1,5):
                dife = valores[i]-valores[j]
                soma +=dife
                cont+=1
        self.t=(soma/cont)*10
        if self.t < 0:
            self.t = self.t *-1
            return self.t
        return self.t
        
    def tempera_simulada(self):
        t_min = 1
        self.atual = list(self.cromossomo)
        print(self.atual)
        self.nota_avaliacao = self.avaliacao(self.atual)
        print(self.nota_avaliacao)
        t_max = self.t_max()
        while(t_max >= t_min):
                self.sucessor()
                self.prox = self.lista[-1]
                self.nota_avaliacao1 = self.avaliacao(self.prox)
                result = self.nota_avaliacao1-self.nota_avaliacao
                if (result < 0):
                    self.atual=self.prox
                    self.nota_avaliacao = self.nota_avaliacao1
    
                else:
                    ale = random.random()
                    result = result * -1
                    conta = result/t_max
                    aux = np.exp(conta)
                    if(ale > aux):
                        self.atual=self.prox
                        self.nota_avaliacao = self.nota_avaliacao1
                    t_max = t_max * 0.9
                
        
                


    def subida_encosta(self):
        self.atual = list(self.cromossomo)
        print(self.atual)
        self.nota_avaliacao = self.avaliacao(self.atual)
        print(self.nota_avaliacao)
        while(True):
            self.ultimos_valores.append(self.atual)
            self.sucessor()
            self.prox = self.lista[-1]
            self.nota_avaliacao1 = self.avaliacao(self.prox)
            if self.nota_avaliacao1 < self.nota_avaliacao:
                print("melhor combinação:",self.ultimos_valores[-1])
                self.itens_max.append(self.nota_avaliacao)
                return
            else:
                self.atual = self.prox  
                self.nota_avaliacao = self.nota_avaliacao1
            
    def subida_encostaT(self):
        t=0
        t_max = 13
        self.atual = list(self.cromossomo)
        self.nota_avaliacao = self.avaliacao(self.atual)
        while(True):
            self.ultimos_valores.append(self.atual)
            self.sucessor()
            self.prox = self.lista[-1]
            self.nota_avaliacao1 = self.avaliacao(self.prox)
            if self.nota_avaliacao1 < self.nota_avaliacao:
                if t > t_max:
                    print("melhor combinação:",self.atual)
                    print("melhor avaliação:",self.nota_avaliacao)
                    return
                t+=1
            else:
                self.atual = self.prox  
                self.nota_avaliacao = self.nota_avaliacao1
                t = 0
class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        self.geracao = 0
        self.melhor_solucao = 0
            
    def inicializa_populacao(self, espacos,valores,limite_espacos):
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo(espacos,valores,limite_espacos))
        self.melhor_solucao = self.populacao[0]
        
    def ordena_populacao(self):
       self.populacao = sorted(self.populacao,
                               key = lambda populacao: populacao.nota_avaliacao,
                               reverse = True)

if __name__ == '__main__':
    #p1 = Produto("Iphone 6", 0.0000899, 2199.12)
    lista_produtos = []
    lista_produtos.append(Produto("Geladeira Dako", 0.751, 999.90))
    lista_produtos.append(Produto("Iphone 6", 0.0000899, 2911.12))
    lista_produtos.append(Produto("TV 55' ", 0.400, 4346.99))
    lista_produtos.append(Produto("TV 50' ", 0.290, 3999.90))
    lista_produtos.append(Produto("TV 42' ", 0.200, 2999.00))
    lista_produtos.append(Produto("Notebook Dell", 0.00350, 2499.90))
    lista_produtos.append(Produto("Ventilador Panasonic", 0.496, 199.90))
    lista_produtos.append(Produto("Microondas Electrolux", 0.0424, 308.66))
    lista_produtos.append(Produto("Microondas LG", 0.0544, 429.90))
    lista_produtos.append(Produto("Microondas Panasonic", 0.0319, 299.29))
    lista_produtos.append(Produto("Geladeira Brastemp", 0.635, 849.00))
    lista_produtos.append(Produto("Geladeira Consul", 0.870, 1199.89))
    lista_produtos.append(Produto("Notebook Lenovo", 0.498, 1999.90))
    lista_produtos.append(Produto("Notebook Asus", 0.527, 3999.00))
    #for produto in lista_produtos:
    #    print(produto.nome)
    
    espacos = []
    valores = []
    nomes = []
    for produto in lista_produtos:
        espacos.append(produto.espaco)
        valores.append(produto.valor)
        nomes.append(produto.nome)
    limite = 3
    
    individuo1 = Individuo(espacos, valores, limite)
    individuo2 = Individuo(espacos, valores, limite)
    #print("Cromossomo = %s" % str(individuo1.cromossomo))
    
    individuo1.subida_encosta()
    individuo1.subida_encostaT()
    individuo1.tempera_simulada()            
    
  
        
        
    