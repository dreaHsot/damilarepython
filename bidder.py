import os

os.system('clear')
print("*****WELCOME TO THE SILENT BIDDING PROGRAM*****\n")
def max_bid(bids):
    m_value = 0
    highest_values = dict()
    for i, j in bids.items():
        if j > m_value:
            highest_values.clear()
            m_value = j
            m_key = i
            highest_values[i] = j
        elif j == m_value:
            highest_values[i] = j

    if len(highest_values) == 1:
        print(f"The highest bidder is {m_key} at {m_value}")
    else:
        print("There are multiple highest bidders: ")

        #print(highest_values)
        for i in highest_values:
            print(i)

        print("\nLet's have another round of bid for the top bidders")

bids = dict()

again = True

while again:
    key = input("What is the name?: ")
    value = int(input("What is your bid?: "))

    bids[key] = value

    another = input("Is there another bidder?Y/N: ").lower()
    if another == 'n':
        #os.system('clear')
        again = False
    elif another == 'y':
        #os.system('clear')
        again = True
    else:
        another = input("Enter Y if there's another bidder and N if there's none: ")
    os.system('clear')

max_bid(bids)
