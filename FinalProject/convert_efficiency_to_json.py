from FinalProject import data
import json
import codecs

dict_of_data_for_plot = {}

for efficiency in data.sorted_enterprise_efficiency_list:

    try:
        dict_of_data_for_plot[efficiency.name]
    except:
        dict_of_data_for_plot[efficiency.name] = {}

    for attr, value in vars(efficiency).items():
        if attr != 'name':
            try:
                dict_of_data_for_plot[efficiency.name][attr].append(value)
            except:
                dict_of_data_for_plot[efficiency.name][attr] = [value]

# json_data = json.dumps(dict_of_data_for_plot, ensure_ascii=False).encode('utf8')
with codecs.open('efficiency.json', 'w', 'utf-8') as json_file:
    json.dump(dict_of_data_for_plot, json_file, ensure_ascii=False)
