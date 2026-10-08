# Week 1.2, Session 2: Task 6

operational_status = int(input("Please enter the operational status of the machine. 1 for operational. 0 for stopped. "))

if operational_status == 1:

    temperature = int(input("Please enter the temperature of the machine in Celsius. "))
    pressure = int(input("Please enter the pressure of the machine in PSI. "))


    if temperature > 80:
        temperature_status = "unsafe"

    elif temperature <= 80 and temperature >= 50:
        temperature_status = "normal"

    elif temperature < 50:
        temperature_status = "safe"


    if pressure > 100:
        pressure_status = "unsafe"
    elif pressure <= 100 and pressure >= 70:
        pressure_status = "normal"
    elif pressure < 70:
        pressure_status = "safe"


    if operational_status == 1:
       if pressure_status == "unsafe":
          print ("High pressure has been detected. Please conduct maintenance as soon as possible.")
       elif pressure_status == "normal":
            print ("The pressure is currently stable.")
       elif pressure_status == "safe":
            print ("The machine currently has a low pressure. You do not need to do anything at this time.")
       if temperature_status == "unsafe":
            print ("The temperature within the machine is unsafe. Please shut down immediately.")
       elif temperature_status == "normal":
            print ("The temperature in the machine is within safe limits.")
       elif temperature_status == "safe":
            print ("The machine is at a low temperature. You do not need to do anything at this time.")
       if temperature_status == "unsafe" or pressure_status == "unsafe":
            print ("This machine is currently operating in unsafe conditions. If you continue operating this machine, it may become damaged. Please shut down immediately.")
       elif temperature_status != "unsafe" and pressure_status != "unsafe":
            print ("This machine is currently within safe limits.")

elif operational_status == 0:
   print ("This machine is not operating. You do not need to do anything at this time.")

else:
   print ("Invalid option. ")