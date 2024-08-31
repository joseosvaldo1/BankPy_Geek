from datetime import date

from utils.helper import date_to_string, string_to_date


class Client:
	counter: int = 101
	
	def __init__(self: object,
	             name: str,
	             email: str,
	             cpf: str,
	             birthday: str) -> None:
		self.__code: int = Client.counter
		self.__name: str = name
		self.__email: str = email
		self.__cpf: str = cpf
		self.__birthday: date = string_to_date(birthday)
		self.__reg_date: date = date.today()
		Client.counter += 1
	
	@property
	def code(self: object) -> int:
		return self.__code
	
	@property
	def name(self: object) -> str:
		return self.__name
	
	@property
	def email(self: object) -> str:
		return self.__email
	
	@property
	def cpf(self: object) -> str:
		return self.__cpf
	
	@property
	def birthday(self:object) -> str:
		return date_to_string(self.__birthday)
	
	@property
	def reg_date(self: object) -> str:
		return date_to_string(self.__reg_date)
	
	
	def __str__(self: object) -> str:
		return (f'Client Data:'
		        f'Code: {self.code} \n'
		        f'Name: {self.name} \n'
		        f'E-mail: {self.email} \n'
		        f'NI-CPF: {self.cpf} \n'
		        f'Birthday: {self.birthday} \n'
		        f'Registration date: {self.reg_date}')