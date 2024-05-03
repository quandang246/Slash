# slashconf.py

import slash
from .microwave import SimpleMicrowave, AdvancedMicrowave
from .heating_plate import Heating_palte

# fixture definition
@slash.fixture(scope='session')                                        # Fixture Scopes
@slash.parametrize('Microwave', [SimpleMicrowave, AdvancedMicrowave])  # Fixture Parametrization     
def microwave(Microwave, this):
    returned = Microwave(ID="M111")

    @this.test_start                                                   # Test Start/End for Widely Scoped Fixtures
    def on_test_start():
        returned.turn_on()

    @this.test_end                                                     # Test Start/End for Widely Scoped Fixtures
    def on_test_end():
        returned.turn_off()

    yield returned                                                     # Yielding Fixtures

    print('Hurray! the session has ended')
    returned.turn_off()

    return returned

def get_appropriate_heating_plate_for(microwave):
    if microwave.get_ID() == "M111":
        return Heating_palte(ID="H111")
    else:
        return Heating_palte(ID="None")

# Fixture Needing Other Fixtures
@slash.fixture(scope='module')                                          # Fixture Scopes
@slash.requires(True)                                                   # Fixture Requirements
def heating_plate(microwave, this):
    @this.add_cleanup                                                   # Fixture Cleanups
    def cleanup():
        print('Hurray! We are finished with this module')
    return get_appropriate_heating_plate_for(microwave)

x = "10"
@slash.generator_fixture(autouse=True, scope='session')                 # Autouse Fixtures, Generator Fixtures
def autouse_fixture():
    yield from x                                                        
    print (f"X value: " + x)
    print ("Autouse fixture")

@slash.fixture()
def used_fixture1():
    print ("Using used_fixture1")
    pass

@slash.fixture()
def used_fixture2():
    print ("Using used_fixture2")
    pass

# Listing Available Fixtures
# slash list --only-fixtures test.py
