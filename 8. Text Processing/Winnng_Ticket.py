
def is_jackpot(ticket):
    for winning_symbol in winning_symbols:
        if winning_symbol in ticket:
            if ticket.count(winning_symbol) == 20:
                print(f"ticket \"{ticket}\" - 10{winning_symbol} Jackpot!")
                return True
    return False



def check_the_left_and_right(ticket):
    left = 0
    right = 0
    for winning_symbol in winning_symbols:
        left_side = ticket[:10]
        right_side = ticket[10:]
        if winning_symbol in left_side:
            i = 0
            count = 0
            while i < len(left_side):
                curr_ch = left_side[i]
                if i + 1 >= len(left_side) - 1:
                    next_sym = left_side[i - 1]
                else:
                    next_sym = left_side[i]
                if curr_ch == winning_symbol and next_sym == winning_symbol:
                    count += 1
                i += 1
            left = f"{count}{winning_symbol}"
    for winning_symbol in winning_symbols:
        if winning_symbol in right_side:
            i = 0
            count = 0
            while i < len(right_side):
                curr_ch = right_side[i]
                if i + 1 >= len(right_side) - 1:
                    next_sym = right_side[i - 1]
                else:
                    next_sym = right_side[i]
                if curr_ch == winning_symbol and next_sym == winning_symbol:
                    count += 1
                i += 1
            right =  f"{count}{winning_symbol}"
    return f"ticket \"{ticket}\" - {min(right,left)}"

winning_symbols = ["@", "#", "$", "^"]


tickets = [el.strip() for el in input().split(", ")]

for ticket in tickets:
    if not len(ticket) == 20:
        print(f"invalid ticket")
        continue
    if is_jackpot(ticket):
        continue

    if check_the_left_and_right(ticket):
        print(check_the_left_and_right())



    print(f"ticket \"{ticket}\" - no match")