from datetime import datetime
import matplotlib.pyplot as plt


class Human:

    def __init__(self):
        self.temperature = []
        self.diastolic_pressure = []
        self.systolic_pressure = []
        self.respiration_rate = []
        self.oxygen_level = []
        self.pulse_rate = []
        self.date_time = []

    def temperature_input(self):
        temp = int(input('Enter the temperature value: '))
        self.temperature.append(temp)
        now = datetime.now()
        now = now.strftime('%H:%M:%S')
        self.date_time.append(now)

    def respiration_input(self):
        rr = int(input('Enter the respiration value: '))
        self.respiration_rate.append(rr)

    def oxygen_input(self):
        o_2 = int(input('Enter the peripheral capillary oxygen saturation value: '))
        self.oxygen_level.append(o_2)

    def pulse_input(self):
        hr = int(input('Enter the pulse value: '))
        self.pulse_rate.append(hr)

    def blood_pressure_input(self):
        bp = input('Enter the blood pressure value: ')
        bp_split = bp.index('/')
        bp_sys = bp[0:bp_split]
        self.systolic_pressure.append(int(bp_sys))
        bp_dias = bp[bp_split + 1:]
        self.diastolic_pressure.append(int(bp_dias))
        plt.xlabel("Date-time")
        plt.ylabel("Blood Pressure")
        plt.title('Graph of blood pressure against time')
        # plt.ylim(50, 150)
        plt.plot(self.date_time, self.systolic_pressure, 'o-b')
        plt.plot(self.date_time, self.diastolic_pressure, '*-r')
        plt.show()
        self.plot_graphs()

    def plot_a_graph(self, y_values, ti_tle, la_bel):
        plt.xlabel('Date-time')
        plt.ylabel(la_bel)
        plt.title(ti_tle)
        plt.grid()
        if la_bel == 'Temperature':
            plt.ylim(30, 50)
            plt.plot(self.date_time, y_values, 'o-g')
        elif la_bel == 'Respiration rate':
            plt.ylim(0, 60)
            plt.plot(self.date_time, y_values, 'o-g')
        elif la_bel == 'SPO2':
            # plt.ylim(0, 100)
            plt.plot(self.date_time, y_values, 'o-g')
        elif la_bel == 'Pulse rate':
            plt.plot(self.date_time, y_values, 'o-g')
            # plt.ylim(60, 180)
        plt.show()

    def plot_graphs(self):
        self.plot_a_graph(self.temperature, 'Graph of temperature against time', 'Temperature')
        self.plot_a_graph(self.respiration_rate, 'Graph of respiration rate against time', 'Respiration rate')
        self.plot_a_graph(self.oxygen_level, 'Graph of SPO2 against time', 'SPO2')
        self.plot_a_graph(self.pulse_rate, 'Graph of Pulse rate against time', 'Pulse rate')


patient = Human()
true = 1
while true:
    patient.temperature_input()
    patient.respiration_input()
    patient.oxygen_input()
    patient.pulse_input()
    patient.blood_pressure_input()
    print('')
    print('')

   
