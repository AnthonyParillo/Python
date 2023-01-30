whatName = input('What is your Name?: ')
lengthName = 'Your Name is ' + str(sum(len(x) for x in whatName.split())) + ' Characters!'
print('\n' + lengthName)