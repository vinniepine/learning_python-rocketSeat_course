name = "Vinnie"
surname = "Pine" 
full_name = "Vinnie Pine"

full_name_quotes = """Vinnie
Pine"""
full_name_break = "Vinnie \
Pine"

# Formatação
print("Nome completo (1a forma):", full_name)
print("Nome completo (2a forma): " + full_name)
print("Nome completo (3a forma): " + "Vinnie" + " " + "Pine")
print("Nome completo (4a forma): " +  "Vinnie", "Pine")
print("Nome completo (5a forma):", full_name_quotes)
print("Nome completo (6a forma):", full_name_break)
print("Nome completo (7a forma): %s" % full_name)
print("Nome completo (8a forma): %s %s" % (name, surname))
print(f"Nome completo (9a forma): {full_name}")
print(f"Nome completo (10a forma): {name} {surname}")
print("Nome completo (11a forma): {} {}".format(name, surname))








