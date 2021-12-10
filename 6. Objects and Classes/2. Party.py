# class Party:
#     def __init__(self):
#         self.people = []
#
#
# party = Party()
# line = input()
# while line != "End":
#     party.people.append(line)
#
# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len(party.people)}")

class Party:
    def __init__(self):
        self.people = []

    def get_info(self):
        all_peoople = self.people # instance atribute
        prople_res = ", ".join(all_peoople)
        return f"""Going: {prople_res}  
Total: {len(all_peoople)}""" # """ za printirane na nqkolko reda

person_input = input()
party = Party()
while person_input != "End":
    party.people.append(person_input)

    person_input = input()

info = party.get_info()
print(info)