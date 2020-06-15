#Python help resource by LS

*STRINGS*

    Indexing
        my_string = "apple pie"
        my_string[1]  --> 'p'


    Negative indexing
         a  p  p  l  e     p  i  e
        -9 -8 -7 -6 -5 -4 -3 -2 -1
        last_character = my_string[-1]


    Slicing
        my_string[0:3]  --> 'app'
        my_string[:5]  --> 'apple'  ( same as [0:5] )
        my_string[5:]  --> ' pie'
        my_string[:]  --> 'apple pie'
        
        my_string[-9:-6]  --> 'app'
        my_string[-9:0]  --> ''   (out of bound)
  
    
    Converting string
        name = "Pickard"
        name.lower() --> 'pickard'  / "Pickard".lower() does the same
        name.upper() --> 'PICKARD'
        
        len(name) = 7
 
    
    Remove whitespace from a string. From end or from start
        name = '   Pickard   '
        name.rstrip() --> '   Pickard'
        name.lstrip() --> 'Pickard   '
        name.strip() --> 'Pickard'
  
   
   Starts or ends with
        my_string = 'apple pie'
        my_string.startswith('app') --> True
        my_string.endswith('e') --> True
    
    
    User Input
        prompt = "What's up"
        user_input = input(prompt)  / when you run it you will see the prompt message with blinking cursos
    
    
    Converting Strings to Numbers
        num = input("Enter a number")
        doubled_num = float(num) * 2
        OR
        doubled_num = int(num) * 2
 
 
    Converting Numbers to Strings
        num = 10
        print("I'll eat" + str(num) + " pankaces")
        print("I'll eat" + str(10) + " pankaces")  / can be called directly on number
        print("I'll eat" + str(num1 - num2) + " pankaces")  / will work with operation on numbers too
    
    
    Print statemens
        print with f-strings
        name = "Zaphod"
        heads = 2
        arms = 3
        f"{name} has {heads} heads and {arms} arms --> 'Zaphod has 2 heads and 3 arms'
        
        arithmetic operations work inside { }
 

    Find a string in a string
        my_string = "it is a surprise"
        my_string.find("suprise") --> 8
        my_string.find("will not find it")  --> -1


    Replace a string in a string
        my_string = "it is a surprise"
        my_string.replace("surpise", "good day") --> "it is a good day"
        
        As string are immutable, you need to re-assign it to my_string if you want to store it there


    Additional resources
        To learn more, check out the following resources:
        https://realpython.com/python-string-formatting/
        https://realpython.com/python-string-split-concatenate-join/
        https://realpython.com/python-basics/resources/#recommended-resources
*NUMBERS and MATH*
    
    Integer, Float
        int("25")  --> 25
            integer to write in 2 ways: 1000000 or 1_000_000 both work
        float("1.25")  --> 1.25
            float to write in 3 ways: 1000000.0 or 1_000_000.0 or 1e6 all will work
        inf and -inf are keywords for infinity as float
   
    
    Check if Integer
        num = 2.5
        num.is_integer() --> False
        However
        num = 2.0 
        num.is_integer() --> True  / there is no fractional part of the number despite it is a float
    

    Arithmetic Operators and Expressions
        9 / 3 --> 3.0
        int(5.0 / 2)  --> 2  / removes floating point
        
        Integer division. / Take care with negative division, it rounds up!
        9 // 3 --> 3
        5.0 // 2 --> 2.0
        
        Exponents
        2 ** 3 --> 8
        
        Modulus operator / returns the remainder when dividing
        20 % 7 --> 6
        16 % 8 --> 0
        
        Round / Rounding ties to even: 
        When you round ties to even, you ﬁrst look at the digit one decimal
        place to the left of the last digit in the tie. If that digit is even, you
        round down. If the digit is odd, you round up. That’s why 2.5 rounds
        down to 2 and 3.5 round up to 4.
        round(2.3) --> 2
        round(2.7) --> 3
        round(2.5) --> 2
        round(3.5) --> 4
        round(3.14159, 3) --> 3.142
        
        Absolute values
        abs(3) --> 3
        abs(-5.0) --> 5.0
        
        Power function
        pow(2,3) --> 8
    
    
    Print numbers with style
        n = 1234.56
        print(f"The value of n is {n:,.2f}") --> 'The value of n is 1,234.56' 
            after n: , means to add ',' in the number and .2f means to show up to 2 decimal places with round. 
            The same to round to 2 decimal places.
   
        ratio = 0.9
        print(f"Ratio is {ratio:.1%}") --> Ratio is 90.0%
            .1% means to convert it to % with one decimal place   

    
    Additional resources
        https://realpython.com/python-data-types/
        https://realpython.com/python-rounding/
        https://realpython.com/python-basics/resources/#recommended-resources
