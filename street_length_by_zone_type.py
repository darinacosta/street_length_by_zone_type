
#Set your target dataset here:
target_dataset = "fq_street_sanitation_v1"

def build_street_array(zone_type):
  street_array = []
  for row in arcpy.SearchCursor(target_dataset):
    #Set your target attributes here
    if row.ST_NAME not in street_array and row.FLUSHSWEEP != "<Null>" and row.ZoneType == zone_type:
      street_array.append(row.ST_NAME)
  street_array.sort()
  return street_array

def calculate_street_length(name, zone_type):
  total = 0
  for row in arcpy.SearchCursor(target_dataset):
    if row.ZoneType == zone_type and row.ST_NAME == name:
      total = total + row.CURB_MILES  
  if total == 0:
    print "Your total is 0."
  else:
    print name + ": " + str(total)

def print_street_lengths(zone_type):
  print "-------BEGIN ZONE TYPE: " + zone_type + "-----------"
  street_array = build_street_array(zone_type)
  for street in street_array:
    calculate_street_length(street, zone_type)
  print "-------END ZONE TYPE: " + zone_type + "-----------"

