#!/usr/bin/env python
# coding: utf-8

# task 1
# question number 1.1

# In[1]:


def myreduce(anyfunc, sequence):
  result = sequence[0] 
  for item in sequence[1:]:
   result = anyfunc(result, item)

  return result
def sum(x,y): return x + y
print ("Sum on list [1,2,3] using custom reduce function "   + str(myreduce(sum, [1,2,3])) )


# question number 1.2:

# In[2]:



def myfilter(anyfunc, sequence):

result = []
for item in sequence:
 if anyfunc(item):
  result.append(item)


return result




def ispositive(x):
if (x <= 0): 
 return False 
else: 
 return True
print ("Filter only positive Integers on list [0,1,-2,3,4,5] using custom filter function"  + str(myfilter(ispositive, [0,1,-2,3,4,5])))


# Q2

# In[3]:



#########
word = "ACADGILD"
alphabet_list = [ alphabet for alphabet in word ]
print ("ACADGILD => " + str(alphabet_list))

#########
input_list = ['x','y','z']
result = [ item*num for item in input_list for num in range(1,5)  ]
print("['x','y','z'] => " +   str(result))

#########
input_list = ['x','y','z']
result = [ item*num for num in range(1,5) for item in input_list  ]
print("['x','y','z'] => " +   str(result))

#########
input_list = [2,3,4]
result = [ [item+num] for item in input_list for num in range(0,3)]
print("[2,3,4] =>" +  str(result))

#########
input_list = [2,3,4,5]
result = [ [item+num for item in input_list] for num in range(0,4)  ]
print("[2,3,4,5] =>" +  str(result))

#########
input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print("[1,2,3] =>" +  str(result))


# Q3

# In[4]:


def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

print(find_longest_word(["PHP", "Exercises", "Backend"]))


# Task 2
# Q1.1

# In[ ]:





# Q1.2

# In[14]:


def filterlongword(string,number):

    for i in range(len(string)):
        listwords = []
        if len(string[i]) > number:
            listwords.append(string[i])

        return listwords 


def main():
    words = input("Please input the list of words: ")
    integer = eval(input("Please input an integer: "))

    words1 = filterlongword(words,integer)

    print("The list of words greater than the integer is",words1)

main()  


# Q2.1
# 

# In[6]:


wordlist = ["This", "is", "a", "beautiful", "day"]

def wordlength(wordlist):
 return list(map(lambda x: len(x), wordlist))

print ("word lengths in array => " + str(wordlength(wordlist)))


# Q2.2

# In[8]:


def vowel_check(char):
 if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
  return True
 else:
  return False

# Take user input
char = input("Enter character: ");

# If Invalid input, exit
if (char.isalpha() == False):
 exit();

# Invoke function
if (vowel_check(char)):
 print(char, "is a vowel.");
else:
 print(char, "is not a vowel."); 


# In[ ]:





# In[ ]:




