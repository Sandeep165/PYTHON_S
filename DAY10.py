#Nested dictionary
people = {
    1: {
        "name" : "Sam",
        "age" : 25,
        "city": "Mumbai",
        "P_id": 1256
    },
    2: {
        "name" : "Tom",
        "age" : 24,
        "city": "Pune",
        "P_id": 1254
    },
    3: {
        "name" : "John",
        "age" : 21,
        "city": "Delhi",
        "P_id": 8469
    },
    4 : {
        "fruits" : {
            1 : "Mango",
            2 : "Apple",
            3 : "Banana"
        },
        "cities" : {
            1 : "Mumbai",
            2 : "Pune",
            3 : "Delhi"
        }
    },

    "next" : {
        "name" : "curran",
        "age"  : 25,
        "location": "USA"
    },

    5 : {
        "one" : {
            "name" : "Ashiwn",
            "age"  : 23
        }
    }

}

# print(pepople)
# print(pepople[3]["P_id"]) #8469
# print(pepople[2]["age"]) #24
# print(pepople[4]["fruits"][2]) #apple
# print(pepople[4]["cities"][3]) #Delhi
# people["next"] = {}  
# people["next"]["name"] = "curran"
# people["next"]["age"] = 25
# people["next"]["location"] = "USA"

# people[5]={}
# people[5]["one"]={}
# people[5]["one"]["name"]="ashwin"
# people[5]["one"]["age"]=23

people[6] ={ 
    "name" : "john",
    "age" : 25,
    "city" : "mumbai"
}

# print(people)



dict1 = { 1 : 1, 2 : 4, 3 : 9, 4 : 16}

# print(dict1[4]) = 16



sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
# print(sampleDict['class']['student']['marks']['history'])


# city to location
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

# print(sampleDict.pop("city"))  #New york
sampleDict["location"] = sampleDict.pop("city") #newyork
# print(sampleDict)




'''
for i in range(10):
    print(i)
'''

# for i in range(0,10,1):
#     print(i)


# for i in range(0,11,3):
#     print(i)


# string = [1,2,3,4]
# integer = 123456

# for i in integer:
#     print(i)


# palindrome str..........palindrome num
# if name == name[::-1]

dict2 = { 1 : "one", 2 : "two"}
# for i,j in dict2.items():
#     print(i,j)

people = {
    1: {
        "name" : "Sam",
        "age" : 25,
        "city": "Mumbai",
        "P_id": 1256
    },
    2: {
        "name" : "Tom",
        "age" : 24,
        "city": "Pune",
        "P_id": 1254
    },
    3: {
        "name" : "John",
        "age" : 21,
        "city": "Delhi",   #3[city]  = "delhi"
        "P_id": 8469
    }
}

for id,info in people.items():
    print("\nPerson Id: ", id)
    for keys in info:
        print(keys  , info[keys])




