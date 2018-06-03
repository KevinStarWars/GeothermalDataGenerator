def get_temperature_list_from_data(data_set):
    temperature_list = []
    for data in data_set:
        temperature_list.append(float(data['Temperatur in C']))
    return temperature_list


def get_drilling_depth_from_data(data_set):
    depth_list = []
    for data in data_set:
        depth_list.append(float(data['Bohrtiefe in m']))
    return depth_list


def get_geothermal_power_from_data(data_set):
    return_list = []
    for data in data_set:
        return_list.append(float(data['Geoth. Leistung in MW']))
    return return_list


def get_electrical_power_from_data(data_set):
    return_list = []
    for data in data_set:
        return_list.append(float(data['Elektr. Leistung in MW']))
    return return_list


def get_normalized_electrical_power_from_data(data_set):
    return_list = get_electrical_power_from_data(data_set)
    return normalize_electrical_power(return_list)


def get_normalized_geothermal_power_from_data(data_set):
    return_list = get_geothermal_power_from_data(data_set)
    return normalize_geothermal_power(return_list)


def get_extraction_rate_from_data(data_set):
    return_list = []
    for data in data_set:
        return_list.append(float(data['Foerderrate in m3/h']))
    return return_list


def get_normalized_extraction_rate_from_data(data_set):
    return_list = get_extraction_rate_from_data(data_set)
    return normalize_extraction_rate(return_list)


def list_to_list_of_lists(liste):
    return_list = []
    for element in liste:
        return_list.append([element])
    return return_list


def normalize_geothermal_power(geothermal_power):
    return_list = []
    for value in geothermal_power:
        return_list.append(value*1000000)
    return return_list


def normalize_extraction_rate(extraction_rate):
    return_list = []
    for value in extraction_rate:
        return_list.append(value*360)
    return return_list


def normalize_electrical_power(electrical_power):
    return_list = []
    for value in electrical_power:
        return_list.append(value*1000000)
    return return_list


def get_max_depth(depth_list):
    return max(depth_list)


def get_min_depth(depth_list):
    return min(depth_list)


def get_max_normalized_extraction(extraction_list):
    extraction = []
    for value in extraction_list:
        extraction.append(value*360)
    return max(extraction)


def get_min_normalized_extraction(extraction_list):
    extraction = []
    for value in extraction_list:
        extraction.append(value*360)
    return min(extraction)