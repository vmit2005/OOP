from re import findall


s="12.12.2022"
print(findall(r'\d{2}.\d{2}.\d{4}', s))