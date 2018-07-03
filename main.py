import operator
from itertools import chain
from collections import defaultdict
import itertools
from collections import Counter
from collections import defaultdict

#add key to dictionary, sort by value#
def mykey(x):
    return x[1]

def test1():
    grades = {
        'sophia': 93,
        'steven': 65,
        'kitten': 80,
        'kitten1': 80,
        'puppy1': 80,
        'puppy': 82
    }

    #add a key to the grades dic#
    grades['panda'] = 77

    #sorted_dict = sorted(grades.items(), key=operator.itemgetter(1,0), reverse=True)
    result = []
    for key in grades.keys():
        value = grades[key]
        pair = (key, value)
        result.append(pair)

    #result.sort(key=lambda x: x[1], reverse=True)
    result.sort(key=mykey, reverse=True)
    return result

#################################################################################

#check if dictionary has certain key, and sum the values#
def key_exists(x):
    grades = {
        'sophia': 93,
        'steven': 65,
        'kitten': 80,
        'puppy': 82
    }
    if grades.has_key(x):
        print ("%s is a key in the grades dictionary" % (x))
    else:
        print ("%s is not a key in the grades dictionary"% (x))

    for key, grades[key] in grades.items():
        print key + " has a score of " +  str(grades[key])

    print "%s is the sum of everyone's grades" % (sum(grades.values()))

    return

#################################################################################

#append two or more dictionaries#
def append_dict(dict1, dict2):
    for key in dict1.keys():
         dict2[key] = dict1[key]
    return        

def test3():
    dic1 = {1:10, 2:20} 
    dic2 = {3:30, 4:40} 
    dic3 = {5:50, 6:60}
    dic4 = {}

    append_dict(dic1, dic4)
    append_dict(dic2, dic4)
    append_dict(dic3, dic4)        

    return dic4

#################################################################################

#input to dictionary, and calculate whatever math to the values, or just calculate values in a dictionary#
def create_dict():
    n = int(raw_input("input an integer: "))
    d = {}

    for x in range(1, n+1):
        d[x] = x*x
    print (d)
    return

def create_dict1():
    d = {}

    for x in range(1, 16):
        d[x] = x ** 2 
    print (d)
    return 

#################################################################################

#multiply values in a dict#
def sample_dict():
    fundict = {"data": 10, "data1": 6, "data2": 2, "data3": 2, "data4": 3}
    fundict.pop("data", None)

    result = 1
    for key in fundict.keys():
        value = fundict[key]
        result = result * value
    return result

#################################################################################

#map two lists and sort by key#
def mykey1(x):
    return x[0]

def map_two_lists():
    result = []
    keys = ['season1', 'season2', 'season3', 'season4']
    colors = ['winter', 'spring', 'summer', 'autumn']

    seasons_dict = dict(zip(keys, colors))

    for key in seasons_dict.keys():
        value = seasons_dict[key]
        pair = (key, value)
        result.append(pair)

    result.sort(key=mykey1, reverse=False)
    return result

#################################################################################

#max and min#
def max_min():
    fundict = {"data": 10, "data1": 6, "data2": 2, "data3": 2, "data4": 3}

    maximum = max(fundict, key=fundict.get)  
    minimum = min(fundict, key=fundict.get)
    print(maximum, fundict[maximum])
    print(minimum, fundict[minimum])
    return

#################################################################################

#class#
class A(object):
    def __init__(self):
        self.p = 'Paris'
        self.l = 'London'
        self.n = 'New York'
        self.b = 'Boston'
        return
a = A()

#################################################################################

#remove dup#
def remove_dup():
    input_raw = {"steven": 
             {'fav food': ['noodles'], 
             'hobby': ['hiking'], 
            },
            "sophia": 
            {'fav food': ['tomato and egg'], 
             'hobby': ['traveling'], 
            },
            "kitten": 
             {'fav food': ['fish'], 
              'hobby': ['playing']
            },
            "steven": 
            {'fav food': ['noodles'], 
             'hobby': ['hiking']
            }
}
    result = {}

    for key, value in input_raw.items():
        if value not in result.values():
            result[key] = value
    return result 

#################################################################################
 
#check if dict is empty#
def test_dict_empty():
    test_dict = {}

    if len(test_dict) == 0:
        print "Dictionary is empty."
    else:
        print "Dictionary is NOT empty."
    return

