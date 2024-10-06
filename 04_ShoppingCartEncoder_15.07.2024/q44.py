def readShoppingCart(cart, read_file):
    with open(read_file) as my_file:
        for line in my_file:
            data = line.strip().split(',')
            cart.append(data[0])
    print('\nStep 1:')
    for item in cart:
        print(item)


def storeInCharMatrix(cart):
    print(f'\nStep 2: {cart}\n')


def convertToRTL(cart):
    max_length = max(len(item) for item in cart) if cart else 0
    formatted_items = []
    for item in cart:
        formatted_items.append(item.rjust(max_length))
    nested = [char.split(', ') for char in formatted_items]
    print(f"Step 3: {formatted_items}")
    return nested


def encryptToASCII(nested):
    ascii_values = [list(map(ord, i[0])) for i in nested]
    print(f'\nStep 4: {ascii_values}\n')
    return ascii_values


def networkStream(ascii):
    flatList = sum(ascii, [])
    final = ''.join(map(str, flatList))
    print(f'Step 5: {final}\n')
    return final


def saveToFile(final, output_file):
    with open(output_file, 'w') as f:
        f.write(final)
    print(f'Step 6: Saved final output to {output_file}\n')


def main():
    cart = []
    csv_file = "Q4/store.csv"
    output_file = "output.txt"
    
    # Pass cart by reference through each function
    readShoppingCart(cart, csv_file)
    storeInCharMatrix(cart[:])  # Pass a shallow copy of cart to keep original cart unchanged
    nested = convertToRTL(cart[:])  # Pass a shallow copy of cart to keep original cart unchanged
    ascii_values = encryptToASCII(nested)  # Pass nested list by reference
    final = networkStream(ascii_values)  # Pass ascii_values list by reference
    saveToFile(final, output_file)


if __name__ == '__main__':
    main()