*FUNCTIONS and LOOPS*
	Function
		def multiply(x, y): # Function signature
			"""Return the product of two numbers x and y."""
			#Function body
			product = x * y
			return product
			
		help(multiply) --> Return the product of two numbers x and y. / Prints what defined at the beginning of the function """   ...   """
	
		
	While loop
		n = 1
		while n < 5:
			print(n)
	
	
	For loop
		for letter in "Python":
			print(letter)
			
		for n in range(3):
			print("Python")
			
		for n in range(10, 20):  #starts with 10, last is 19
			print(n * n)
	
	
	For else Loops #useful for checking password user input
		phrase = "it marks the spot"
		for character in phrase:
			if character == "X":
				break
		else:     #only executed if the for loop completes without any break
			print("There was no 'X' in the phrase")  
			
		
		for n in range(3):
			password = input("Password: ")
			if password == "I<3Bieber":
				break
			print("Password is incorrect.")
		else:
			print("Suspicious activity. The authorities have been alerted.")
	
	
	Additional resources
		https://realpython.com/python-while-loop/
		https://realpython.com/python-for-loop/
		https://realpython.com/python-basics/resources/#recommended-resources
*CONDITIONAL LOGIC*
	Boolean operators
		>; <; >=; <=; !=; ==
	
	
	Logical operators
		1 < 2 and 3 < 4  --> True
		2 < 1 and 3 < 4  --> False
		
		1 < 2 or 3 < 4  --> True
		
		not True  --> False
		
		Operator Order of Precedence (Highest to Lowest)
			<, <=, ==, >= ,>
			not
			and
			or
			
			False == not True --> syntax error, because as == has higher precedence, than not
				Python tries to evaulate False == not, which is invalid syntax
				
	
	If
		if 2 + 2 == 4:
			print("correct")
		else:
			print("incorrect")
			
		if 2 + 2 == 4:
			print("correct")
		elif 2 + 2 > 4:
			print("still incorrect")
		elif 2 + 2 <4:
			print("still incorrect)
		else:
			print("incorrect")
			
		
	Break
		for n in range(0, 4):
			if n == 2:
				break  # break out of the loop
			print(n)
			
		print(f"Finished witn n = {n}")  --> 0 1 Finished with n = 2
	

	Continue
		for n in range(0, 4):
			if n == 2:
				continue # skip any remaining code in the loop and continue on the next iteration
			print(n)
			
		print(f"Finished witn n = {n}")  --> 0 1 3 Finished with n = 3
		
	
	Additional resources
		https://realpython.com/python-operators-expressions/#logical-operators
		https://realpython.com/python-conditional-statements/
		https://realpython.com/python-basics/resources/#recommended-resources
*EXCEPTIONS*
	Error Types
		ValueError  --> Trying to convert "not a number" to an int
		TypeError  --> Trying to add a string and an int
		Name Error  --> When using a variable name, which not defined
		ZeroDivisionError  --> 1 / 0
		OverflowError  --> When result of an arithmetic operation is too large
		
		
	Try and Except
		try: 
			number = int(input("Enter an integer: "))
		except ValueError:
			print("That was not an integer")
			
		
		def divide(num1, num2):
			try:
				print(num1 / num2)
			except (TypeError, ZeroDivisionError):
				print("encountered a problem")
		
		
		def divide(num1, num2):
			try:
				print(num1 / num2)
			except TypeError:
				print("type error")
			except ZeroDivisionError:
				print("zero division")
				
				
		try:
			#do a lot of hazardous things
		except:
			print("Something bad happened")
*RANDOM*
	import random
	random.randint(1, 10)
*TUPLES*
	Tuples are immutable
	Tuples don't require objects same type
		my_tuple = (1, 2, 3)
		empty_tuple = ()
		x = (1,)  --> tuple with one item
		tuple("Python")  --> ('P', 'y', 't', 'h', 'o', 'n')   #careful tuple() accepts only one parameter
		
		values = (1, 3, 5, 7, 9)
		values[2]  --> 5
		values[2:4]  --> (5, 7)  # creates a new tuple with two items
	
	Tuples are iterable
		for n in values:
			print(n)
	
	
	Packing and unpacking
		Packing
			coordinates = 4.21, 9.29  # list without parantheses, created a tuple
		
		Unpacking
			x, y = coordinates
			x  --> 4.21
			y  --> 9,29
			
		Packing and Unpacking combined
			name, age, occupation = "David", 34, "programmer"
			name  --> 'David'
			age  --> 34
			occupation  --> 'programmer'
			
			
	Checking existence
		vowels = ("a", "e", "i")
		"a" in vowels  --> True
		
		
	Returning Multiple Values From a Function
		def adder_subtractor(num1, num2):
			return (num1 + num2, num1 - num2)
			
		adder_subtractor(3, 2)  --> (5, 1)
		
		
	Namedtuple - useful to return function values
		#Just as effective as normal Tuples
		import collections
		Person = collections.namedtuple('Person', 'name age gender')
		bob = Person('Bob', 30, 'male')
		print(bob)  --> Person(name='Bob', age=30, gender='male')			
*LISTS*
	Lists are mutable
	Lists don't require objects same type
	colors = ["red", "yellow", "green", "blue"]
	list("Python") --> ['P', 'y', 't', 'h', 'o', 'n']
	
	List from string with split
		groceries = "eggs, milk, cheese"
		gorcery_list = groceries.split(", ")
		grocery_list --> ['eggs', 'milk', 'cheese']
		.split works in many ways: with " ", with ";", even with char sequence like 'abc'
		
		Important: the .split() return always one more element, than seperator found in list
			example
			"abbabbaba".split("c") --> ['abbabbaba']
		
		
	Basic list operators
		numbers[1, 2, 3, 4]
		numbers[1] --> 2
		numbers[1:3]  --> [2, 3]
		
		
	Checking existence
		numbers[1, 2, 3, 4]
		"Bob" in numbers --> False
		
		
	Lists are iterable
		numbers[1, 2, 3, 4]
		for number in numbers:
			print(number)
		
	
	Changing element in a list
		colors = ["red", "yellow", "green", "blue"]
		colors[0] = "burgundy"
		colors --> ['burgundy', 'yellow', 'green', 'blue']
		
		
	Changing several element in a list
		colors = ['burgundy', 'yellow', 'green', 'blue']
		colors[1:3] =["orange", "magenta"] #changes positions 1 and 2
		colors --> ['burgundy', 'orange', 'magenta', 'blue']
		
	
	Change and ADD
		colors = ["red", "yellow", "green", "blue"]
		colors[1:3] = ["orange", "magenta", "aqua"] #changes positions 1 and 2 and ADDS position 3, as the list is longaer than the slice
		colors --> ['red', 'orange', 'magenta', 'aqua', 'blue']
		
		
	Change and REMOVE
		colors = ['red', 'orange', 'magenta', 'aqua', 'blue']
		colors[1:4] = ["yellow", "green"] # changes positions 1 and 2 and REMOVES positions 3, as the list is shorter than slice
		colors --> ['red', 'yellow', 'green', 'blue']
		
		
	Insert
		Important: do not reassign the list. colors = colors.insert... will delete the list
		
		colors = ["red", "yellow", "green", "blue"]
		colors.insert(1, "orange")
		colors --> ['red', 'orange', 'yellow', 'green', 'blue']
		
		colors.insert(10, "violet") #index is larger than list len. It will insert at the end.
		colors --> ['red', 'orange', 'yellow', 'green', 'blue', 'violet'] 
		
		colors.insert(-1, "indigo") #inserts at last slot, which was violet. Violet is shifted one to the right!
		colors --> ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
		
	
	Pop
		Removes the element at the index and the value is returned by the method
		colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
		color = colors.pop(3)
		color --> "green"
		colors --> ['red', 'orange', 'yellow', 'blue', 'indigo', 'violet']
		
		colors.pop(-1) --> 'violet'
		colors --> ['red', 'orange', 'yellow', 'blue', 'indigo']
		
		colors.pop()  --> 'indigo'  #without index, it removes the last item
		colors --> ['red', 'orange', 'yellow', 'blue']
		
		
	Append
		Append adds one element at the end of the list
		colors = ['red', 'orange', 'yellow', 'blue']
		colors.append("indigo")
		colors --> ['red', 'orange', 'yellow', 'blue', 'indigo']
		
	
	Extend
		Extend used to add several new elements to the end of the list
		colors = ['red', 'orange', 'yellow', 'blue', 'indigo']
		colors.extend("violet", "ultraviolet")
		colors --> ['red', 'orange', 'yellow', 'blue', 'indigo', 'violet', 'ultraviolet']
		
		
	Copy a list
		Shallow copy. The references of the items are the same. You can append, but changing will change the original list!
		For Deep copy see other readings.
		animals = ["lion", "tiger", "frumious Bandersnatch"]
		large_cats = animals[:]
		large_cats.append("leopard")
		large_cats --> ['lion', 'tiger', 'frumious Bandersnatch', 'leopard']
		animals --> "lion", "tiger", "frumious Bandersnatch"]
		
		
	Sort a list - simple
		colors = ["red", "yellow", "green", "blue"]
		colors.sort()
		colors --> ['blue', 'green', 'red', 'yellow']
		
		numbers = [1, 10, 5, 3]
		numbers.sort()
		numbers --> [1, 3, 5, 10]
		
	
	Sort a list - with key
		Key accepts a function and the sorting is done based on the return value of the function
		Function can only accept one argument
		User defined function can be be passed as key function
		
		colors = ["red", "yellow", "green", "blue"]
		colors.sort(key=len)
		colors  --> ['red', 'blue', 'green', 'yellow']
		
		def get_second_element(item):
			return item[1]
		items = [(4, 1), (1, 2), (-9, 0)]
		items.sort(key=get_second_element)
		items  --> [(-9, 0), (4, 1), (1, 2)]
		
		
	Lists of Numbers - Built in methods
		sum([1, 2, 3, 4, 5]) --> 15
		min([1, 2, 3, 4, 5 ]) --> 1
		max([1, 2, 3, 4, 5 ]) --> 5
		
		
	Create list from existing iterable
		List comprehesion is a short hand for a loop
		
		numbers = (1, 2, 3, 4, 5)
		squares = [num**2 for num in numbers]
		squares --> [1, 4, 9, 16, 25]
		
		str_numbers = ["1.5", "2.3", "5.25"]
		float_numbers = [float(value) for value in str_numbers]
		float_numbers --> [1.5, 2.3, 5.25]
