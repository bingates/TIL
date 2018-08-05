from function import *

raw_data = get_data_from_excel('class_1.xlsx')
scores=list(raw_data.values())

avrg=get_average(scores)
variance=get_variance(scores,avrg)
std_dev=get_std_dev(variance)

evaluate_class(avrg, std_dev)