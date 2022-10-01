import database

MENU_PROMPT=""" ---Products---
Please choose one of these option:
1)Add a product.
2)See all product
3)Search product
4)See top rated product
5)EXIT
6)See product by Price(low to high).

You selected:"""

def menu():
    conn=database.conn()
    database.createTable(conn)

    while (userInput := input(MENU_PROMPT)) !="5":
        if userInput =="1":
            name=input("Eneter product name: ")
            price=int(input("Eneter product price: "))
            rating=int(input("Eneter product rating: "))
            database.insertP(conn,name,price,rating)
        elif userInput =="2":
            product=database.getAllP(conn)

            for p in product:
                print(p)
        elif userInput =="3":
            name=input("Eneter product name: ")
            prod=database.getPName(conn,name)
            for p in prod:
                print(f"{p[1]} - {p[2]}-{p[3]}/5")
        elif userInput =="4":
            product=database.getTopP(conn)
            print("Product by rating :")

            for p in product:
                print(p)
        elif userInput =="6":
            product=database.getPByPrice(conn)
            print("Product by price: ")
            for p in product:
                print(p)
        else:
            print("Wrong Input!,Please try again!")


menu()