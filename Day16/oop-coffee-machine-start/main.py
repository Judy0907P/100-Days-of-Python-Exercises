from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#TODO-1 print report
money_machine=MoneyMachine()
coffee_maker=CoffeeMaker()
menu=Menu()

is_on=True



#TODO-2 check resources sufficient
while is_on:
    options=menu.get_items()
    choice=input(f"What would you like? ({options}): ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink=menu.find_drink(choice)
                  #TODO-3 process coins
#TODO-4 check transaction successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
  #TODO-5 make coffee
                coffee_maker.make_coffee(drink)



    