import collections
import os
pets={}
b=1

def printMenu():
	    print('введите число согласно меню')
	    print('добавить питомца 1')
	    print('найти данные по питомцу 2')
	    print('обновить данные о питомце 3')
	    print('удалить питомца 4')
	    print('запросить список всех питомцев 5')
	    print('выход 0')
	    print()
	    print()
	    
def addPet(name,type,age,o):
	
	if len(pets)==0:
		last=0
	else:
		last= collections.deque(pets,maxlen=1)[0]
	Pet=dict(type=type,age=age,owner=o)
	obj={}
	obj[name]=Pet
	pets[last+1]=obj

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')	

	
def update():
	print('введите id')
	id=int(input())
	validatorId(id)
	p=''
	print('введите какой параметр необходимо обновит.')
	print('name,type,age,owner')
	k=input()
	key=''
	p=pets.get(id)
	for i in p.keys():
		key=i
	if k=='name':
		print('введите новое имя')
		n=input()
		
		obj={}
		petUpdate=p[key]
		obj[n]=petUpdate
		pets[id]=obj
		print(pets[id])
	elif k=='type':
		print('введите новый тип')
		t=input()
		pets[id][key]['type']=t
	elif k== 'age':
		a=int(input())
		pets[id][key]['age']=a
	elif k=='owner':
		print('введите нового влажельца')
		o=input()
		pets[id][key]['owner']=o
	else:
		exit

def creat():
	
    print('name pet')
    name=input()
    print('type')
    type=input()
    print('age')
    age=int(input())
    print('owner')
    owner=input()
    addPet(name,type,age,owner)	
    
def delete():
        print('введите id питомца подлежащего удалению')
        id=int(input())
        validatorId(id)
        pets.pop(id)
      
def validatorId(id):
    	if get_pet(id)== False:
    		print('не верный id')
    		exit()
        
def get_list():
	for i in pets.values():
		printPet(i)
	if len(pets)==0:
		print('база пуста')
		exit()
	
def get_pet(id):
    if id in pets.keys():
    	return pets[id]
    else:
    	return False
    	
def printPet(j):
	    key=''
	    for i in j.keys():
	    	key=i
	    print('Это {type} по кличке "{name}". Возраст питомца: {age} {f}. Имя владельца: {owner}'.format(type=j[key]['type'],name=key,age=j[key]['age'],f=get_suffix(j[key]['age']),owner=j[key]['owner']))
	
def read():
    print('введите id')
    id=int(input())
    validatorId(id)
    j = get_pet(id)

    printPet(j)

    
    
def menu():
    
    printMenu()
    c = int(input())

    while(c>0 and c <6):
    		if c==1:
    			clear()
    			creat()
    			printMenu()
    			
    		elif c==2:
    				clear()
    				read()
    				printMenu()
    		elif c==3:
    					clear()
    					update()
    					printMenu()
    		elif c==4:
    			clear()
    			delete()
    			printMenu()
    		elif c ==5:
    			clear()
    			print(get_list())
    			printMenu()
		
    		c= int(input())

    		if c ==0:
    			exit

def get_suffix(age):
	r=''
	
	if age>5 and age< 20:
		r='лет'
	elif age%10 ==1:
		r='год'
	elif age%10<5 and age%10!=0:
		r='года'
	else:
		r='лет'
	return r

menu()
