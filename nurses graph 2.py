import matplotlib.pyplot as plt
from datetime import datetime

class Hospitalization:
    Pulse = []
    Temperature = []
    Respiration = []
    Oxygen = []
    Diastolic_pressure = []
    Systolic_pressure = []
    DateTime = []

    def getTime(self):
        now = datetime.now()
        now = now.strftime('%H:%M:%S')
        self.DateTime.append(now)

    def pulse_function(self):
        pr = float(input("Please Enter the value for the Pulse: "))
        self.Pulse.append(pr)
        plt.title("Pulse")
        plt.ylim(60, 180)
        plt.plot(self.DateTime, self.Pulse, marker="*")
        plt.grid()
        plt.show()

    def temperature_function(self):
        temp = float(input("Please Enter the value for Temperature"))
        self.Temperature.append(temp)
        plt.title("Temperature")
        plt.ylim(35, 41)
        plt.plot(self.DateTime, self.Temperature, marker="*")
        plt.grid()
        plt.show()

    def respiration_function(self):
        resp = float(input("Please Enter the value for Respiration"))
        self.Respiration.append(resp)
        plt.title("Respiration")
        plt.ylim(0, 59)
        plt.plot(self.DateTime, self.Respiration, marker="*")
        plt.grid()
        plt.show()

    def oxygen_function(self):
        oxy = float(input("Please Enter the value for Oxygen"))
        self.Oxygen.append(oxy)
        plt.title("Oxygen")
        plt.ylim(0, 100)
        plt.plot(self.DateTime, self.Oxygen, marker="*")
        plt.grid()
        plt.show()

    def blood_pressure_input(self):
        bp = input('Enter the blood pressure value: ')
        bp_split = bp.index('/')
        bp_sys = bp[0:bp_split]
        bp_sys = int(bp_sys)
        self.Systolic_pressure.append(bp_sys)
        bp_dias = bp[bp_split + 1:]
        bp_dias = int(bp_dias)
        self.Diastolic_pressure.append(bp_dias)
        plt.ylabel("Blood Pressure")
        plt.ylim(60, 200)
        plt.title('Graph of blood pressure against time')
        plt.plot(self.DateTime, self.Systolic_pressure,'o-b', label="Systolic Pressure")
        plt.plot(self.DateTime, self.Diastolic_pressure,'o-r',label="Diastolic Pressure")
        plt.legend()
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


