import re


pattern = r"(?P<Day>\d{2})(?P<separator>[\.\-\/])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})"

text = input()
matches = [match_obj.groupdict() for match_obj in re.finditer(pattern,text)]
print('\n'.join([f"Day: {data['Day']}, Month: {data['Month']}, Year: {data['Year']}" for data in matches]))
