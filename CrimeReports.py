#Reads tweets from a file and prints the id of each tweet
def task7():
    with open("CrimeReport.txt", "r") as f: # Opens file as f
        i = 1 # tweet id counter
        print "**********************************************************"
        while True: # loops until the end of the file
            line = f.readline() # sets the read line to the var line
            if not line: # if line is empty the loop is broken
                break
            
            tweet = dict() # Intialzes var tweet as a dictonary
            tweet = json.loads(line) # loads the string stored in line to tweet
            print "tweet id", i, ":", tweet['id'] # prints the tweet id number
            i += 1 # increments the counter

    f.close() # closes the file

# Uses the datetime import to compare times of tweets posted and print the 10 most recent ones
import datetime
def task8():
    tweets = [] # creates a list
    for line in open("CrimeReport.txt", "r").readlines(): # opens criem reports and reads the lines
        tweet = json.loads(line) # loads the current line into var tweet as a dict
        tweets.append(tweet) # appends tweet to tehe list tweets
        # sorts the list tweets based on the lime that they were created
        sorted_tweets = sorted(tweets, key = lambda tweet:
                               datetime.datetime.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +0000 %Y"))
        

    f = open('task8.data', 'w') # opens a file as f
    for tweet in sorted_tweets[-10:]: # Loops through the first 10 tweets in sorted_tweets
        f.write(json.dumps(tweet)) # writes the tweet as a string to f
        f.write('\n') # writes new line character
        
    f.close() # Closes the file

#Creates a new directory and creates files in that directory named after the date and hour the tweet was made
import os, shutil
def task9():
    tweets = [] # list called tweets
    tweets_times = [] # List of tweets_times
    for line in open("CrimeReport.txt", "r").readlines(): # Opens file and reades each line as a string
        tweet = json.loads(line) # Loads the line into the dict tweet
        tweets.append(tweet) # appends tweet to the list tweets
        
    i = 0 # counter for the index of tweets
    while i < len(tweets): # loops until the end of the list tweets is reached
        # Appends the datetime of the time the tweet was created to the lost tweets_times
        tweets_times.append(datetime.datetime.strptime(tweets[i]['created_at'], "%a %b %d %H:%M:%S +0000 %Y"))
        i += 1 # increments the index counter

    try:   # tries to make a new directory 
        os.makedirs("task9-output")

    except: # if directory already exsists it delets the directory and then makes a new one
        shutil.rmtree("task9-output")
        os.makedirs("task9-output")
        
    os.chdir("task9-output") # changes the current directory
    i = 0 # index
    while i < len(tweets_times): # loops until the end of the list
            month = str(tweets_times[i].month) # gets the month, day, year and hour the tweet was created and turns it into strings
            day = str(tweets_times[i].day)
            year = str(tweets_times[i].year)
            hour = str(tweets_times[i].hour)
            month_day_year_hour = month + "-" + day + "-" + year + "-" + hour + ".txt" # concatenates the month, day, year, and hour strings togther to make a txt file
            with open(month_day_year_hour, "a") as f: # opens the file as f for appending
                f.write(json.dumps(tweets[i])) # writes the tweet at i to the file
                f.write('\n') # writes a new line for formating

            f.close() # closes the file
            i += 1 # increments the index
            
    os.chdir('..') #returns to the parrent directory

# Preformes sentiment analysis on the text in the tweets and files them into the coresponding files
def task10():
    from pattern.en import sentiment # imports sentiment package from  pattern.en module
    f = open("positive-sentiment-tweets.txt", "w") # opens file f for writing 
    g = open("negative-sentiment-tweets.txt", "w") # opens file g for writing
    for line in open("CrimeReport.txt", "r").readlines(): # rads through the file
        tweet = json.loads(line) # loads the line read into the tweet dict
        sent_tuple = sentiment(tweet['text']) # calls the sentiemnt function on the text in the tweet dict and stores it into the a tuple
        if sent_tuple[0] >= 0: # CHecks the value in the sentiment tuple
            f.write(json.dumps(tweet)) # if equal to or greater than 0 it is positive and writes the tweet to file f
            f.write('\n')
        else: #Else it is negative and the tweet is writen to file g
            g.write(json.dumps(tweet))
            g.write('\n')

    f.close() # closes the files
    g.close()

# Calls all of the functions
if __name__ == '__main__':
    task7()
    task8()
    task9()
    task10()
