import pygal

from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(1000000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wyniki rzucania trzema kośćmi 1,000,000 razy"
hist.x_labels = [str(x) for x in range(3, max_result + 1)]
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('triple_dice_visual.svg')
