town = input("Please type a name for the town:")
occupation = input("Please type in an occupation:")
name = input("Please type in a name:")
crime = input("Please type in a crime:")
plural_noun = input("Please type in a plural noun:")
adj = input("Please type in an adjective:")
noun = input("Please type in a noun:")

madlib = "In the mysterious town of {town}, a {occupation} named {name}, was accused of {crime}. The crime scene was filled with {plural_noun} and was so obsure, police arrested the perpetrator straight away. During the trial, the {adj} perpetrator, managed to fill the room with {noun} and managed to escape. To this day, they have never been found!".format(town=town, occupation=occupation, name=name, crime=crime,plural_noun=plural_noun, adj=adj, noun=noun)

print(madlib)