import json  
  

#方法一  
# with open('config.json','r') as f:  
#     data = json.load(f) 
# print(data)


#方法二
file = open('config.json','r')
#data = json.load(file)
data = file.read()
print(data)
file.close()