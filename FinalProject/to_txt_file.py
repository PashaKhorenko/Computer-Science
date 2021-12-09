from numpy import *
from FinalProject.convert_efficiency_to_json import dict_of_data_for_plot
import codecs

output_str = ""
for enterprise in dict_of_data_for_plot.items():
    output_str = output_str + "\n" + str(enterprise)

with codecs.open('txt_efficiency_of_enterprise.txt', 'w', 'utf-8') as file:
    file.write(output_str)
