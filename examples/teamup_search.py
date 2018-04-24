from daftlistings import TeamUpWith, Teamup, County

t = Teamup()
t.set_county(County.DUBLIN)
t.set_team_up_with(TeamUpWith.ANY)
t.set_rent(1000)

results = t.get_results()

for r in results:
    print("Name: " + r.name())
    print("Gender: " + r.gender())
    print("Price Range: " + r.price_range())
    print("Areas of Interest: " + r.areas_of_interest())
    print("Looking for: " + r.looking_for())
    print("Length of Lease: " + r.length_of_lease())
    print("Date available: " + r.date_available())
    print("Date entered: " + r.date_entered())
    print("URL: " + r.url())
    print("")
