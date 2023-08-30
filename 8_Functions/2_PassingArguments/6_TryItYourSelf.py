print("8.3 T-shirt")
def make_shirt(size, message):
    print(" Shirt size is", size, 
          "the message is", message)
make_shirt(40, "'analice, write and execute'")


print("\n8.4 Large shirts")
def make_shirt(message = "I love python",size= 'large'):
    print("Size:", size, 
          "Message:", message)
make_shirt()
make_shirt(size='medium')
make_shirt(message="peace")

print("\n Cities")
def describe_city (city_name, country_name = 'Norway'):
    print(city_name, "is in", country_name)
describe_city("Quito", "Ecuador")
describe_city("Oslo")
describe_city("Edimburgo", "Escocia")
    