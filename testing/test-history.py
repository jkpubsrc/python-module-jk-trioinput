#!/usr/bin/python3



from jk_testing import Assert
from jk_trioinput import ConsoleInputHistory




h = ConsoleInputHistory()

h.append("123")
h.append("wieu")
h.append("LODJFKJHS")
h.resetCursor()

Assert.isEqual(h.prev(), "LODJFKJHS")
Assert.isEqual(h.prev(), "wieu")
Assert.isEqual(h.next(), "LODJFKJHS")
Assert.isEqual(h.prev(), "wieu")
Assert.isEqual(h.prev(), "123")
Assert.isEqual(h.next(), "wieu")
Assert.isEqual(h.prev(), "123")
Assert.isEqual(h.prev(), None)
Assert.isEqual(h.next(), "wieu")
Assert.isEqual(h.next(), "LODJFKJHS")
Assert.isEqual(h.next(), None)




h = ConsoleInputHistory()

h.append("123")
h.append("wieu")
h.append("LODJFKJHS")
h.resetCursor()

h.append("LODJFKJHS")
Assert.isEqual(len(h), 3)







print("Success.")


