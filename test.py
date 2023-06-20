import re

data = "Изготовитель системы производства     hjj"
os_prod_list = []
os_prod_reg = re.compile (r"Изготовитель системы:\s*\S*")
os_prod_list.append(os_prod_reg.findall(data))
print(os_prod_list)