#!/usr/bin/python3

value=1
print('The value is {:#010b}'.format(value))
notvalue=~value&0xff # not and mask off higher bits to avoid negation
print('The notvalue is {:#010b}'.format(notvalue))

# turn off all switches

value=0
print('The value is {:#010b}'.format(value))
notvalue=~value&0xff
print('The notvalue is {:#010b}'.format(notvalue))

# turn on the second switch

value=value|(1<<2)
print('The value is {:#010b}'.format(value))
notvalue=~value&0xff
print('The notvalue is {:#010b}'.format(notvalue))

# now also turn on the fourth switch

value=value|(1<<4)
print('The value is {:#010b}'.format(value))
notvalue=~value&0xff
print('The notvalue is {:#010b}'.format(notvalue))

# If I do the same thing again, nothing bad happens; switch 5 stays on

value=value|(1<<4)
print('The value is {:#010b}'.format(value))
notvalue=~value&0xff
print('The notvalue is {:#010b}'.format(notvalue))

# now turn off the third switch

value=value&(~(1<<2))
print('The value is {:#010b}'.format(value))
notvalue=~value&0xff
print('The notvalue is {:#010b}'.format(notvalue))

# If I do the same thing again, nothing bad happens, switch 3 stays off

value=value&(~(1<<2))
print('The value is {:#010b}'.format(value))
notvalue=~value&0xff
print('The notvalue is {:#010b}'.format(notvalue))

# Conclusion:  here's a class for the switches

class switches:
    def __init__(self,value=0):
        self.value=value
    def turn_on(self,switch):
        self.value=self.value|(1<<switch)
    def turn_off(self,switch):
        self.value=self.value&(~(1<<switch))
    def all_off(self):
        self.value=0
    def all_on(self):
        self.value=0xff
    def get_switches(self):
        notvalue=~self.value&0xff
        return(notvalue)
    def set_switches(self,value=0):
        self.value=value

my_switches=switches(7) # 7 in binary is 111; would turn on first three switches
print('The switches are {:#010b}'.format(my_switches.get_switches()))
my_switches.all_off()
print('The switches are {:#010b}'.format(my_switches.get_switches()))
my_switches.all_on()
print('The switches are {:#010b}'.format(my_switches.get_switches()))
my_switches.all_off()
print('The switches are {:#010b}'.format(my_switches.get_switches()))
my_switches.turn_on(3)
print('The switches are {:#010b}'.format(my_switches.get_switches()))
my_switches.turn_on(4)
print('The switches are {:#010b}'.format(my_switches.get_switches()))
my_switches.turn_off(1)
print('The switches are {:#010b}'.format(my_switches.get_switches()))
my_switches.turn_off(4)
print('The switches are {:#010b}'.format(my_switches.get_switches()))
my_switches.turn_on(0)
print('The switches are {:#010b}'.format(my_switches.get_switches()))
my_switches.set_switches()
print('The switches are {:#010b}'.format(my_switches.get_switches()))
my_switches.set_switches(7)
print('The switches are {:#010b}'.format(my_switches.get_switches()))
