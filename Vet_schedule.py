class PatientInfo:
    def __init__(self, o_fname, o_lname, petname, species, priority):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(o_fname) and name_characters.issuperset(o_lname) 
            and name_characters.issuperset(petname) and name_characters.issuperset(species)):
            raise ValueError
        self.o_fname = o_fname
        self.o_lname = o_lname
        self.petname = petname
        self.species = species
        self.priority = priority

class Schedule:
    def __init__(self):
        self.queue = []

    def insert(self, node): 
        if(self.size() == 0):
            self.queue.append(node)
        else:
            for x in range(0, self.size()):
                if(node.priority >= self.queue[x].priority):
                    if(x == (self.size() - 1)):
                        self.queue.insert(x + 1, node)
                    else:
                        continue
                else:
                    self.queue.insert(x, node)

    def delete(self): #have it so that it takes off the beginning node first meaning it is taking off the highest priority first
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def print(self):
        for x in self.queue:
            print("Owner name: {} {}, Pet Name: {}, Species: {} - {}".format(x.o_fname, x.o_lname, x.petname, x.species, x.priority))
    

if __name__ == "__main__":
    schedule1 = Schedule()
    pet1 = PatientInfo("John","Smith","Ginger","Cat","1")
    pet2 = PatientInfo("Jane", "Doe", "Sam", "Dog","2")
    pet5 = PatientInfo("bob","dylan","sparky","cat","5")
    pet3 = PatientInfo("Holly", "Johnson", "Kenny", "Other","3")
    pet4 = PatientInfo("Sam", "Jackson", "Percy", "Dog","4")
   

    schedule1.insert(pet3)
    schedule1.insert(pet1)
    schedule1.insert(pet2)
    schedule1.insert(pet5)
    schedule1.insert(pet4)
    schedule1.print()

    schedule1.delete()
    schedule1.print()
