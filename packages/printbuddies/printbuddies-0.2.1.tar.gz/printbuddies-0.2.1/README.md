# printBuddies

A few utilities to do terminal printing tricks. <br>
Install with <pre>python -m pip install git+https://github.com/matt-manes/printBuddies</pre>

Contains one class and three functions: ProgBar, printInPlace, ticker, and clear.<br>
<br>
ProgBar is a self-incrementing, dynamically sized progress bar.<br>
The progress counter and completion values can be manually overriden if desired.<br>
The width of the progress bar is set according to a ratio of the terminal width
so it will be resized automatically if the terminal width is changed.<br>
The display function has a 'returnObject' parameter, allowing ProgBar to be used in comprehensions.<br>
Basic usage:<br>
<pre>
from printBuddies import ProgBar
total = 100
progBar = ProgBar(total=total-1)
for _ in range(total):
    progBar.display()
progBar.reset()
myList = [progBar.display(returnObject=i) for i in range(total)]
</pre>
<br>
<br>
printInPlace erases the current line in the terminal and then writes the value of 
the 'string' param to the terminal.<br>
<pre>
from printBuddies import printInPlace
import time
#This will print numbers 0-99 to the terminal with each digit overwriting the last.
for i in range(100):
    printInPlace(i)
    time.sleep(0.1)
</pre>
<br>
ticker prints a list of strings to the terminal with empty lines above and below
such that previous text in the terminal is no longer visible.<br>
Visually, It functions as a multi-line version of printInPlace.<br>
<pre>
from printBuddies import ticker
import time
#This will produce visually the same output as the above example
for i in range(100):
    ticker([i])
    time.sleep(0.1)
</pre>
<br>
A call to clear() simply clears the current line from the terminal.
