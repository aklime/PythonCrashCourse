import pygal

from die import Die

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wyniki rzucania kością 1,000 razy"
hist.x_labels = [str(x) for x in range(1, die.num_sides + 1)]
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
