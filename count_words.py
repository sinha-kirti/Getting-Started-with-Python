#Dated: 08-October-2016

# In this progam a string and a number was given as input and you have to find
# the top n elements of string

from collections import Counter
import operator
def count_words(s,n):
    d=Counter(s.split())
    # counts the occurence of each word in s, if s.split() is not taken as argument instead of s, we would have got no.of occurence of alphabets
    a=sorted(sorted(d.items(), key = lambda x : x[0]), key = lambda x : x[1], reverse = True) 
    # this function sorts the tuples in d based on multiple attributes, both occurence and alphabetically in case of ties
    top_n=a[:n]
    # gives first n elements of collection
    return top_n

print count_words("betty bought a bit of butter but the butter was bitter",3)
print count_words("cat bat mat cat bat cat", 3)

#output should be [('butter', 2), ('a', 1), ('betty', 1)]
#s = sorted(s, key = operator.itemgetter(1, 2))
