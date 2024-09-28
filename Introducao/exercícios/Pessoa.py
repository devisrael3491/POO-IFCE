class Pessoa
  def __init__(self, nome : str, idade: int) -> None:
    self.__name = nome
    self.__idade = idade
  def get_name(self) -> str:
    return self.__name
  def set_name(self, new_name : str) -> None:
    if isinstance(new_name, str):
      if new_name.isalpha():
        self.__name = new_name
      else:
        print(f'O nome não pode conter caracteres que não sejam letras.')
    else:
      print(f'O nome deve ser da classe string.')
  def get_idade(self) -> int:
    return self.__idade
  def set_idade(self, new_age : int) -> None:
    if isinstance(new_age, int):
      if new_age >= 0:
        self.__idade = new_age
      else:
        print(f'A idade não pode assumir valores negativos.')
    else:
      print(f'A idade deve ser da classe int.')
  def apresentar(self) -> None:
    print(f'Olá, meu nome é {self.get_name()} e eu tenho {self.get_idade()} anos.')
    
