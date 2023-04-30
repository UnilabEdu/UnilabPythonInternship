def create_dict(keys, values):
    data_dict = {}
    for i in range(len(keys)):
        data_dict[keys[i]] = values[i]
    return data_dict


def create_dicts(keys, value_tuples):
    dicts = []
    for values_tuple in value_tuples:
        dicts.append(create_dict(keys, values_tuple))
    return dicts
