# Programação Orientada a Objetos (POO)

Este repositório contém material referente à disciplina de **Programação Orientada a Objetos (POO)** do curso técnico em Informática. A seguir, estão descritos alguns conceitos fundamentais da POO.

---

## Classes

Uma **classe** é uma abstração que representa um conceito ou elemento, definindo suas **características** (atributos) e **comportamentos** (métodos). Ela atua como um molde a partir do qual os **objetos** (instâncias da classe) são criados. 

### Características das Classes:
- **Atributos**: Definem as propriedades que os objetos terão.
- **Métodos**: Definem as ações ou comportamentos dos objetos.

Os objetos criados a partir de uma classe compartilham a mesma definição de atributos e métodos, mas podem ter valores únicos para seus atributos e podem agir de forma independente.

---

## Objeto

Um **objeto** é uma **entidade concreta** criada a partir de uma classe. Em outras palavras, um objeto é uma **instância** de uma classe. Esta entidade possui as **características (atributos)** definidas pela classe, mas cada objeto tem seus **valores independentes**.

### Propriedades dos Objetos:
- Cada objeto tem uma **estrutura** definida pela classe.
- Cada objeto mantém seu **próprio estado** (valores dos atributos).
- Objetos diferentes podem compartilhar a mesma classe, mas manter valores independentes para seus atributos.

---

## Instância

Uma **instância** é uma **ocorrência específica** de uma classe. Quando um objeto é criado a partir de uma classe, ele é considerado uma instância dessa classe. 

### Propriedades das Instâncias:
- Cada instância tem seus **valores próprios** para os atributos.
- Instâncias compartilham a mesma **estrutura** (definição de atributos e métodos), mas seus **comportamentos** e **estados** podem variar.
  
---

## Parâmetro `self`

Em Python, o parâmetro `self` é usado para referenciar a **instância da classe** atual. Ele é sempre o primeiro parâmetro dos métodos de instância e permite acessar os atributos e métodos da instância que invocou o método.

### Características do `self`:
- Refere-se à **instância específica** do objeto.
- Usado para **manipular atributos e métodos** pertencentes a um objeto específico.
- Por convenção, usa-se o nome `self`, mas qualquer outro nome seria funcional (embora não recomendado).

Exemplo de uso do `self`:

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"Car: {self.brand} {self.model}")
```
## Método Construtor

O método construtor é um método especial que inicializa os atributos de uma instância de uma classe. Em Python, o método construtor é definido pelo nome especial `__init__`.
Características do Método Construtor:

    - Usado para configurar atributos iniciais da instância.
    - É automaticamente chamado quando um objeto é criado.
    - Permite passar parâmetros no momento da criação do objeto para personalizar a instância.

Exemplo de um método construtor:

```python

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking!")

# Criando instâncias da classe 'Dog'
dog1 = Dog("Rex", "German Shepherd")
dog2 = Dog("Buddy", "Golden Retriever")

# Chamando o método
dog1.bark()  # Saída: Rex is barking!
dog2.bark()  # Saída: Buddy is barking!
```


