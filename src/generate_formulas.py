from sklearn.linear_model import LinearRegression
import numpy
import statistics
import data_operations as do


# used in order to find a linear relationship which describes the relationship between temperature and drilling depth
def temperature_drilling_depth(temperatures, drilling_depth):
    linear_regression = LinearRegression()
    temperature_array = numpy.array(temperatures)
    temperature_array = do.list_to_list_of_lists(temperature_array)
    depth_array = numpy.array(drilling_depth)
    depth_array = do.list_to_list_of_lists(depth_array)
    linear_regression.fit(depth_array, temperature_array)
    return linear_regression.coef_[0][0], linear_regression.intercept_[0]


# used in order to find a polynom which describes the relationship between temperatures, extraction_rates and
# geothermal_power
def temperature_geothermal_power_extraction_rate(temperatures, extraction_rates, geothermal_power):
    extraction_temperature = []
    # calculating a coefficient
    for i in range(0, len(temperatures)):
        extraction_temperature.append(temperatures[i]*extraction_rates[i])
    numpy_extraction_temperature = numpy.array(extraction_temperature)
    numpy_geothermal_power = numpy.array(geothermal_power)
    polynomial = numpy.polyfit(numpy_geothermal_power, numpy_extraction_temperature, 5)
    tester = numpy.poly1d(polynomial)
    return tester


# returns median and std dev of effciencies
def calculate_turbine_efficiency(geothermal_power, electrical_power):
    efficiency = []
    for i in range(0, len(geothermal_power)):
        efficiency.append(electrical_power[i]/geothermal_power[i])
    return statistics.stdev(efficiency), statistics.median(efficiency)
