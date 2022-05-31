from itertools import count
import pdb
from models.country import Country
from models.traveler import Traveler
from models.visit import Visit

import repositories.country_repository as country_repository
import repositories.traveler_repository as Traveler_repository
import repositories.visit_repository as visit_repository

# visit_repository.delete_all()
# country_repository.delete_all()
# Traveler_repository.delete_all()

visit_repository.select_all()
country_repository.select_all()
Traveler_repository.select_all()

traveler1 = Traveler('Tommy')
Traveler_repository.save(traveler1)

traveler2 = Traveler('Bob')
Traveler_repository.save(traveler2)

country1 = Country('France','Paris')
country_repository.save(country1)

country2 = Country('Germany','Berlin')
country_repository.save(country2)