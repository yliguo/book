import myBook

B1 = myBook.eBook("Gone with the Wind", 9.99, "https://ebook-mecca.com/online/gonewiththewind.pdf")
B2 = myBook.paperBook("One Hundred Years of Solitude", 8.99, 4.99)
print("The cost of \"" + str(B1.title) + "\" is $", end = "")
B1.showCost()
print("The cost of \"" + str(B2.title) + "\" is $", end = "")
B2.showCost()