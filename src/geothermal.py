import numpy
import generate_formulas as gf
import data_operations as do
import json
import uuid
import random


class Geothermal:

    def __init__(self):
        self.time_step = 0
        self.id = str(uuid.uuid4())
        self.depth = 0
        self.temperature = 0
        self.extraction_rate = 0
        self.geothermal_power = 0
        self.electrical_power = 0
        self.efficiency = 0
        self.efficiency_median = 0
        self.efficiency_std_dev = 0
        self.polynomial_temperature_extraction_geothermal = None
        self.temperature_depth_gradient = 0
        self.temperature_depth_y_axis = 0

    def get_formulas(self, data_set):
        self.efficiency_median, self.efficiency_std_dev = gf.calculate_turbine_efficiency(do.get_normalized_geothermal_power_from_data(data_set),
                                                                                          do.get_normalized_electrical_power_from_data(data_set))
        self.polynomial_temperature_extraction_geothermal = gf.temperature_geothermal_power_extraction_rate(do.get_temperature_list_from_data(data_set),
                                                                                                            do.get_normalized_extraction_rate_from_data(data_set),
                                                                                                            do.get_normalized_geothermal_power_from_data(data_set))
        self.temperature_depth_gradient, self.temperature_depth_y_axis = gf.temperature_drilling_depth(do.get_temperature_list_from_data(data_set),
                                                                                                       do.get_drilling_depth_from_data(data_set))

    def generate_random_geothermal(self, depth_list, extraction_list):
        self.generate_random_depth(do.get_min_depth(depth_list), do.get_max_depth(depth_list))
        self.calculate_temperature()
        self.generate_random_extraction(do.get_min_normalized_extraction(extraction_list),
                                        do.get_max_normalized_extraction(extraction_list))
        self.calculate_geothermal_power()
        self.generate_random_efficiency()
        self.calculate_electrical_power()

    def generate_random_depth(self, minimum, maximum):
        self.depth = numpy.random.uniform(minimum, maximum)

    def calculate_temperature(self):
        self.temperature = self.depth * self.temperature_depth_gradient + self.temperature_depth_y_axis

    def generate_random_extraction(self, minimum, maximum):
        self.extraction_rate = numpy.random.uniform(minimum, maximum)

    def calculate_geothermal_power(self):
        self.geothermal_power = self.polynomial_temperature_extraction_geothermal(self.temperature*self.extraction_rate)

    def generate_random_efficiency(self):
        min_efficiency = self.efficiency_median - self.efficiency_std_dev
        max_efficiency = self.efficiency_median + self.efficiency_std_dev
        self.efficiency = numpy.random.uniform(min_efficiency, max_efficiency)

    def calculate_electrical_power(self):
        self.electrical_power = self.geothermal_power * self.efficiency

    def to_string(self):
        return 'self.depth - {0}\n' \
               'self.temperature - {1}\n' \
               'self.extraction_rate - {2}\n' \
               'self.geothermal_power - {3}\n' \
               'self.electrical_power - {4}\n' \
               'self.efficiency - {5}\n' \
               'self.id - {6}'.format(self.depth, self.temperature, self.extraction_rate,
                                      self.geothermal_power, self.electrical_power, self.efficiency, self.id)

    def to_dictionary(self):
        data = {'depth': self.depth,
                'temperature': self.temperature,
                'extraction_rate': self.extraction_rate,
                'geothermal_power': self.geothermal_power,
                'electrical_power': self.electrical_power,
                'efficiency': self.efficiency,
                'id': self.id,
                'time_step': self.time_step}
        return data

    def to_file(self):
        filename = 'generated_data/' + self.id + '.json'
        with open(filename, 'a') as outfile:
            json.dump(self.to_dictionary(), outfile, indent=4, sort_keys=True)

    def generate_time_data(self, steps, depth_list, extraction_list, breakdown):
        if breakdown:
            breakdown_timestep = self.get_breakdown_time(steps)
            efficiency_or_extraction = random.choice([True, False])
        else:
            breakdown_timestep = steps + 1
            efficiency_or_extraction = True
        time_list = []
        self.generate_random_geothermal(depth_list, extraction_list)
        for step in range(0, steps):
            if step == breakdown_timestep:
                if efficiency_or_extraction:
                    print('efficiency breakdown')
                    self.efficiency_breakdown()
                else:
                    print('extraction breakdown')
                    self.extraction_breakdown()
            else:
                self.change_extraction()
                self.change_efficiency()
            self.calculate_geothermal_power()
            self.calculate_electrical_power()
            time_list.append(self.to_dictionary())
        self.list_to_file(time_list)

    def change_efficiency(self):
        self.efficiency += numpy.random.uniform(-0.00001, 0.00001)

    def change_extraction(self):
        self.extraction_rate += numpy.random.uniform(-5, 5)

    def list_to_file(self, list):
        filename = 'generated_data/' + self.id + '.json'
        with open(filename, 'a') as outfile:
            json.dump(list, outfile, indent=4, sort_keys=True)

    def efficiency_breakdown(self):
        self.efficiency = self.efficiency * 0.5

    def extraction_breakdown(self):
        self.extraction_rate = self.extraction_rate * 0.5

    def get_breakdown_time(self, steps):
        return random.randint(1, steps)