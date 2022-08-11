
from enigma.machine import EnigmaMachine
import itertools
import string

TO_FIND = ["ENIGMA", "PANZER", "RATSEL", "CRYPTO", "BEFHL"]
EXTENDED_LIST = {}
machine = EnigmaMachine.from_key_sheet(
       rotors='II I V',
       reflector='A',
#        ring_settings='W H I',
       ring_settings='11 16 6',
       plugboard_settings='OZ VN MI AH LF DS GR BK XC UW')
def is_contain(str):
        for word in TO_FIND:
                if word in str: return True
        return False

def decrypt(machine, msg_key, cipher_text):
    machine.set_display(msg_key)    # use message key BLA
    return machine.process_text(cipher_text)


length = 3
for combinaison in itertools.product(string.ascii_uppercase, repeat=length):
        msg_key = ''.join(combinaison)
        str1 = decrypt(machine, msg_key, 'Cniuwi qxsjsh bmx Qwwjgh')
        str2 = decrypt(machine, msg_key, 'VypswfkvhhvfbwsOphszx')
        if is_contain(str1) or is_contain(str2): print(msg_key + " " + str1 +" "+str2)


print("DEBUG:")
machine.set_display('FDF')    # set initial rotor positions
enc_key = machine.process_text('Cniuwi           qxsjsh bmx Qwwjgh')      # encrypt message key
print("\n"+enc_key)

machine.set_display('FDF')    # set initial rotor positions
enc_key = machine.process_text('Cniuwi  qxsjsh bmx Qwwjgh')      # encrypt message key
print("\n"+enc_key)

machine.set_display('FDF')
enc_key = machine.process_text(enc_key)      # encrypt message key
print("\n"+enc_key)




"""

Reflector: 
        Name: Reflector A
        Model: None
        Date: None
        Wiring: EJMZALYXVBWFCRQUONTSPIKHGD
Rotor 1: 
        Name: II
        Model: Enigma 1
        Date: 1930
        Wiring: AJDKSIRUXBLHWTMCQGZNPYFVOE
        State: w
Rotor 2: 
        Name: I
        Model: Enigma 1
        Date: 1930
        Wiring: EKMFLGDQVZNTOWYHXUSPAIBRCJ
        State: h
Rotor 3: 
        Name: V
        Model: M3 Army
        Date: December 1938
        Wiring: VZBRGITYUPSDNHLXAWMJQOFECK
        State: i
Plugs: OZ VN MI AH LF DS GR BK XC UW

"""
