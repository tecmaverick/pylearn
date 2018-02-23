#A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. Let us get to it step by step

def my_name(name, time_of_day):
	def morning():
		print "Hi {} Good Morning!".format(name)

	def evening():
		print "Hi {} Good Evening!".format(name)

	def night():
		print "Hi {} Good Night!".format(name)

	if time_of_day == "morning":
		return morning
	elif time_of_day == "evening":
		return evening
	elif time_of_day == "night":
		return night
	else:
		return morning

greet_morning = my_name("Alfred","morning")
greet_noon = my_name("Andrew","evening")
greet_evening = my_name("Philip","night")

greet_morning()
greet_noon()
greet_evening()
