def dashboard():
    print("\nWelcome to Temperature Converter! 🌡️")
    print("Select the target degree:")
    print("1. Fahrenheit")
    print("2. Celsius ")
    print("3. Exit Program")  

while True:
    dashboard()
    choice = input("Choose an option (1, 2, or 3): ").strip()
    if choice=="1":
        celsisus=float(input("enter the celsisus degrees to converte "))
        fahrenheit=(celsisus *1.8)+32
        print(f" the converted temperature from {celsisus}°C to {fahrenheit}°F ")
    elif choice=="2": 
        fahrenheit=float(input("enter the fahrenheit degrees to converte "))
        celsisus=(fahrenheit-32)/1.8
        print(f" the converted temperature from {fahrenheit}°F to {celsisus}°C ")
    elif choice=="3":
        print("successfully exited 😊")
        break
    else:
        print("please select valid options ")

        
        