# test.py

import slash
from .slashconf import microwave, heating_plate, used_fixture1, used_fixture2

def test_microwave_turns_on(m: slash.use('microwave')):                         # Aliasing Fixtures
    m.turn_on()
    assert m.get_state() == True

def test_heating_plate_usage(microwave, heating_plate):
    assert microwave.get_ID() == 'M111' and heating_plate.get_ID() == "H111"

@slash.use_fixtures(["used_fixture1", "used_fixture2"])                         # The use_fixtures Decorator
def test_used_fixture():
    pass
