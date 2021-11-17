from matplotlib import pyplot as plt
from datetime import datetime

class Hospitalization:
    DateTime = []
    Temperature = []
    PulseRate = []
    Respiration = []
    BloodPressure =[]
    
    def graph_time(self):
        now = datetime.now()
        now = now.strftime("%H:%M:%S")
        self.DateTime.append(now)

    # TemperatureGraph_Sample
    def temperature_function(self):
        temp = input('Input temp value')
        self.Temperature.append(temp)
        plt.subplot(1, 4, 2)
        plt.ylabel("Temperature °C")
        plt.xlabel("Day(s)")
        plt.title("Temperature Graph")
        plt.plot(self.DateTime, self.Temperature, marker='*')

    #BloodPressureGraph_Sample
    def BloodPressure_function(self):
        bp = input('input bp values') 
        self.BloodPressure.append(bp)
        plt.subplot(1, 4, 1)
        
        
    # PulseRateGraph_Sample
    def pulserate_function(self):
        pulse = input('input pulse value')
        self.PulseRate.append(pulse)
        plt.subplot(1, 4, 1)
        plt.ylabel("Pulse Rate")
        plt.xlabel("Time")
        plt.title("Pule Rate Graph")
        plt.plot(self.DateTime, self.PulseRate, marker='*')


    # RespirationGraph_Sample
    def respiration_function(self):
        resp = input('input Respiration value')
        self.Respiration.append(resp)
        plt.subplot(1, 4, 3)
        plt.xlabel("Respiration Rate")
        plt.ylabel("Time (mins)")
        plt.title("Respiration Rate Graph")
        plt.plot(self.DateTime, self.Respiration, marker='*')


a = Hospitalization()

true = 1
while true:
    a.graph_time()
    a.pulserate_function() 
    a.temperature_function()
    a.respiration_function()
    plt.show()

