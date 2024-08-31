from models.client import Client
from utils.helper import format_float_str_currency

class Count:
	code: int = 1001
	def __init__(self: object, client: Client) -> None:
		self.__number: int = Count.code
		self.__client: Client = client
		self.__balance: float = 0.00
		self.__limit: float = 100.00
		self.__total_balance: float = self._calculate_total_balance
		Count.code += 1
	
	def __str__(self: object) -> str:
		return (f"Number of the count: {self. number} \n"
		        f"Client: {self.client.name} \n"
		        f"Total balance: "
		        f"{format_float_str_currency(self.total_balance)} \n")
	
	@property
	def number(self: object) -> int:
		return self.__number
	
	@property
	def client(self: Client) -> Client:
		return self.__client
	
	@property
	def balance(self: object) -> float:
		return self.__balance
	
	@balance.setter
	def balance(self: object, value: float) -> None:
		self.__balance = value
	
	@property
	def limit(self: object) -> float:
		return self.__limit
	
	@limit.setter
	def limit(self, value: float) -> None:
		self.__limit = value
	
	@property
	def total_balance(self: object) -> float:
		return self.__total_balance
	
	@property
	def _calculate_total_balance(self: object) -> float:
		return self.balance + self.limit
	
	@total_balance.setter
	def total_balance(self: object, value: float) -> None:
		self.__total_balance = value
	
	def deposit(self: object, value: float) -> None:
		if value > 0:
			self.balance = self.balance + value
			self.total_balance = self._calculate_total_balance
			print("Bank deposit made successfully!")
		else:
			print("Error when making deposit. Please "
			      "try again!")
	
	def withdraw(self: object, value: float) -> None:
		if 0 < value <= self.total_balance:
			if self.balance >= value:
				self.balance -= value
				self.total_balance = self._calculate_total_balance
			else:
				remaining: float = self.balance - value
				self.balance = 0.00
				self.limit += remaining
				self.total_balance = self._calculate_total_balance
			print("Bank withdraw made successfully!")
				
		else:
			print("Bank withdrawal not made. Please "
			      "try again.")
	
	def transfer(self: object,
	             destination: object,
	             value: float) -> None:
		if 0 < value <= self.total_balance:  # <=> if value > 0 and self.total_balance >= value:
			if self.balance > value:
				self.balance -= value
				self.total_balance = self._calculate_total_balance
				destination.balance += value
				destination.total_balance = destination._calculate_total_balance
				
			else:
				remaining: float = self.balance - value
				self.balance = 0.0
				self.limit += remaining
				self.total_balance = self._calculate_total_balance
				destination.balance += value
				destination.total_balance = destination._calculate_total_balance
			
			print("Bank transfer completed successfully!")
		else:
			print("Bank transfer not made. Please "
			      "try again!")
		
	
	
	
	
	
	
		