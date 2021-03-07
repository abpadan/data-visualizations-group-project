import urllib2

def validate_clean(perp_age_group):
    if perp_age_group != "1020" and perp_age_group != "224" and perp_age_group != "940":
      return True
    else:
      return False

def validate_not_empty(perp_age_group, perp_sex, perp_race):
    if perp_age_group and perp_sex and perp_race and validate_clean(perp_age_group):
        return True
    else:
      return False

def get_year(occur_date):
  return "," + occur_date[-4:]

def line_to_append(line, occur_date): 
  line = line.rstrip()
  line = line + get_year(occur_date)
  line = line + '\n'
  return line

data = urllib2.urlopen('https://data.cityofnewyork.us/api/views/833y-fsy8/rows.csv?accessType=DOWNLOAD')
cleaned_file = open("NYPD_Shooting_Incident_Data__Historic_Cleaned.csv", "w")
count = 0
cleaned_file.write("INCIDENT_KEY,OCCUR_DATE,OCCUR_TIME,BORO,PRECINCT,JURISDICTION_CODE,LOCATION_DESC,STATISTICAL_MURDER_FLAG,PERP_AGE_GROUP,PERP_SEX,PERP_RACE,VIC_AGE_GROUP,VIC_SEX,VIC_RACE,X_COORD_CD,Y_COORD_CD,Latitude,Longitude,Lon_Lat,OCCUR_YEAR\n")
for line in data:
  if count > 0:
    split = line.split(",")
    occur_date = split[1]
    perp_age_group = split[8]
    perp_sex = split[9]
    perp_race = split[10]
    validate_flg = validate_not_empty(perp_age_group, perp_sex, perp_race)

    if validate_not_empty(perp_age_group, perp_sex, perp_race):
      cleaned_file.write(line_to_append(line, occur_date))
  count += 1
cleaned_file.close()