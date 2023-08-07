
inventory = []


sales_record = {}


def add_snack(snack_id, name, price, availability):
    snack = {
        "snack_id": snack_id,
        "name": name,
        "price": price,
        "availability": availability
    }
    inventory.append(snack)
    print("Snack added to inventory.")


def remove_snack(snack_id):
    for snack in inventory:
        if snack["snack_id"] == snack_id:
            inventory.remove(snack)
            print("Snack removed from inventory.")
            break


def update_availability(snack_id, availability):
    for snack in inventory:
        if snack["snack_id"] == snack_id:
            snack["availability"] = availability
            print("Snack availability updated.")
            break


def make_sale(snack_id):
    snack_found = False
    for snack in inventory:
        if snack["snack_id"] == snack_id:
            snack_found = True
            if snack["availability"] == "yes":
                if snack_id in sales_record:
                    sales_record[snack_id] += 1
                else:
                    sales_record[snack_id] = 1
                snack["availability"] = "no"
                print("Sale made and inventory updated.")
            else:
                print("Snack is unavailable.")
            break
    if not snack_found:
        print("Snack not found in inventory.")


while True:
    print("1. Add a snack")
    print("2. Remove a snack")
    print("3. Update snack availability")
    print("4. Make a sale")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        snack_id = input("Enter snack ID: ")
        name = input("Enter snack name: ")
        price = float(input("Enter snack price: "))
        availability = input("Enter snack availability (yes/no): ")

        add_snack(snack_id, name, price, availability)

    elif choice == "2":
        snack_id = input("Enter snack ID to remove: ")
        remove_snack(snack_id)

    elif choice == "3":
        snack_id = input("Enter snack ID to update availability: ")
        availability = input("Enter new availability (yes/no): ")
        update_availability(snack_id, availability)

    elif choice == "4":
        snack_id = input("Enter snack ID sold: ")
        make_sale(snack_id)

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again.")
