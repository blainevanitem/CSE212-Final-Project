import random
import time

def main():
    checkout_line = []
    customers = []
    customers = create_customers(customers)
    checkout_line = enqueue_all(checkout_line,customers)
    dequeue_all(checkout_line)



def enqueue_all(checkout_line,customers):
    for i in range(len(customers)):
        checkout_line.append(customers[i])
    
    return checkout_line

def dequeue_all(checkout_line):
    for i in range(len(checkout_line)):
        print(f'Checking out {checkout_line[i].name} ----------------------------------')
        for j in checkout_line[i].items:
            time.sleep(0.3)
            print("** Beep **")
            print("Scanned: " + j + " for " + checkout_line[i].name)
        print("\n")
    for i in range(len(checkout_line)):
        checkout_line.pop()
    


def create_customers(customers):
    for i in range(10):
        customer = Customer(get_name(),items=[])
        for i in range(random.randint(1,13)):
            customer.items.append(get_item())
        customers.append(customer)

    return customers



def get_item():
    number = random.randint(0,9)
    items_in_store = ["sponge","paper towels","apple","banana","toilet paper","chocolate","milk","towels","gum","water bottles"]
    item = items_in_store[number]
    return item



def get_name():
    number = random.randint(0,9)
    different_names = ["Doug","John","Blaine","Mark","Mary","Sydney","Anna","Bob","Yohan","Margot"]
    name = different_names[number]
    return name



class Customer():
    def __init__(self,name,items):
        self.name = name
        self.items = items


if __name__ == '__main__':

    main()