*DICTIONARIES*
	Create a dict
		#Key - value pairs. Mind the last "," !
		#Key can be any immutable type, but one dictionary can include different key types
		capitals = {
		"California": "Sacramento",
		"New York": "Albany",
		"Texas": "Austin",
		} 
	
	Create from a sequence of tuples
		key_value_pairs = (
		("California", "Sacramento"),
		("New York", "Albany"),
		("Texas", "Austin"),
		)
		capitals = dict(key_value_pairs)
		capitals  --> {'California': 'Sacramento', 'New York': 'Albany', 'Texas': 'Austin'}
	
	
	Create empty dictionary:
		1st method : {}
		2nd nethod: dict()
	
	
	Access element in dict
		capitals["Texas"]  --> 'Austin'
		
	
	Add  / Overwrite element
		# If the key existed before, then Python overwrites the value!
		capitals["Colorado"] = "Denver"
		
		
	Checking the Existence of Keys
		'Arizona' in capitals --> False
		'California' in capitals --> True
		
		
	Iterating over Dict
		for key in capitals:
			print(key)
	
		for state in capitals:
			print(f"The capital of {state} is {capitals[state]}")  -->
		The capital of California is Sacramento
		The capital of New York is Albany
		The capital of Colorado is Denver
		
		# .items() return a list of tuples of key-value pairs
		# These items are called dictitems
		# Iterating over with unboxing
		for state, capital in capitals.items():
			print(f"The capital of {state} is {capital}")  -->
		The capital of California is Sacramento
		The capital of New York is Albany
		The capital of Colorado is Denver
	
	
	Additional resources
		https://realpython.com/python-dicts/
