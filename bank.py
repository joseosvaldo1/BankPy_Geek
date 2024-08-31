from typing import List
from time import sleep

from models.client import Client
from models.count import Count

counts: List[Count] = []


def main() -> None:
	menu()


def menu() -> None:
	print('##################################')
	print('############### ATM ##############')
	print('############ Geek Bank ###########')
	print('##################################')
	
	print("Choose an option from the menu below:")
	print('1. Create count;')
	print('2. Make withdraw;')
	print('3. Make deposit;')
	print('4. Make transfer;')
	print('5. List counts;')
	print('6. Log out of the system.')
	print("")
	
	mesage_1 = 'Enter your choice: '
	option: int = int(input(mesage_1))
	
	if option == 1:
		create_count()
	elif option == 2:
		make_withdraw()
	elif option == 3:
		make_deposit()
	elif option == 4:
		make_transfer()
	elif option == 5:
		list_counts()
	elif option == 6:
		mesage_2 = "We hope to see you again soon."
		print(mesage_2)
		sleep(2)
		exit(0)
	else:
		mesage_3 = ("Invalid option. Please select an "
		            "option between 1 and 6, inclusive.")
		print(mesage_3)
		sleep(2)
		menu()
	
		
def create_count() -> None:
	mesage_4 = "Please enter the client details:"
	print(mesage_4)
	
	name: str = input("Client's full name: ")
	email: str = input("Client's email address: ")
	cpf: str = input("Client's CPF: ")
	birthday: str = input("Client's birthday: ")
	
	client: Client = Client(name, email, cpf, birthday)
	count: Count = Count(client)
	counts.append(count)
	
	mesage_5 = "Bank account created successfully!"
	print(mesage_5)
	
	print(30*'-')
	print('Count details:')
	print(count)
	print(30 * '-')
	
	sleep(2)
	
	menu()


def make_withdraw() -> None:
	if len(counts) > 0:
		mesage_6 = "Please enter your number account: "
		number: int = int(input(mesage_6))
		count: Count = search_count_by_number(number)
		
		if count:
			mesage_7 = "Please enter an amount to withdraw: "
			value: float = float(input(mesage_7))
			count.withdraw(value)
		else:
			print(f"Account number {number} was not found!")
	else:
		mesage_8 = ("There are no bank accounts "
		            "registered yet!")
		print(mesage_8)
	
	sleep(2)
	menu()


def make_deposit() -> None:
	if len(counts) > 0:
		mesage_9 = ("Please enter the account number to "
		            "proceed with the deposit: ")
		number: int = int(input(mesage_9))
		count: Count = search_count_by_number(number)
		
		if count:
			mesage_10 = "Please enter an amount to deposit: "
			value: float = float(input(mesage_10))
			count.deposit(value)
		else:
			print(f"Account number {number} was not found!")
	else:
		mesage_11 = ("There are no bank accounts "
		             "registered yet!")
		print(mesage_11)
	
	sleep(2)
	menu()


def make_transfer() -> None:
	if len(counts) > 0:
		mesage_12 = "Please enter your number account: "
		number_origin: int = int(input(mesage_12))
		count_origin: Count = search_count_by_number(number_origin)
		
		if count_origin:
			mesage_13 = ("Please provide the destination "
			"bank account number: ")
			number_destination: int = int(input(mesage_13))
			count_destination: Count = search_count_by_number(number_destination)
			if count_destination:
				mesage_14 = "Please enter a amount to transfer: "
				value: float = float(input(mesage_14))
				count_origin.transfer(count_destination, value)
			else:
				print(f"Account number {number_origin} of "
				      f"destination was not found!")
		else:
			print(f"Account number {number_origin} of "
			      f"origin was not found!")
	else:
		mesage_15 = ("There are no bank accounts "
				     "registered yet!")
		print(mesage_15)

	sleep(2)
	menu()

def list_counts() -> None:
	if len(counts) > 0:
		mesage_16 = "Listing registered bank accounts"
		print(mesage_16)
		
		for count in counts:
			print(count)
			print(20*'-')
			sleep(1)
	else:
		mesage_17 = ("There are no bank accounts "
					 "registered yet!")
		print(mesage_17)
	
	sleep(2)
	menu()


def search_count_by_number(number: int) -> Count:
	c: Count = None
	
	if len(counts) > 0:
		for count in counts:
			if count.number == number:
				c = count
	return c


if __name__ == '__main__':
	main()
	
	
	





