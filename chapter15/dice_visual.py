import pygal

from die import Die

die_1 = Die(8)
die_2 = Die(8)

results = []
for roll_num in range(1000000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wyniki rzucania dwiema kośćmi 1,000,000 razy"
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"

hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_visual.svg')

# 15.9 - multiplication
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar(x_label_rotation=90)
hist.force_uri_protocol = 'http'

hist.title = "Pomnożone wyniki rzucania dwiema kośćmi 1,000 razy"
hist.x_labels = [str(x) for x in range(1, max_result + 1)]
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"

hist.add('D8 * D8', frequencies)
hist.render_to_file('multiplication_dice_visual.svg')
