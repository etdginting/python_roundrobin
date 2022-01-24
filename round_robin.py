

# NOTE 
# input total resource INT 
# ex: 10
# input with , to team leader resource 
# ex: 3,4,5,6,7



class RoundRobin:
    def __init__(self):
        self.listN=[]
        self.output1=[]
        self.output2=[]
        self.rinput1=[]
        self.rinput2=[]

    def inputTotalResource(self):
        checkingResource=False
        while not checkingResource:
            n=int(input('Please input your total resource: '))
            self.listN=[i for i in range(1,n+1)]
            if len(self.listN) % 2 == 0:
                print(f'Please choose your resource {self.listN}')
                checkingResource = True
            else:
                print('Total Resources can not odd..!!')
    def inputTeamLeader1(self):
        limitResource1=False
        while not limitResource1:
            input1=input("Team leader 1 resources :")
            self.rinput1 = list(map(int,input1.strip().split(',')))
            if (len( self.rinput1) <= int(len(self.listN)/2)):
                limitResource1= True
            else:
                print(f'You only can choose {int(len(self.listN)/2)} resources')
    def inputTeamLeader2(self):
        limitResource2=False
        while not limitResource2:
            input2=input("Team leader 2 resources :")
            self.rinput2 = list(map(int,input2.strip().split(',')))
            if len(self.rinput2) <= int(len(self.listN)/2):
                limitResource2= True
            else:
                print(f'You only can choose {int(len(self.listN)/2)} resources')
    def getAvailableResource(self,arr):
        # get available resource
        for _,v in enumerate(self.listN):
            if v not in self.output1 and v not in self.output2:
                arr.append(v)
                break
    def roundRobinLogic(self):
        index = 0
        limitN = False
        while not limitN: 
            r1 = self.rinput1[index]
            r2 = self.rinput2[index]
            # check Team leader 1 resources
            if r1 not in self.output2 and r1 not in self.output1:
                self.output1.append(r1)
            else:   
                # get available resource
                self.getAvailableResource(self.output1)
            
            # check Team leader 2 resources
            if r2 not in self.output1 and r2 not in self.output2:
                self.output2.append(r2)
            else:
                # get available resource
                self.getAvailableResource(self.output2)
            
            if index == int(len(self.listN)/2)-1:
                limitN=True
            else:
                index+=1

    def execute(self):
        self.inputTotalResource()
        self.inputTeamLeader1()
        self.inputTeamLeader2()
        self.roundRobinLogic()
                

if __name__:
    roundRobin = RoundRobin()
    roundRobin.execute()
    print(f'Output 1 : {roundRobin.output1}')
    print(f'Output 2 : {roundRobin.output2}')
