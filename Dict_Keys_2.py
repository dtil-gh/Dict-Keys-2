name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)

di = dict() # create empty dict

for lin in handle: # interate through each line in the file
    line = lin.strip() # strip whitespaces
    words = lin.split() # split lines into words and assign it a variable
    for wrd in words: #loop through each word
        if wrd == "From": # conditional that looks for the word From
            time = words[5] #look until we find the hour on index 5
            hour = time[0:2] #split the hour from the minutes onword
            di[hour] = di.get(hour, 0) + 1 #add the hours to the dict with a counter each time it  finds the word

dic = sorted(di.items()) #variable to sort the dict and creats a tuple with .items() in acending order

for k,v in dic: #go through each k and value in the dict
    print(k,v) #print out each key and value
