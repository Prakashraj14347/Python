from collections import OrderedDict

schools={}
schools["S1"]='Loyola'
schools["S3"]='velammal'
schools["S2"]='DAV'
schools["S4"]='JRM'
schools["S5"]='Fathima'
print("\nRegular Dictionary")
print("\nBefore changing ")
print(schools)

schools.pop("S4")
print("\nAfter changing ")
print(schools)


od = OrderedDict()
od["S1"]='Loyola'
od["S5"]='velammal'
od["S3"]='DAV'
od["S4"]='JRM'
od["S2"]='Fathima'
print("\nOrdered Dictionary")
print("\nBefore changing ")
print(od)

od.pop("S4")
print("\nAfter changing ")
print(od)

