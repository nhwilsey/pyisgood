print("heloooooooooooooooooo")
print(1+1)
print(10/2)
print(100 * 6.2 - 70/3.5)
print(1 == 1)
print(1 == 2)
print(1 < 2)
print(5 * 20 >= 100/13)
print(43==23490)
x = 2
y = 5
z = x + y
print(x * 100)
print(z)
name = "Nick"
print(name)
print(16+16+15+15)

print(type(1))

a_number = 1 				# an integer
another_number = 5.1 		# a float
some_string = "Hello!" 		# a string
some_boolean = True 		# a boolean (notice the capitalization)
a_list = ["a bunch", "of", "stuff", a_number, some_string]
a_dictionary = {"key1": 10, "key2": "a string"} # a dictionary (key/value pairs)

people_at_table = 4	        # an integer
sandwiches_I_ate = 1.5 		# a float
best_friend = "Abbas" 		# a string
is_raining = False 		# a boolean (notice the capitalization)

print(people_at_table)

colors = ["blue", "pink", "turquoise", "sand"]
dark_blue = [10, 27, 56]
random_info = [people_at_table, sandwiches_I_ate, best_friend, is_raining]

print(colors[2])
print(dark_blue[0])
print(random_info[-1])


first_name = "Cardi"
last_name = 'B'

print(first_name)
print(last_name)

name = "Cardi B"
first_letter = name[0]
print(first_letter)

second_letter = name[1]
print(second_letter)

last_letter = name[-1]
print(last_letter)

first_three_letters = name[0:3]
print(first_three_letters)

print(len("California"))

sentence = "I do what I like, I do, I do"
print("do" in sentence)
print("boss" in sentence)

sentence = "Now here's a little story I've got to tell About three bad brothers you know so well!"
uppercase = sentence.upper()
print(uppercase)


sentence = "  I need you, I want you to Come to me, ecstasy (uh) Ecstasy, ecstasy, (uh) ecstasy (uh) Ecstasy, ecstasy, (uh) ecstasy (uh) Ecstasy, ecstasy, (uh) ecstasy (uh) Ecstasy, ecstasy, (uh) ecstasy (uh) Ecstasy You got sick thoughts? I got more of 'em You got a sister-in-law you'd smash? I got four of 'em Damn, those is your sisters You did somethin' unholy to them pictures Damn, you need to be locked up Nah, we need a bigger hot tub Now let me see you back, back, back, back Time to get the bag, bag, bag, bag We don't throw stones, we throw stacks That's why they goin' mad, mad, mad, Max If you don't say your name then I won't ask She got a smartphone, but a dumb ass I thought of all this on Ecstasy You got sick thoughts? I got more of 'em You remember bad bitches that you smashed? I recorded 'em She said fuck weed 'cause she love X If she suck seed, that's a success If a girl cum, that's a fuck fest And we gon' score 100 on this drug test Now let me see you back, back, back, back It's time to get the bag, bag, bag, bag We don't throw stones, we throw stacks That's why they goin' mad, mad, mad, Max If you don't say your name then I won't ask You got a smartphone, but a dumb ass I thought of all this on Ecstasy (perfect!) Fuckin' 'round whoop, scoop! Whoopity whoop Whoopity whoop, scoop poop woop toop Scoopity whoop loot, looty-whoop-whoop Ecstasy, ecstasy, ecstasy (uh, uh) You got sick thoughts? I got more of 'em Han? Scoop! You see them escorts? I escorted 'em, scooty-woot! While y'all was trippin', I resorted 'em, whoop! Then I kicked 'em out, I got bored of them, whoop! Now let me see you back, back, back, back It's time to get the bag, bag, bag, bag We don't throw stones, we throw stacks That's why they goin' mad, mad, mad, Max If you don't say your name then I won't ask You got a smartphone, but a dumb ass I thought of all this on Ecstasy  "


lowercase_sentence = sentence.lower()


titlecase_sentence = sentence.title()

stripped = sentence.strip()

less_poetic_sentence = sentence.replace("ecstasy", "pugs")

print(sentence);
print(lowercase_sentence)
print(titlecase_sentence)
print(stripped)
print(less_poetic_sentence)


# make an empty list
dreams = []

# add something to our list with the "append" method
dreams.append("flying dream") # the list will now look like this: ["flying dream"]

# add some more stuff
dreams.append("forgot something")
dreams.append("saw a friend from a long time ago")
dreams.append(100)
dreams.append("whatever")

print(dreams)
# ['flying dream', 'forgot something', 'saw a friend from a long time ago', 100, 'whatever']

# get the length of a list
# len(dreams)
#
# # you can access individual items in the list by referrring to their index value
# print dreams[0] # prints "flying dream"
# print dreams[2] # prints "saw a friend from a long time ago"
#
# # use negative numbers to start at the back
# print dreams[-1] # prints whatever - the last item
#
# # you can access part of a list with a ":"
# print(dreams[1:4])



# for (var i = 0; i < 3; i++) {
#     print(i);
# }

for x in range(0, 3):
  print(x)

text = open("61.txt", "r").read()
print(text.upper())

text_list = open("61.txt", "r").readlines()
# print(text_list)
print(text_list)

for abc in text_list:

    # print(abc)
    line_ = abc.strip()
    words = line_.split(" ") # Separates the lines by an empty space, getting a list of words

    print(words[0]) # Outputs the first word of each sentence

    # Chain it all together!
    print(words[0].center(30, '~').upper())

    print(abc.replace(" ", "eeeeeee"))