#################################################################################

 #print all unique values in a dictionary# 
def unique_values():
    lis = [{"abc":"movies"}, {"abc": "movies"}, {"xyz": "movies"}, {"pqr":"news"}, {"pqr":"sports"}]
    s = set(val for dic in lis for val in dic.values())

    for x in s:
        print x
    return

#################################################################################

#create and display all combinations of letters, selecting each letter from a different key in a dictionary#
def combination():
    sample_data =  {'1':['a','b'], '2':['c','d']}
    for combo in itertools.product(*[sample_data[k] for k in sorted(sample_data.keys())]): 
        print ''.join(combo)
    return 

#################################################################################

#find the highest 3 values in a dictionary#
def highest_values():
    sample_dic = {'A': 23, 'B': 14, 'C.': 21, 'D': 2, 'E': 5}

    sorted_dict = sorted(sample_dic.items(), key=operator.itemgetter(1), reverse=True)[:3]

    return sorted_dict

#################################################################################

#combine two dictionary adding values for common keys#      
def combine_dict():
    d1 = {'a': 100, 'b': 200, 'c':300}
    d2 = {}
    d2['a'] = 300
    d2['b'] = 200
    d2['d'] = 400
    d3 = {}

    for key in set(d1.keys() + d2.keys()):
        v = 0
        if key in d1:
            v += d1[key]
        
        if key in d2:
            v += d2[key]

        d3[key] = v    

        #d3[key] = d1.get(key, 0) + d2.get(key, 0)
    return d3

#################################################################################

#combine values in python list of dictionaries#
def combine_values():
    sample_data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    result = {}
    for item in sample_data:
        key = item['item']
        v = item['amount']
        if key in result:
            v += result[key]
        result[key] = v

    print(result)

    myresult = []
    for key in result.keys():
        item = {}
        item['item'] = key
        item['amount'] = result.get(key)
        myresult.append(item)

    print(myresult)    
    return

#################################################################################

#create dictionary from a string#
def string_dict():
    test_string = '     A -   13  , B - 14, C - 29, M - 99'

    items = test_string.split(',')
    #print items
    
    result = {}
    for item in items:
        pair = item.split(' - ')
        key = pair[0].strip()
        value = pair[1].strip()
        result[key] = int(value)

    print result   
    return 

#################################################################################

#print dictionary in table format#
def table_dict():

    dataset =[{'Major': 'Computer Science', 'GPA': '3.1', 'Name': 'Steven'}, 
    {'Major': 'English Literature', 'GPA': '3.7', 'Name': 'Sophia'}, 
    {'Major': 'Physics', 'GPA': '3.5', 'Name': 'Kitten'}]

    line = "name    major     GPA"
    print(line)
    print("==============================")
    for record in dataset:
        line = "%s  %s    %s" % (record['Name'], record['Major'], record['GPA'])
        print(line)
    return     

#################################################################################

#count the values associated with key in a dictionary#
def count_values():

    sample_list = [{'id': 1, 'success': True, 'name': 'Makoto'}, 
    {'id': 2, 'success': False, 'name': 'Usagi'},
    {'id': 3, 'success': True, 'name': 'Rei'}]

    result = 0
    for record in sample_list:
        if record['success']:
            result = result + 1
        else:
            result 

    return result

#################################################################################

#convert a list into a nested dictionary of keys#
def convert_list():
    mylist = ['a','b','c','d']
    result = current = {}

    for x in mylist:
        current[x] = {}
        current = current[x]
    
    return result

#################################################################################

#sort a list alphabetically in a dictionary#
def sort_list():
    random_dict={'list1': ['b', 'a', 'c'], 'list2': ['f', 'a', 'e'], 'list3': ['c', 'b', 'a']}

    #for key in random_dict.keys():
        #value = random_dict[key]
        #value.sort()

    for _, value in random_dict.items():
        value.sort()

    print random_dict
    return 

#################################################################################

#remove spaces from dictionary keys#
def remove_spaces():
    random_dict = {'C         14': ['15263808', '13210478'], 'W   1': ['13122205']}

    result = {}
    for key in random_dict.keys():
        value = random_dict[key]
        pair = (key, value)
        key = pair[0].replace(" ", "")
        result[key] = value

    return result

