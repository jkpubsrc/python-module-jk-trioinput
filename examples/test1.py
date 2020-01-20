#!/usr/bin/python3


import trio

import jk_console
import jk_console.demo
import jk_trioinput
import jk_json












async def inputLoop(history, cancel_scope):
	try:
		while True:
			s = await jk_trioinput.readConsoleInput("> ", 0, jk_console.Console.height()-2, syntaxHighlighter=None, history=history)
			s = s.strip()
			if not s:
				cancel_scope.cancel()
			jk_console.Console.printAt(0, 5, "INPUT: " + repr(s) + " " * 20)
	except:
		cancel_scope.cancel()
#


async def run():
	jk_console.Console.clear()
	print("This is a demo to test asynchroneous input from the console.") 

	history = jk_trioinput.ConsoleInputHistory()

	async with trio.open_nursery() as nursery:
		nursery.start_soon(inputLoop, history, nursery.cancel_scope)

	print(jk_console.Console.RESET)
	print()
	return
#



trio.run(run)








