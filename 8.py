import re
text = "RazDvaTriChetireAndDotaFu"
print(re.findall('[A-Z][^A-Z]*', text))