*OOP*
	Classes
	Define a class	
		class Dog:
			#class attribute
			species = "this species"
			
			def __init__(self, name age):
				self.name = name
				self.age = age
			
			#instance methof
			def description(self):
				return f"{self.name} is {self.age} years old"
				
			# another instance method
			def speak(self, sound):
				return f"{self.name} says {sound}"
				
			#instead description better use __str()__
			def __str__(self):
				return f"{self.name} is {self.age} years old"
			
		
	Instanttiate a class
		buddy = Dog("Buddy", 9)
	
	Access instance attributes
		buddy.age = 9
		buddy.name = 'Buddy'
		
		
	Access class attributes
		buddy.species = "this species"
		
	
	Instance and class attributes can be modified dynamically
		buddy.age = 10
		buddy.age --> 10
		
		
	Call instance method
		buddy.description() --> "Buddy is 9 years old"
		buddy.speak("Woof woof")  --> "Buddy says Woof woof"
		
	
	Call __str()__ method of class
		print(buddy)  -- > "Buddy is 9 years old"
		
	
	Additional resources
		https://docs.python.org/3/tutorial/classes.html
		https://realpython.com/search?q=oop
		https://realpython.com/python-basics/resources/#recommended-resources
*MODULES*
	Modules are different *.py files
	A module has to be imported into another one to be used
	
	# adder.py
	def add(x, y):
		return x + y
		
	# main.py
	import adder  # import it always at the beginning 
	value = adder.add(2, 2)  #important to add the name of the module
	print(value)
	
	Variations of importing
		Import with changed name
		import adder as a  # from here on refer to adder as "a"
		
	Import only a portion of the namespace
		#after this you don't need "adder." before "add"
		# just call the function as it was an internal function of the module
		from adder import add, double # one or more functions		
