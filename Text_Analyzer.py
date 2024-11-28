import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get the URL input for webpage analysis
URL = input("Enter your URL if you want analysis of a webpage (leave blank to skip): ")

# Check if URL is provided
if URL:
    try:
        # Fetch the webpage content
        html_data = requests.get(URL).text
        # Parse the webpage content
        soup = BeautifulSoup(html_data, 'html.parser')
        # Extract text from the webpage
        givenstring = soup.get_text()
        print("Webpage content fetched successfully.")
    except requests.exceptions.RequestException as e:
        print("Error fetching webpage:", e)
        givenstring = input("Enter Your Text for analysis instead: ")
else:
    givenstring = input("Enter Your Text for analysis: ")
                        
class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
    
    def freqOf(self,word):
        # get frequency map
        global freqDict
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0

analyzed = TextAnalyzer(givenstring)
word = input("Enter the word's frequency you want:")
count = analyzed.freqOf(word)
print("The word",word,"appears",count,"times.")
