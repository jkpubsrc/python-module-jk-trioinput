#!/usr/bin/python3


import trio

import jk_console
import jk_console.demo
import jk_trioinput
import jk_json












async def animationLoop(effect):
	while True:
		await trio.to_thread.run_sync(effect.runLoopOnce)
		await trio.sleep(0.05)
#


async def inputLoop(history, cancel_scope):
	try:
		while True:
			s = await jk_trioinput.readConsoleInput("> ", 0, jk_console.Console.height()-2, syntaxHighlighter=None, history=history)
			s = s.strip()
			if not s:
				cancel_scope.cancel()
	except:
		cancel_scope.cancel()
#


async def run():
	jk_console.Console.clear()
	print("This is a demo to test if a loop with repeated activity and reading input from the console can be performed at the same time.") 

	history = jk_trioinput.ConsoleInputHistory()
	effect = jk_console.demo.Effect1(0, 4, jk_console.Console.width()*4//8, jk_console.Console.height()*2//8)

	async with trio.open_nursery() as nursery:
		nursery.start_soon(animationLoop, effect)
		nursery.start_soon(inputLoop, history, nursery.cancel_scope)

	print(jk_console.Console.RESET)
	print()
	return
#



trio.run(run)








