talents = input("Enter number of talents: ")
pounds = input("Enter number of pounds: ")
lots = input("Enter number of lots: ")
weight_total = float(talents) * 20 * 32 * 13.3 + float(pounds) * 32 * 13.3 + float(lots) * 13.3
weight_kilo = weight_total / 1000
weight_gram = float(weight_total) - int(weight_kilo) * 1000
print('The weight in modern units: %d kilograms and %.2f grams' %(weight_kilo, weight_gram))