def max_bid(bids):
    m_value = 0
    highest_values = list()
    for i, j in bids.items():
        if j > m_value:
            highest_values.clear()
            m_value = j
            m_key = i
        elif j == m_value:
            highest_values.append(i)

    if not highest_values:
        print(f"The highest bidder is {m_key} at {m_value}")
    else:
        print("There are multiple highest bidders: ")

        for i in highest_values:
            print(i)

        print("\nLet's have another round of bid for the top bidders")

bids = dict()

again = True

while again:
    key = input("What is the name?: ")
    value = input("What is your bid?: ")

    bids[key] = value

    another = input("Is there another bidder?Y/N: ")
    if another == 'n' or another == 'N':
        again = False
    elif another == 'y' or another == 'Y':
        again = True
    else:
        another = input("Enter Y if there's another bidder and N if there's none: ")

m_value = 0
highest_values = dict()
for i, j in bids.items():
    if j > m_value:
        highest_values.clear()
        m_value = j
        m_key = i
    elif j == m_value:
        highest_values[i] == j


print(bids)
