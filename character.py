from struct import pack_into


print("Create your Character!")
name = input("What is your character called? ")
age = input("How old is your character? ")
strengths = input("What are your character's strengths? ")
weaknesses = input("What are your character's weaknesses? ")

print("Your character's name is", name)
print("Your character is", age, "years old")
print("Strengths:", strengths)
print("Weaknesses:", weaknesses)
print(name, "says, 'Thanks for creating me!'")