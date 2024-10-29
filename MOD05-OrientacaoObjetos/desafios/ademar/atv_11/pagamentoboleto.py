from pagamento import Pagamento

class PagamentoBoleto(Pagamento):
    def __init__(self, codigo_boleto=""):
        self._codigo_boleto = codigo_boleto

    @property
    def codigo_boleto(self):
        return self._codigo_boleto

    @codigo_boleto.setter
    def codigo_boleto(self, codigo_boleto):
        if len(codigo_boleto) != 13:
            raise ValueError("O código do boleto deve ter 13 dígitos.")
        self._codigo_boleto = codigo_boleto

    def processar_pagamento(self):
        print(f"Pagamento com boleto {self._codigo_boleto} processado com sucesso.")
        
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def informacao(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}')

class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    def informacao_completa(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Portas: {self.numero_portas}')

class Calculadora:
    def somar(self, a, b=0, c=0):
        return a + b + c

# Testando a sobrecarga simulada
calc = Calculadora()

# Chamando o método com diferentes números de argumentos
print(calc.somar(2))         # Saída: 2
print(calc.somar(2, 3))      # Saída: 5
print(calc.somar(2, 3, 4))   # Saída: 9


class Calculadora:
    def somar(self, *args):
        return sum(args)

# Testando a sobrecarga simulada com *args
calc = Calculadora()

# Chamando o método com diferentes números de argumentos
print(calc.somar(2))         # Saída: 2
print(calc.somar(2, 3))      # Saída: 5
print(calc.somar(2, 3, 4))   # Saída: 9

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def mostrar_info(self):
        print(f'Aluno: {self.nome}, Matrícula: {self.matricula}')

class Curso:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def mostrar_alunos(self):
        for aluno in self.alunos:
            aluno.mostrar_info()
            
# Exemplo de Polimorfismo

class Animal:
    def emitir_som(self):
        raise NotImplementedError("Este método deve ser implementado pela subclasse")

class Cachorro(Animal):
    def emitir_som(self):
        return "Late"

class Gato(Animal):
    def emitir_som(self):
        return "Mia"

# Teste de Polimorfismo
animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.emitir_som())