#################################################################################

#get the top three items in a dict#
def top_three():
    sample_data = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

    #sorted_dict = sorted(sample_data.items(), key=operator.itemgetter(1), reverse=True)[:3]
    mylist = []
    for key in sample_data.keys():
        v = sample_data[key]
        pair = (key, v)
        mylist.append(pair)

    print(mylist)

    mylist.sort(key=lambda x: x[1], reverse=True)

    result_dict = {}
    for i in range(3):
        pair = mylist[i]
        k = pair[0]
        v = pair[1]
        result_dict[k] = v    

    print(result_dict)
    return

#################################################################################

#get the key, value and count in a dictionary#
def count_each():
    dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

    line = "key  value  count"
    print(line)

    for count, (key, value) in enumerate(dict_num.items(), 1):
        line = "%s    %s    %s" % (key, value, count)
        print line
    return

#################################################################################

#print a dictionary line by line#
def line_by_line():
    cars = {'A':{'speed':70,'color':2},
            'B':{'speed':60,'color':3}}

    for x in cars:
        print(x)
        for y in cars[x]:
            print (y +': ' + str(cars[x][y]))
    return

#################################################################################

#check multiple keys exists in a dictionary#
def check_keys():
    fruits = {'apple': 1, 'orange': 2, 'banana': 3}

    if 'orange' in fruits or 'melon' in fruits:
        print('one or more key exists in the dictionary')
    else:
        print('both keys don\'t exist in the dictionary')
    return 

#################################################################################

#count number of items in a dictionary value that is a list#
def count_items():
    breakfast = {'B': ['eggs', 'sausage', 'milk']}
    
    result = {}
    for key in breakfast.keys():
        vlist = breakfast[key]
        count = len(vlist)
        result[key] = count

    print(result)
    return

#################################################################################

#sort Counter by value#
def sort_counter():
     scores = Counter({'Math': 90, 'Physics': 80, 'Chemistry': 87, 'English Literature': 98})
     y = scores.most_common()
     return y

#################################################################################

#create a dictionary from two lists without losing duplicate values#
def two_lists_dict():
    
    alist = ['key1','key2','key3','key3','key4','key4','key5']
    blist=  [30001,30002,30003,30003,30004,30004,30005]

    two_lists = zip(alist, blist)
    print(two_lists)

    result_dict = {}
    #for i in range(len(two_lists)):
    for pair in two_lists:
        #pair = two_lists[i]
        key = pair[0]
        value = pair[1]
        if key in result_dict:
            result_dict[key].append(value)
        else:
            result_dict[key] = [value]
    
    print(result_dict)
    return     

#################################################################################

#replace dictionary values with their sum#
def dict_sum():
    lst = [   {'id' : 1, 'v1' : 1, 'v2' : 2},
              {'id' : 2, 'v1' : 3, 'v2' : 4},
              {'id' : 3, 'v1' : 5, 'v2' : 6}    ]

    for d in lst:
        v1 = d.pop('v1')
        v2 = d.pop('v2')
        d['v'] = v1 + v2
    
    return lst

#################################################################################

#match key and values in two dictionaries#

def match_key():
    x_dict = {'key1': 1, 'key2': 3, 'key3': 2}
    y_dict = {'key1': 1, 'key2': 2}

    for key, value in set(x_dict.items()) & set(y_dict.items()):
        if x_dict[key] == y_dict[key]:
            print '%s: %s is present in both x and y' % (key, value)

    return 


#################################################################################

def main():
    #print "hello world"
    #print test1()
    #print test3()
    #key_exists("puppy")
    #create_dict()
    #create_dict1()
    #print sample_dict()
    #print map_two_lists()
    #max_min()
    #print a.__dict__
    #print remove_dup()
    #test_dict_empty()
    #print combine_dict()
    #unique_values()
    #combination()
    #print highest_values()
    #combine_values()
    #string_dict()
    #table_dict()
    #print count_values()
    #print convert_list()
    #sort_list()
    #print remove_spaces()
    #top_three()
    #count_each()
    #line_by_line()
    #check_keys()
    #count_items()
    #print sort_counter()
    #two_lists_dict()
    #print dict_sum()
    match_key()
    return

if __name__ == "__main__":
    main()