No developer writes perfect code all the time. One thing you should expect is that your code won't always work as expected. This lesson will show you how to read error messages that are output to the Terminal and how to identify the code that caused the error. Debugging is something we'll be using throughout the course, so by the time you complete it, you'll be quite adept at finding and fixing bugs in your code. In this lesson, I'll also show you how to get the most out of debugging with Google and StackOverflow.

How to read errors in Python
When I first copied over the poem into printing.py, I forgot to close out one of the lines with a parenthesis ). That led to the following error:

Command Line

SyntaxError: Missing parenthesus in call to 'print'
One-Months-Mac-mini-python mattangriffel$ python printing.py
File "printing.py", line 10
print ("then wisdom")
SyntaxError: invalid syntax
Sometimes error messages are clear, sometimes they are not. This error message is scary, but let’s check it out.

The first line tells you the file name and what line it thinks the error is on:

Command Line

One-Months-Mac-mini:python mattangriffel$ python printing.py
file "printing.py", line 10
The next line is the code in the file from this script and the ^ shows you where it thinks the error is. And the final line is the actual error message (you can use this to look up more information).

How to troubleshoot using StackOverflow
Whenever you get stuck, Google your error and see if you can find the solution on StackOverflow.

Here's how to get the most out of StackOverflow:

1. Search Google for the error message ("SyntaxError: invalid syntax").

2. Click on the link for Stack Overflow: The parentheses in the line before your error line is unmatched.

And indeed, if we look back into the code, we can see there's a missing parenthesis on line 9, which was carried forward onto the next line.

In the printing.py you will see:

print("my blood approves")
print("and kisses are a better fate"
print("then wisdom")
Remember, as you correct errors, always remember to save the Sublime file before you try running the code again.

To put it in perspective how much developers rely on StackOverflow, check out this joke from Reddit's /ProgrammingHumor. 