*PATH*
		1. Windows: C:\Users\David\Documents\hello.txt  --> cannot enter path like this as \ is an escape character fro Python
		2. macOS: /Users/David/Documents/hello.txt
		3. Ubuntu Linux: /home/David/Documents/hello.txt
		
		import pahtlib
		#change windows path to raw string, then it works
		path = pathlib.Path(r"C:\Users\David\Desktop\hello.txt")
	
	
	Home directory
		#get home directory as path object
		home = pathlib.Path.home()
			Windows: C:\Users<username>
			macOS: /Users/<username>
			Ubuntu Linux: /home/<username>
			
			
	Current working directory
		pathlib.Path.cwd() --> WindowsPath(r"C:\Users\David\Documents")
		
	
	The "/" operator
		home / "Desktop" / "hello.txt"  --> WindowsPath('C:/Users/David/Desktop/hello.txt')
		
		
	Absolute and Relative Paths
		Relative paths
			# Relative Windows path
			path = pathlib.Path(r"Photos\image.jpg")
			# Relative macOS or Linux path
			path = pathlib.Path("Photos/image.jpg")
			
			path.is_absolute() --> False
			
		Absolute paths
			home = pathlib.Path.home()  --> WindowsPath('C:/Users/David')
			home / pathlib.Path(r"Photos\image.png")  --> WindowsPath('C:/Users/David/Photos/image.png')
		
		
	Parents
		# .parents attribute of a path object returns an iterable containing the list of directories of the path
		path = pathlib.Path.home() / "hello.txt"
		path  --> WindowsPath("C:\\Users\\David")
		# first item is the dir itself, last is the root
		list(path.parents)  --> [WindowsPath("C:\\Users\\David"), WindowsPath("C:\\Users"), WindowsPath("C:\\")]
		
		#Parents is iterable
		for directory in path.parents:
			print(directory)
			
		#Direct parent - one level up	
		#returns the direct parent as a string
		path.parent --> 'C:\Users\David'
		
	
	Anchor - get root
		# if the path is absolute, .path.anchor returns a string of root
		path.anchor --> 'C:\'
		# for relative strings, path.anchor returns an empty string
		
		
	Name
		# . name returns the name of the dir or file of the path
		home = pathlib.Path.home()
		# C:\Users\David
		home.name  --> 'David'
		path = home / "hello.txt"
		path.name  --> 'hello.txt'
		
		path.stem --> 'hello'
		path.suffix --> '.txt'
		
		
	Exists, is_file, is_dir
		# check whether a path exists
		path = pathlib.Path.home() / "hello.txt"
		path.exists() --> False
		
		path.is_file() --> True
		path.is_dir() --> False
