import random

class AnimalTypes:
    def __init__(self, name, population, hygiene, hunger, health,location):
        self.name = name        
        self.population = population
        self.hygiene = hygiene
        self.hunger = hunger
        self.health = health  
        self.location= location

    def daypass(self):
        self.hunger+=30
        self.hygiene-=35
        if  self.hygiene!=0 and self.hunger!=0:
            self.health-= self.population*self.hunger/2000*self.hygiene 
        elif  self.hygiene==0 and self.hunger!=0:
            self.health-=self.population*self.hunger/10000 +20
        elif  self.hygiene !=0 and self.hunger ==0 :
            self.health -= self.population/50*self.hygiene +20
        else: 
            self.health-=self.population/10+10

        return self.hunger, self.hygiene, self.health

    def daycheck(self):
        if self.hygiene > 100:
            self.hygiene=100
        elif self.hygiene < 0:
            self.hygiene=0
        
        if self.hunger < 0:
            self.hunger = 0
        elif self.hunger > 100:
            self.hunger = 100

        if  self.health > 100:
            self.health=100
        elif self.health < 0 :
            self.health=0

        if self.hunger==100 or self.health==0 or self.hygiene==0:
            self.population=self.population-random.randint(5,15)


        return self.population, self.hunger, self.hygiene, self.health
        

    def animalinfo(self):
        print(f'\n{self.name}: Population: {self.population}, Hunger: {self.hunger}, Hygiene: {self.hygiene}, Health: {self.health}. Region: {self.location}.')

class Region: 
    def  __init__(self,color,capacity):
        self.color=color
        self.capacity = capacity

class  ZooKeeper:
    def __init__(self, speciality,skill):
        self.specialty = speciality
        self.skill = skill

    def dailywork(self,j:AnimalTypes,special):
        if special=="Feeder":
            j.hunger-= self.skill*0.75+2
            return j.hunger
            
        elif special=="Cleaner":
            j.hygiene+= self.skill*0.75+3
            return j.hygiene
            
        elif special == "Vet":
            j.health+= self.skill*5+3
            return  j.health 
        
    def alert(self,j:AnimalTypes,special):
        if special=="Feeder":
            j.hunger= j.hunger - (self.skill*0.5+2)
            return j.hunger
            
        elif special=="Cleaner":
            j.hygiene =j.hygiene+ (self.skill*0.5+3)
            return j.hygiene
            
        elif special == "Vet":
            j.health =j.health+ (self.skill*0.75+2)
            return  j.health            
            
class Zoo: 
    def  __init__(self, animals:list[AnimalTypes], areas:list[Region] , zookeepers : list [ZooKeeper]):
        self.animals = animals
        self.areas = areas
        self.zookeepers= zookeepers
    def sort_animals(self):
        self.animals.sort(key=lambda x: x.population)
        return  self.animals
    def sort_areas(self):
        self.areas.sort(key=lambda x: x.capacity)
        return   self.areas
    def mapping(self):
        sortedanimals=self.sort_animals()
        sortedareas=self.sort_areas()
        for i,j in zip(sortedanimals,sortedareas):
            if i.population <= j.capacity:   
                i.location=j.color
            else:
                i.location= None
                sortedanimals.remove(i)

        print('\nThe Zoo mapping is:')
        for i in self.animals:
            if i.location==None:
                print(f'{i.name} have  no home yet.')
            else:
                print(f'{i.name} are in the {i.location} area')
        
    def assign(self):
        spec=['Feeder','Cleaner','Vet','Breeder']  
        random.shuffle(spec)
        for i in self.zookeepers:
            c=self.zookeepers.index(i)
            if  c in range(4):
                i.specialty=spec[c]
                i.skill=random.randint(1,5)
            else:
                i.specialty=random.choice(spec)
                i.skill= random.randint(1,5)
        return i.specialty, i.skill  
    
    def daypass(self): #n is the number of days
        
        for i in self. animals:

            i.daypass()
            for j in self.zookeepers:
                for k in ['Feeder','Cleaner','Vet','Breeder']:
                    j.dailywork(i,k)

            if i.hunger>80:
                 j.alert(i,'Feeder')

            if i.health<20:
                j.alert(i, 'Vet')

            if i.hygiene<20:
                j.alert(i,'Cleaner')

            if i.health==100 and i.hunger==0 and i.hygiene==100:
                if j.specialty== 'Breeder':
                    i.population+=2*j.skill

            i.daycheck()
            
            if i.population <=0:
                print(f'There are no more {i.name} left.\n')
                self.animals.remove(i)

        for i in self.animals:
            i.animalinfo()
        return self.animals
    
    def n_daypass(self,n): #n is the number of days
        if n==1:
            print('\n 1 day has passed...\n')
            self.daypass()

        else: 
            print(f'\n {n} days have passed...\n')
            for i in range(n):
                print (f'\n Day {i+1}:\n')
                self.daypass()
        
    def zooinfo(self):
        print(f'The zoo has the following animals:')
        for i in self.animals: 
            print(f'{i.name}, Population: {i.population}')
        print(f'\nIt is devided in the following areas:')
        for j in self.areas:
            print (f'{j.color}, Capacity: {j.capacity}')
        print (f'\nAnd it employes {len(self.zookeepers)} zookepers of different specialties and skill. More specifically:')
        for i in  self.zookeepers:
            print(f'{i.specialty}, Skill: {i.skill}')

    def firstdayinfo(self):

        print(f'\nOn the Zoo\'s 1st day there are:')
        for i in self.animals:
            i.daycheck()
            i.animalinfo()
        return self.animals


def regiongen(n): #n=number of regions
    regions=[]
    colors= ['Red','Green', 'Blue', 'Yellow', 'Purple', 'White', 'Black', 'Gray', 'Orange', 'Brown','Pink','Cyan']
    random.shuffle(colors)
    for i in range (n):
        r=Region(colors[i],random.randint(50,200))
        regions.append(r)
    return regions

def animalgen(m): # m= number of animals to generate
    types= ['Bears','Giraffes','Pandas','Hippos','Lions','Flamingos','Rhinos','Camels','Zebras','Capybaras','Donkeys','Koalas','Parrots','Tiger','Unicorn','Peacocks','Snails']
    random.shuffle(types)
    animals=[]
    for i in range(m):
        a=AnimalTypes(types[i], random.randint(20,100),random.randint(30,100),random.randint(30,100),random.randint(30,100),None)
        animals.append(a)
    return animals

def keepergen(n): #minimum 4=#specialties
    keepers = []
    for i in range(n):
        keepers.append(ZooKeeper(None,None))
    return keepers


CapyZoo=Zoo(animalgen(6),regiongen(7),keepergen(10))
CapyZoo.assign()
CapyZoo.zooinfo()
CapyZoo.mapping()
CapyZoo.firstdayinfo()
CapyZoo.n_daypass(3)
