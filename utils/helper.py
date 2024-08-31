from datetime import date
from datetime import datetime


def date_to_string(date: date) -> str:
	return date.strftime("%d/%m/%Y")


def string_to_date(date: str) -> date:
	return datetime.strptime(date, "%d/%m/%Y")


# def format_float_str_currency(value: float) -> str:
# 	return f"R$ {value:,.2f}"


def format_float_str_currency(value: float) -> str:
    # Format the value with thousand separators and two decimal places
    formatted_value = f"{value:,.2f}"
    # Replace commas with a temporary character and then swap dots and commas for Brazilian formatting
    formatted_value = formatted_value.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {formatted_value}"