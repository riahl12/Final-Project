import heapq

class PatientInfo: #This class takes in attributes for the owner first and last name, pet name, species and priority(meaning what order will the vet see them in)
    def __init__(self, o_fname, o_lname, petname, species, priority):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-") #this is setting that only string characters can be entered to validate input
                                                                                        #for the schedule
        if not (name_characters.issuperset(o_fname) and name_characters.issuperset(o_lname) 
            and name_characters.issuperset(petname) and name_characters.issuperset(species)):
            raise ValueError("The inputs must be a letter.")
        else:
            self.o_fname = o_fname
            self.o_lname = o_lname
            self.petname = petname
            self.species = species
            self.priority = priority

class Schedule: #The class initializes an empty list to save the information gathered from the PetInfo class
    def __init__(self):
        self.pqueue = []

    def insert(self, node): #This function inserts the PetInfo into the empty list and will sort based on the priority
                            #it will put the appointments in order from first to last
        if(self.size() == 0):
            self.pqueue.append(node)
        else:
            for x in range(0, self.size()):
                if(node.priority >= self.pqueue[x].priority):
                    if(x == (self.size() - 1)):
                        self.pqueue.insert(x + 1, node)
                    else:
                        continue
                else:
                    self.pqueue.insert(x, node)


    def delete(self): #This function will take off the highest priority appointment first since the highest
                        #priority will always be at index 0
        return self.pqueue.pop(0)
    
    def size(self): #This function will return the length of the daily schedule, the vet can see how many appointments they have 
                    #in a given day
        return len(self.pqueue)
    
    def print(self):#This function will print out the information for the schedule along with the priority next to it
                    #so the vet can make sure they are seeing everyone in the correct order
        for x in self.pqueue:
            print("Owner name: {} {}, Pet Name: {}, Species: {} - {}".format(x.o_fname, x.o_lname, x.petname, x.species, x.priority))
    

if __name__ == "__main__":
    schedule1 = Schedule()
    pet1 = PatientInfo("John","Smith","Ginger","Cat","1")
    pet2 = PatientInfo("Jane", "Doe", "Sam", "Dog","2")
    pet5 = PatientInfo("bob","dylan","sparky","cat","5")
    pet3 = PatientInfo("Holly", "Johnson", "Kenny", "Other","3")
    pet4 = PatientInfo("Sam", "Jackson", "Percy", "Dog","4")
    pet6 = PatientInfo("Hailey","Jones","sally","Cat","6")
   

    schedule1.insert(pet3)
    schedule1.insert(pet1)
    schedule1.insert(pet2)
    schedule1.insert(pet5)
    schedule1.insert(pet4)
    schedule1.insert(pet6)
    schedule1.print()
    print("Today's schedule has:",schedule1.size()," patients.")

    
    print("\nSchedule after 2 patients have been seen:")
    schedule1.delete()
    schedule1.delete()
    schedule1.print()
