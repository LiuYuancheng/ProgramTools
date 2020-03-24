#---------------------------------------------------------------------------
# Q1[data structure]: What is data dictionary/ hash table ? 
# Is there a way to convert a string to integer without using program built- 
# in function?(Usually we use int(a))
a = '12'

#---------------------------------------------------------------------------
# Q2[data communication]: what is the difference TCP and UDP ? 
# If you wand to transfer a image() from UDP/TCP but the image size is bigger 
# that your buffer size, what will to send your image? 

import pickle
BUFFER_SZ = 4096    # TCP/UDP buffer size.
img = open("test.jpg", 'rb')
_ = len(img) = 24000
imgBytes = img.read()
data = pickle.dumps(imgBytes, 0)
sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# design the sender logic 

# design the receiver logic

#---------------------------------------------------------------------------
# Q3[Web design]: What's the difference between GET and POST method in HTTP?
# How do you create links to sections within the same page?




# Answers:


#---------------------------------------------------------------------------
# Q1 result: 
hashTable = {'1':1, '2':2, '3':3}
counter = 0
result = 0 
for char in a:
    result = result * 10 + hashTable[char]
# 
print(result)
#---------------------------------------------------------------------------
# Q3 answer:
<a name= 'bookmark'>
<a href="#bookmark">BACK TO TOP</a>