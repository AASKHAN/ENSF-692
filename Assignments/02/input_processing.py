# input_processing.py
# Adeel_Ahmed_Salman, ENSF 692 P24
# A terminal-based application for determining a course of action based on detected obstacles.

class Sensor:
    """
    A class used to represent the sensor status of a car's computer vision system.
    """

    def __init__(self, light='green', pedestrian='no', vehicle='no'):
        """
        Initializes the Sensor with default values.
        """
        self.light = light  # attribute light which is used for what color the traffic light is
        self.pedestrian = pedestrian  # attribute pedestrian which is used for whether a pedestrian is present or not
        self.vehicle = vehicle  # attribute vehicle which is used for whether a vehicle is present or not

    def update_status(self):
        """
        Updates the status of the sensor based on user input.
        """
        print("Are changes detected in the vision input?")  # prints the initial line

        try:
            change = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")  
            # change asks for the initial change from the default settings

            if change not in ["0", "1", "2", "3"]:
                raise ValueError
            else:
                if change == "1":  # evaluates the following code when the user inputs 1
                    input_1 = input("What change has been identified? (green, yellow, red): ").lower()
                    if input_1 in ["green", "yellow", "red"]:  # ensures the input is one we were expecting
                        self.light = input_1
                    else:
                        print("Invalid vision change \n")  # lets the user know the input is not allowed
                elif change == "2":  # evaluates the following code when the user inputs 2
                    input_2 = input("What change has been identified? (yes, no): ").lower()
                    if input_2 in ["yes", "no"]:  # ensures the input is one we were expecting
                        self.pedestrian = input_2
                    else:
                        print("Invalid vision change \n")  # lets the user know the input is not allowed
                elif change == "3":  # evaluates the following code when the user inputs 3
                    input_3 = input("What change has been identified? (yes, no): ").lower()
                    if input_3 in ["yes", "no"]:  # ensures the input is one we were expecting
                        self.vehicle = input_3
                    else:
                        print("Invalid vision change \n")  # lets the user know the input is not allowed
                elif change == "0":
                    print("\n")
        except ValueError:
            print("You must select either 0, 1, 2, 3")
            return "null"
        return change

def print_message(sensor):
    """
    Prints the action message based on the current sensor status.
    """
    if sensor.light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":  
        # prints stop if the conditions are as set
        print("\n STOP \n")
    if sensor.light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle == "no":  
        # prints caution if the conditions are as set
        print("\n Caution \n")
    if sensor.light == "green" and sensor.pedestrian == "no" and sensor.vehicle == "no":  
        # prints proceed if the conditions are as set
        print("\n Proceed \n")

def main():
    """
    Main function to run the car vision detector processing program.
    """
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")

    vehicle_sensor = Sensor()  # makes an object of the class Sensor
    user_entry = " "  # initially sets user_entry

    while True:
        user_entry = vehicle_sensor.update_status()  
        # if true then the user_entry is updated to vehicle_sensor object with method update_status()
        if user_entry == "0":
            break  # breaks the program if the user enters 0
        elif user_entry != "null":
            print_message(vehicle_sensor)  # prints the vehicle_sensor object
            print("Light = " + vehicle_sensor.light + ", " + "Pedestrian = " + 
                  vehicle_sensor.pedestrian + ", " + "Vehicle = " + vehicle_sensor.vehicle + "\n")  
            # prints the updated status

if __name__ == '__main__':
    main()  # runs the main function if the script is executed directly
