
package to interact with AR488 interface boards, adds a bit of abstraction to simplify interactions. also can be passed as an argument cto custom classes to isentify instruments in your code like :

    class HP3468A:
        def __init__(gpib_addrs:int, interface:AR488):
            self.address = gpib_addrs
            self.interface = interface

        def read_measurement():
            return self.interface.read()


    my_awesome_interface = AR488('COM5')  # open the interface
    my_swesome_meter = HP3468A(22 , my_awesome_interface)  # create the interument object

    reading = my_awesome_meter.read_measurement()  #read measurement
    print(reading)