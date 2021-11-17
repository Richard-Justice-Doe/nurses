import matplotlib.pyplot as plt
from datetime import datetime

class Hospitalization:
    Pulse = []
    Temperature = []
    Respiration = []
    Oxygen = []
    DateTime = []
    Diastolic_pressure = []
    Systolic_pressure = []

    def getTime(self):
        now = datetime.now()
        now = now.strftime('%H:%M:%S')
        self.DateTime.append(now)

    def pulse_function(self):
        pr = float(input("Please Enter the value for the Pulse: "))
        self.Pulse.append(pr)
        plt.subplot(1, 5, 1)
        plt.ylim(60, 180)
        plt.title("Pulse")
        plt.minorticks_on()
        plt.grid(b=true,which ='minor',color = 'green')
        
        plt.grid(b=true,color = 'white')
        plt.grid(True)
        plt.plot(self.DateTime, self.Pulse, marker="*")



    def temperature_function(self):
        temp = float(input("Please Enter the value for Temperature :"))
        self.Temperature.append(temp)
        plt.subplot(1, 5, 2)
        plt.ylim(35, 41)
        plt.title("Temperature")
        plt.minorticks_on()
        plt.grid(b=true,which ='minor',color = 'green')
        
        plt.grid(b=true,color = 'white')
        plt.grid(True)
        plt.plot(self.DateTime, self.Temperature, marker="*")


    def respiration_function(self):
        resp = float(input("Please Enter the value for Respiration :"))
        self.Respiration.append(resp)
        plt.ylim(0, 59)
        plt.subplot(1, 5, 3)
        plt.title("Respiration")
        plt.minorticks_on()
        plt.grid(b=true,which ='minor',color = 'green')
        
        plt.grid(b=true,color = 'white')
        plt.grid(True)
        plt.plot(self.DateTime, self.Respiration, marker="*")


    def oxygen_function(self):
        oxy = float(input("Please Enter the value for Oxygen: "))
        self.Oxygen.append(oxy)
        plt.subplot(1, 5, 4)
        plt.ylim(0, 100)
        plt.title("Oxygen")
        plt.minorticks_on()
        plt.grid(b=true,which ='minor',color = 'green')
        
        plt.grid(b=true,color = 'white')
        plt.grid(True)
        plt.plot(self.DateTime, self.Oxygen, marker="*")

    def blood_pressure_input(self):
        bp = input('Enter the blood pressure value: ')
        bp_split = bp.index('/')
        bp_sys = bp[0:bp_split]
        bp_sys = int(bp_sys)
        self.Systolic_pressure.append(bp_sys)
        bp_dias = bp[bp_split + 1:]
        bp_dias = int(bp_dias)
        self.Diastolic_pressure.append(bp_dias)
        plt.subplot(1, 5, 5)
        plt.ylim(60, 200)
        plt.title('Blood pressure')
        plt.plot(self.DateTime, self.Systolic_pressure,'o-b', label="Systolic Pressure")
        plt.plot(self.DateTime, self.Diastolic_pressure,'o-r',label="Diastolic Pressure")
        plt.legend()
        
        plt.minorticks_on()
        plt.grid(b=true,which ='minor',color = 'green')
        
        plt.grid(b=true,color = 'white')
        plt.grid(True)


g1 = Hospitalization()
true = 1
while true:
    g1.getTime()
    g1.pulse_function()
    g1.temperature_function()
    g1.respiration_function()
    g1.oxygen_function()
    g1.blood_pressure_input()
    plt.show()

