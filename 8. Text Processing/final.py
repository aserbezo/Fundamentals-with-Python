def is_jackpot(ticket):
    for winning_symbol in winning_symbols:
        if winning_symbol in ticket:
            if ticket.count(winning_symbol) == 20:
                print(f"ticket \"{ticket}\" - 10{winning_symbol} Jackpot!")
                return True
    return False

def check_symbols(ticket):
    symbol = False
    for i in ticket:
      if i == "@":
          symbol = True
          break
      elif i == "#":
          symbol = True
          break
      elif i == "$":
          symbol = True
          break
      elif i == "^":
          symbol = True
          break
    return symbol

def check_the_left(left_side):
    for winning_symbol in winning_symbols:
        if winning_symbol in left_side:
            i = 0
            count = 0
            symbol = winning_symbol
            while i < len(left_side):
                curr_ch = left_side[i]
                if i + 1 >= len(left_side) - 1:
                    next_sym = left_side[i - 1]
                else:
                    next_sym = left_side[i]
                if curr_ch == winning_symbol and next_sym == winning_symbol:
                    count += 1
                i += 1
    return f"{count}{symbol}"

def check_the_right(right_side):
    for winning_symbol in winning_symbols:
        if winning_symbol in right_side:
            j = 0
            count_r = 0
            symbol = winning_symbol
            while j < len(right_side):
                curr_chr = right_side[j]
                if j + 1 >= len(right_side) - 1:
                    next_syms = right_side[j - 1]
                else:
                    next_syms = right_side[j]
                if curr_chr == winning_symbol and next_syms == winning_symbol:
                    count_r += 1
                j += 1

    return f"{count_r}{symbol}"

def match(left, right):
    if left == right:
        result = "Yes"
    else:
        result = min(left, right)
    return (f"ticket \"{ticket}\" - {result}")

winning_symbols = ["@", "#", "$", "^"]
tickets = [el.strip() for el in input().split(", ")]

for ticket in tickets:
    left_side = ticket[:10]
    right_side = ticket[10:]
    if not len(ticket) == 20:
        print(f"invalid ticket")
        continue
    if is_jackpot(ticket):
        continue
    if check_symbols(ticket):
        result_left = check_the_left(left_side)
        result_right = check_the_right(right_side)
        maching = match(result_right,result_left)
        print(maching)
    else:
        print(f"ticket \"{ticket}\" - no match")




