def body_info():
	height= float(input("what is your weight?(inches or meters)"))
	weight= float(input("what is your weight? (pounds or killograms)"))
	system=input("are you measured on metric or imperial?").lower().strip()
	return (height, weight, system)
	
def calculate_bmi(height,weight,system="metric"):
	if system=="metric":
		bmi=weight/(height**2)
	else:
		bmi=703*(weight/(height**2))
    return bmi	
while True:
	if system.startswith('m'):
		bmi=calculate_bmi(weight,system=system,	height=height)
		print(f"your bmi is {bmi}")
		break
	if system.startswith('i'):
		bmi=calculate_bmi(weight,height)
		print(f"your bmi is {bmi}")
		break
	else:
		print("please use imperial or metric.")