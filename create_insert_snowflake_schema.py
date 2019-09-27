
#Drop statements
drop_temperature = "DROP TABLE IF EXISTS temperature;"
drop_location = "DROP TABLE IF EXISTS location;"
drop_time = "DROP TABLE IF EXISTS time;"
drop_us_demographics = "DROP TABLE IF EXISTS us_demographics;"

#Create statements
create_temperature = """CREATE TABLE IF NOT EXISTS temperature
(
date DATE NOT NULL,
location_id BIGINT NOT NULL,
average_temperature FLOAT,
average_temperature_uncertainty FLOAT
) ;
"""

create_location = """CREATE TABLE IF NOT EXISTS location
(
location_id BIGINT PRIMARY KEY NOT NULL,
country TEXT,
city TEXT,
longitude FLOAT,
latitude FLOAT
);
"""

create_time = """CREATE TABLE IF NOT EXISTS time
(
date DATE PRIMARY KEY NOT NULL,
year INT,
month INT,
day INT,
week INT
);
"""

create_us_demographics = """CREATE TABLE IF NOT EXISTS us_demographics
(
us_location_id BIGINT PRIMARY KEY NOT NULL,
location_id BIGINT,
city text,
state text,
median_age float,
male_population int,
female_population int,
total_population int,
number_of_veterans int,
foreign_born int,
average_household float,
state_code text
);
"""
# Parquet files locations
copy_locations = {
'temperature':'temperature.csv',
'location':'location.csv',
'time':'time.csv',
'us_demographics':'us_demographics.csv'
}

#Copy statements

copy_temperature = """
copy temperature (date, average_temperature, average_temperature_uncertainty, location_id)
FROM '/home/workspace/{}/{}' csv header;
"""

copy_location = """
copy location (location_id, country, city, longitude, latitude)
FROM '/home/workspace/{}/{}' csv header;
"""

copy_time = """
copy time (date, year, month, day, week)
FROM '/home/workspace/{}/{}' csv header;
"""

copy_us_demographics = """
copy us_demographics (city, state, median_age, male_population,
female_population, total_population, number_of_veterans,
foreign_born, average_household, state_code, location_id, us_location_id)
FROM '/home/workspace/{}/{}' csv header;
"""


#Queries lists
drop_snowflake_schema = [drop_temperature, drop_location, drop_time, drop_us_demographics]
create_snowflake_schema = [create_temperature, create_location, create_time, create_us_demographics]
copy_snowflake_schema = {'temperature':copy_temperature, 'location':copy_location, 'time':copy_time, 'us_demographics':copy_us_demographics}
data_quality_snowflake_schema = {'temperature':8190455, 'location':3490, 'time':3167, 'us_demographics':596}



