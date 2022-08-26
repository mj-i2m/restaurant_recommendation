from vertex import Restaurant

pastaparlor = Restaurant('Pasta Parlor', (5, 5), 'Italian', '$$', 3, True)
sushistation = Restaurant('Sushi Station', (7, 3), 'Japanese', '$$$', 5, True)
hotdoghouse = Restaurant('Hotdog House', (2, 4), 'Fast Food', '$', 3, False)
burgerbastion = Restaurant('Burger Bastion', (5, 5), 'Fast Food', '$', 4, True)
pizzapalace = Restaurant('Pizza Palace', (7, 4), 'Fast Food', '$', 2, True)
sandwichspot = Restaurant('Sandwich Spot', (2, 6), 'Fast Food', '$', 5, True)


restaurants = [pastaparlor, sushistation, hotdoghouse, burgerbastion, pizzapalace, sandwichspot]


def main():
    print('Welcome to the Restaurant Recommendation!')

    exit_resp = 'n'

    while exit_resp == 'n':

        start_search = input('Do you want to start the search for a restaurant? [y/n]')
        if start_search == 'y':
            print('Great!')
            cuisine = input('What cuisine do you like? \n'
                            '- Italian \n'
                            '- Japanese \n'
                            '- Fast Food \n'
                            'Please enter the text.')
            if cuisine in 'Italian Japanese Fast Food':
                price_segment = input('What is your price segment? \n'
                            '- $ \n'
                            '- $$ \n'
                            '- $$$ \n'
                            'Please enter the price segment.')
                if price_segment == '$' or price_segment=='$$' or price_segment=='$$$':
                    suggested_rests = [rest for rest in restaurants if
                                       rest.cuisine == cuisine and rest.price_segment == price_segment]
                    print(f'...{len(suggested_rests)} restaurants found...')
                    print('Based on your preferences I suggest the following restaurants:')
                    if suggested_rests:
                        for count, restaurant in enumerate(suggested_rests):
                            if restaurant.open:
                                status = 'open'
                            else:
                                status = 'closed'
                            print(f'{count+1} -', restaurant.name,f'- {restaurant.rating} out of 5 stars', f'- Currently {status}.')
                        distance_resp = input('Do you want to know the distance to each restaurant? [y/n]')
                        if distance_resp == 'y':
                            try:
                                you_x = int(input('Please enter your X coordinate.'))
                                you_y = int(input('Please enter your Y coordinate.'))
                            except:
                                print('Oops something went wrong :( - Probably and invalid entry!')
                            for restaurant in suggested_rests:
                                distance = restaurant.get_distance((you_x, you_y))
                                print(f'Distance to {restaurant.name}: ', distance)
                        elif distance_resp =='n':
                            pass
                        else:
                            print('Invalid entry!')


                    else:
                        print('Sorry, no matching restaurants available :(')
                else:
                    print('Invalid entry!')
            else:
                print('Invalid entry!')
        elif start_search == 'n':
            pass
        else:
            print('Invalid entry!')
        exit_resp = input('Do you want to exit? [y/n]')


if __name__ == '__main__':
    main()

