# Christmas Project

# Customer details
print("Customer Details;")

# first name
first_name = str(input("Enter first name: (Max 30 characters)\n"))
fn = first_name
# character length
if len(first_name) > 30:
    print("Only 30 characters allowed!")
if len(first_name) == 0:
    print("Invalid input")

# Last name
last_name = str(input("Enter last name: (Max 30 characters)\n"))
ln = last_name
if len(last_name) > 30:
    print("Only 30 characters allowed!")
if len(last_name) == 0:
    print("Invalid input")

# Phone number
phone_number = str(input("Enter the phone number:\n"))
if len(phone_number) != 10:
    print("Invalid phone number!")

# Email
e = str(input("Enter email address:\n"))
if e == "":
    print("Please enter a valid email!")
if "@" not in e:
    print("No '@', Please enter a valid email!")
if "." not in e:
    print("No '.', Please enter a valid email!")
email = e

# Pizza order

# Pizza types
# small margherita
sm1 = "\tSmall Margherita - €"
sm = 10
# medium margherita
mm1 = "\tMedium margherita - €"
mm = 12
# Large margherita
lm1 = "\tLarge Margherita - €"
lm = 15
# Small pepperoni
sp1 = "\tSmall Pepperoni - €"
sp = 12
# Medium pepperoni
mp1 = "\tSmall Pepperoni - €"
mp = 14
# Large pepperoni
lp1 = "\tLarge Pepperoni - €"
lp = 17
# Small four seasons
sfs1 = "\tSmall Four Seasons - €"
sfs = 11.50
# Medium four seasons
mfs1 = "\tMedium Four Seasons - €"
mfs = 13.50
# Large four seasons
lfs1 = "\tLarge Four Seasons - €"
lfs = 16.50

# List of pizza types


def list_of_pizzas():
    list_of_pizza = str(input("\nList of available pizzas? (y/n)\n"))
    if list_of_pizza == "y":
        print("\nList of Pizza types;")
        print(sm1, sm)
        print(mm1, mm)
        print(lm1, lm)
        print(sp1, sp)
        print(mp1, mp)
        print(lp1, lp)
        print(sfs1, sfs)
        print(mfs1, mfs)
        print(lfs1, lfs, "\n")
    else:
        print()


# Pizza order
p = 0
pizza_ = input("\nPizza? (y/n)\n")
if pizza_ == "y":
    list_of_pizzas()
    pt = str(input("What type of pizza? (Enter the initials of the pizza only. E.G. sp for small pepperoni)\n"))
    if pt == "sm":
        p = sm
        print(sm1, sm)
    if pt == "mm":
        p = mm
        print(mm1, mm)
    if pt == "lm":
        p = lm
        print(lm1, lm)
    if pt == "sp":
        p = sp
        print(sp1, sp)
    if pt == "mp":
        p = mp
        print(mp1, mp)
    if pt == "lp":
        p = lp
        print(lp1, lp)
    if pt == "sfs":
        p = sfs
        print(sfs1, sfs)
    if pt == "mfs":
        p = mfs
        print(mfs1, mfs)
    if pt == "lfs":
        p = lfs
        print(lfs1, lfs)
    if pt == "n":
        p = 0
        print("No pizza")
else:
    p = 0
    print("No input recognised")

# Toppings or dips
# Rucola
r1 = "\tRucola - €"
r = 1.50
# Mushrooms
m1 = "\tMushrooms - €"
m = 2
# Garlic Dip
gd1 = "\tGarlic Dip - €"
gd = 3
# Spicy Mayo Dip
smd1 = "\tSpicy Mayo Dip - €"
smd = 3


# Topping order

def list_of_topping():
    list_of_extra = str(input("\nList of extra toppings and dips? (y/n)\n"))
    if list_of_extra == "y":
        print(r1, r)
        print(m1, m)
        print(gd1, gd)
        print(smd1, smd, "\n")
    else:
        print()


# List of extra toppings and dips
w = 0
t = str(input("\nExtra toppings or dips? (y/n)\n"))
if t == "y":
    list_of_topping()
    d = input("What extra toppings or dip? (Enter the initials)\n")
    if d == "r":
        w = r
        print(r1, r)
    if d == "m":
        w = m
        print(m1, m)
    if d == "gd":
        w = gd
        print(gd1, gd)
    if d == "smd":
        w = smd
        print(smd1, smd)
    if t == "n":
        w = 0
        print("No extra toppings or dips")
else:
    w = 0
    print("No input recognised")

# Receipt
receipt = str(input("\nReceipt? (y/n)\n"))
if receipt == "y":
    print("\t!!Welcome to Abi's Pizzeria!!")
    print("\t\t--- Receipt---")
    # .center() - to align the text
    # first and last name
    print("Name: {} {}".format(fn, ln))
    # phone number
    print("Phone: (" + phone_number[0:3] + ")", phone_number[4:10])
    # email
    print("Email:", email)
    # Pizza
    print("Pizza - €", p)
    # Toppings
    print("Toppings - €", w)
    subtotal = (p + w) / 123 * 100
    print("Subtotal - €", subtotal)
    vat = subtotal * 0.23
    print("VAT - €", vat)
    total = p + w
    if total >= 35:
        total = total * 0.9
    print("\tThank you for ordering with us! \n\tWe hope to serve you again!\n\t\tEnjoy your pizza!")
else:
    print("Pizza - €", p)
    # Toppings
    print("Toppings - €", w)
    subtotal = (p + w) / 123 * 100
    print("Subtotal - €", subtotal)
    vat = round(subtotal * 0.23, 2)
    print("VAT - €", vat)
    total = p + w
    if total >= 35:
        total = total * 0.9
    print(total)
