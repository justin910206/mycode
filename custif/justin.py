connection = float(input("Who is your cell phone provider?"))

if connection == Verizon:
    message = message + 'the best in the world.'
elif connection == Sprint:
    message = message + 'the worst in the state of WA.'
elif connection == Tmoblie:
    message = message + 'ok, but not great.'
else:
    message = message + 'bad and should be Verizon.'
print(message)
