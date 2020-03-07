def ask():
	while True:
		try:
			user_input = input("please provide a number or type 'exit': ")
			if user_input == 'exit':
				print("Thank you for using our calculator")
				break
			result = int(user_input)
		except:
			print('whoops! this is not a number. try again')
			continue
		else:
			print("your number is squared",result**2)
			continue
		finally:
			("im going to ask you again")
ask()
