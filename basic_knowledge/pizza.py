def make_pizza(size,*toppings):
    print('\nMaking a '+str(size)+'-inch pizza need:')
    for topping in toppings:
        print('-'+topping)