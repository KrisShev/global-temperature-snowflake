#Drop statements
drop_table_city = "DROP TABLE IF EXISTS yearly_average_temperature_city;"
drop_table_country = "DROP TABLE IF EXISTS  yearly_average_temperature_country;"
drop_table_monthly = "DROP TABLE IF EXISTS  monthly_average_temperature_year;"
drop_table_population = "DROP TABLE IF EXISTS yearly_average_temperature_us_population;"

#Create statements
create_table_city = """CREATE TABLE IF NOT EXISTS yearly_average_temperature_city
(
year int NOT NULL,
city text NOT NULL,
country text,
yearly_average float
);
"""

create_table_country = """CREATE TABLE IF NOT EXISTS yearly_average_temperature_country 
(
year int NOT NULL,
country text NOT NULL,
yearly_average float
);
"""

create_table_monthly = """CREATE TABLE IF NOT EXISTS monthly_average_temperature_year
(
year int NOT NULL,
month int NOT NULL,
monthly_average float
);
"""

create_table_population = """CREATE TABLE IF NOT EXISTS yearly_average_temperature_us_population
(
year int NOT NULL,
city text NOT NULL,
state text,
total_population int,
female_population int,
male_population int,
yearly_average float
);
"""

#Insert statements
insert_table_city = """
INSERT INTO yearly_average_temperature_city (year, city, country, yearly_average)
SELECT b.year, c.city, c.country, avg(a.average_temperature) as yearly_average
FROM temperature a
JOIN time b on a.date=b.date
JOIN location c on a.location_id=c.location_id
GROUP BY b.year, c.city, c.country
ORDER BY yearly_average DESC
;
"""

insert_table_country = """
INSERT INTO yearly_average_temperature_country (year, country, yearly_average)
SELECT b.year, c.country, avg(a.average_temperature) as yearly_average 
FROM temperature a
JOIN time b on a.date=b.date
JOIN location c on a.location_id=c.location_id
GROUP BY b.year, c.country
ORDER BY yearly_average DESC
"""

insert_table_monthly = """
INSERT INTO monthly_average_temperature_year (year, month, monthly_average)
SELECT b.year, b.month, avg(a.average_temperature) as monthly_average
FROM temperature a
JOIN time b on a.date=b.date
GROUP BY b.year, b.month
ORDER BY monthly_average DESC
"""

insert_table_population = """
INSERT INTO yearly_average_temperature_us_population (year, city, state, total_population, female_population, male_population, yearly_average)
SELECT b.year, c.city, c.state, c.total_population,
c.female_population, c.male_population, avg(a.average_temperature) as yearly_average
FROM temperature a
JOIN time b on a.date=b.date
JOIN us_demographics c on a.location_id=c.location_id
GROUP BY b.year, c.city, c.state, c.total_population,
c.female_population, c.male_population
ORDER BY yearly_average DESC
"""

#Lists
drop_analytics_tables = [drop_table_city, drop_table_country, drop_table_monthly, drop_table_population]
create_analytics_tables = [create_table_city, create_table_country, create_table_monthly, create_table_population]
insert_analytics_tables = [insert_table_city, insert_table_country, insert_table_monthly, insert_table_population]
analytics_tables = ['yearly_average_temperature_city', 'yearly_average_temperature_country', 'monthly_average_temperature_year', 'yearly_average_temperature_us_population']