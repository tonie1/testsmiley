
print("Who is the current President of the United States?")

def unitedfunction(*firstnames):

    print("The current President of the United States is " + firstnames[4])

unitedfunction("Bill", "George", "Barack", "Donald", "Joe")


print("But what is Joe's last name?")


def lastnamefunctionCOOL(**lastnames):

    print("His last name is " + lastnames["lname"])

lastnamefunctionCOOL(fname = "Joe", lname = "Mama")

print("What mistakes has Joe made?")

print("There is a lot. Heres a list: ")

def Lfunction(L = "1994 Crime Bill"):

    print(L)

Lfunction("Afghanistan Evacuation")
Lfunction()
Lfunction("Denial of Hunter Biden Controversy")
Lfunction("Inflation")
Lfunction("Sniffing Girls")
Lfunction("Dementia & Speech Impediment")