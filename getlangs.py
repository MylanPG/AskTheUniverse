import googletrans
from googletrans import constants
import pprint
from pprint import *

print("Total supported languages:", len(constants.LANGUAGES))
print("Languages:")

pprint(constants.LANGUAGES)
