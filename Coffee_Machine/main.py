from Menu import *
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money =0
def other(order):
    if order =='off':
      on = False
    elif  order.lower() =='report':
      print(f'Water: {resources["water"]}')
      print(f'Coffee: {resources["coffee"]}')
      print(f'Milk: {resources["milk"]}')
      print(f'Money: ${money}')
    else:
        return 'Enter Right Command'
on = True
while on:
  order = input("What would you like? (espresso/latte/cappuccino): ")
  print("Please insert the coins")
  total_money_inserted = int(input('How many Quaters?: '))*0.25
  total_money_inserted += int(input('How many Dimes?: '))*0.1
  total_money_inserted += int(input('How many Nickel?: '))*0.05
  total_money_inserted += int(input('How many pennies?: '))*0.01
  change = total_money_inserted - MENU[order]['cost']
  if change < 0:
      break
  if order =='latte' or order =='espresso' or order == 'cappuccino':
      if resources['coffee'] <= MENU[order]['ingredients']['coffee'] or  resources['water'] <= MENU[order]['ingredients']['water'] or resources['milk'] <= MENU[order]['ingredients']['milk']:
       print('Not Enough resources!')
       break
      money = money + MENU[order]['cost']
      resources['water'] = resources['water'] - MENU[order]['ingredients']['water']
      resources['milk'] = resources['milk'] - MENU[order]['ingredients']['milk']
      resources['coffee'] = resources['coffee'] - MENU[order]['ingredients']['coffee']
      print(f'Here is ${round(change,2)} change')
      print(f'Here is your {order}.Enjoy!')
  else:
        other(order)
  
   