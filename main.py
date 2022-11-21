units = input("Imperial (imp) or Metric (met)? ")
mof = input("(M)ale or (F)emale? ")     #mof means Male Or Female
wt = input("Weight? ")
if units == "imp":
    print("Only use inches, not feet")
ht = input("Height? ")
waist = input("Waist? ")
neck = input("Neck? ")

if units == "imp":
    ht = float(ht) * 2.54
    waist = float(waist) * 2.54
    neck = float(neck) * 2.54

if mof.upper() == "M":
    bf = 10.1 - (0.239 * ht) + (0.8 * waist) - (0.5 * neck)
elif mof.upper() == "F":
    bf = 19.2 - (0.239 * ht) + (0.8 * waist) - (0.5 * neck)

fm = float(bf/100) * float(wt)
lm = float(wt) - float(fm)

print("Body Fat %:", round(bf))
print("Fat Mass:", round(fm, 1))
print("Lean Mass:", round(lm, 1))