*FILES*
	Python has 2 file types:
		Text
		Binary
		
	Path.open() method
		from pathlib import Path
		path = Path.home() / "hello.txt"
		path.touch() #creates the file
		file = path.open(mode="r", encoding="utf-8") #returns a file object.
		# important: .open() method keeps the file open until explicitely closed
		#to close the file
		file.close()
		
		mode:
			"r"	Creates a text file object for reading and raises an error if the file can’t be opened.
			"w"	Creates a text file object for writing and overwrites all existing data in the file.
			"a"	Creates a text file object for appending data to the end of a file.
			"rb"	Creates a binary file object for reading and raises an error if the file can’t be opened.
			"wb"	Creates a binary file object for writing and overwrites all existing data in the file.
			"ab"	Creates a binary file object for appending data to the end of the file
			
		encoding:
			"ascii"		ASCII
			"utf-8"		UTF-8
			"utf-16"	UTF-16
			"utf-32"	UTF-32
			
		
	open() Built-in method
		#difference to Path.open(): argument is string
		file_path = "C:/Users/David/hello.txt"
		file = open(file_path, mode="r", encoding="utf-8")
		file.close()
		
	
	Open files using WITH statement - Pythonic way
		#return value of the open() method is assigned to the variable after "as"
		#when code execution leaves the indented block, the file is closed automatically
		#closing happens even if any exception raised during the execution
		with path.open(mode="r", encoding=-"utf-8") as file:
			# Do something with file
			
		with open(file_path, mode="r", encoding="utf-8") as file:
			# Do something with file
		
		
	Read data from file
		path = Path.home() / "hello.txt"
		with path.open(mode="r", encoding="utf-8") as file:
			text = file.read()
			
		print(text) --> "Hello word!" #whole content of the file is saved in one string
		#lines are separated by "\n"
		
		
		#Read line by line
		with path.open(mode="r", encoding="utf-8") as file:
			for line in file.readlines():
				print(line)
				
		
	Write data to file
		Overwrite all
		with path.open(mode="w", encoding="utf-8") as file:
			file.write("Hi there!")
		#this will return the number of characters written, this case "9"
		
		#Important: when opening with "w" all data in file will be overwritten! 
		#This practically deletes the original file!
		#When opening with "w", if folder exists, but file not, it will create a new file
	
		
		Append to file
		with path.open(mode="a", encoding="utf-8") as file:
			file.write("\nHello")
		#this returns the characters written, this case "6"
		#new data is printed on new line, as "\n" is at the beginning of the input string
		
		
		Write multiple lines to file
			lines_of_text = [
				"hello line1\n",
				"hello line2\n",
				"hello line3\n",
			]
			with path.open(mode="w", encoding="utf-8") as file:
				file.writelines(lines_of_text)
			#Important, remember, that "w" will erase all previous data in file
			#writenlines() does not automatically insert lines to new line, that is why "/n"-s are present
			
			#When opening with "w", if folder exists, but file not, it will create a new file
*PIP*
	python3.8 -m pip install PackageName  #on linux you need to specify the exact python version, because many versions may be present at the same time
	


*GIT*
	DELETE a local repository:
		Enter in terminal the folder of the repo
		rm -rf .git --> this will delete the local repo, but not the files

	VSCode authentication failure
		Try SSH key generation first
		#Open in terminal the project folder
		git config credential.helper store #will sore user and pass in the folder
		#commit changes in VSCode (already committed one if push failed...)
		git pus <repository web address>  #it will ask for username and pass which it will store

	ONE TIME SETUP
		git config --global user.name "Jeff Call"
		git config --global user.email jeff.call.ch@gmail.com
		git config --global core.editor vscode # choose editor

	.GITIGNORE
		Create a file called: .gitignore 
		fill it with contenct from here: https://github.com/github/gitignore/blob/master/Python.gitignore

		If you want to add files, folder later to the .gitignore file and you need to update the repo follow this
			http://www.codeblocq.com/2016/01/Untrack-files-already-added-to-git-repository-based-on-gitignore/
			git rm -r --cached .  # . at the end is needed too. Command to clear cache. No files will be deleted
			git add . #add all files again
			git commit -m ".gitignore fix" #make a commit
			#after all push it in VSCode



			


	SSH Key
		If you don't have an ssh Key, generate one to drop user and pass auth
		https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
		ssh-keygen -t rsa -b 4096 -C "jeff.call.ch@gmail.com"
		#it will ask for file location and pass phrase. Hit ENTERs until code is generated

		Start teh ssh agentin the backgroud:
		 eval "$(ssh-agent -s)"  --> Agent pid xxxxx
		
		Add SSH private key to ssh-agent
		 ssh-add ~/.ssh/id_rsa  --> Identity added ... folder of ssh key
		
		ADD SSH key to github account
		https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account
		Follow instructions under the link
		$ sudo apt-get install xclip
		# Downloads and installs xclip. If you don't have `apt-get`, you might need to use another installer (like `yum`)
		$ xclip -sel clip < ~/.ssh/id_rsa.pub
		# Copies the contents of the id_rsa.pub file to your clipboard
		

		