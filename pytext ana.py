# Python 3 code for text mining using Textblob library.
from textblob
import Textblob

y=input("Type your sentence")

edu=TextBlob(y)

x=edu.sentiment.polarity

if x<0:
   
 print("Negative")

  elif x=0:
     
 print("Neutral")

else print("Positive")