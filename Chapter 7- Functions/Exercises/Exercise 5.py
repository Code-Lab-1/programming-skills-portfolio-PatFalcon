def city_description(city, country='Philippines'):
  city=(f"\n {city.title()} is in {country.title()}")
  print(city)

city_description("Makati")
city_description("Reykjavik", "Iceland")
city_description("Pasig")