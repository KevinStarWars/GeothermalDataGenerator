import json_data_interaction as jdi
import geothermal
import data_operations as do
import numpy


def run():
    breakdown = numpy.random.choice([True, False])
    time_steps = 10000
    json_file = "calculation_data.json"
    data = jdi.get_data(json_file)
    geo = geothermal.Geothermal()
    geo.get_formulas(data)
    geo.generate_time_data(time_steps,
                           do.get_drilling_depth_from_data(data),
                           do.get_extraction_rate_from_data(data),
                           breakdown)
