#!/usr/bin/python3


import jk_console
import jk_console.demo
import jk_json










jk_console.Console.clear()
print("This is a demo to test asynchroneous input from the console.") 

while True:
	jk_console.Console.moveCursorTo(0, 10)
	s = jk_console.Console.Input.readKey()
	if (not s) or (s == jk_console.Console.Input.KEY_CTRL_C):
		break

	jk_console.Console.printAt(0, 5, "INPUT: " + repr(s) + ", " + str(jk_console.Console.Input.ALL_KEYS_TO_KEY_NAME.get(s)) + " " * 20)
#










