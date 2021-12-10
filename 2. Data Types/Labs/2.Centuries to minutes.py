centur = int(input())

years = int(centur * 100)
days = years * 365.2422
hours = days * 24
minutes = hours * 60

print(f"{centur} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")