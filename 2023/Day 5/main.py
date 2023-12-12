seeds = [79, 14, 55, 13]
seed_to_soil_map = []
seed_to_soil_label = "seed-to-soil map:\n"
soil_to_fertilizer_map = []
soil_to_fertilizer_label = "soil-to-fertilizer map:\n"
fertilizer_to_water_map = []
fertilizer_to_water_label = "fertilizer-to-water map:\n"
water_to_light_map = []
water_to_light_label = "water-to-light map:\n"
light_to_temperature_map = []
light_to_temperature_label = "light-to-temperature map:\n"
temperature_to_humidity_map = []
temperature_to_humidity_label = "temperature-to-humidity map:\n"
humidity_to_location_map = []
humidity_to_location_label = "humidity-to-location map:\n"


# def seed_to_soil(seed_to_soil_map, seed):
#     for source_start, dest_start, range_length in seed_to_soil_map:

def mapping(mapper, data):
    for source_start, dest_start, range_length in mapper:
        if data >= source_start and data <= source_start + range_length:
            return dest_start + data - source_start




def soil_to_fertilizer(soil_to_fertilizer_map, soil):
    if soil_to_fertilizer_map.get(soil) is None:
        return soil
    else:
        return soil_to_fertilizer_map[soil]


def fertilizer_to_water(fertilizer_to_water_map, fertilizer):
    if fertilizer_to_water_map.get(fertilizer) is None:
        return fertilizer
    else:
        return fertilizer_to_water_map[fertilizer]


def water_to_light(water_to_light_map, water):
    if water_to_light_map.get(water) is None:
        return water
    else:
        return water_to_light_map[water]


def light_to_temperature(light_to_temperature_map, light):
    if light_to_temperature_map.get(light) is None:
        return light
    else:
        return light_to_temperature_map[light]


def temperature_to_humidity(temperature_to_humidity_map, temperature):
    if temperature_to_humidity_map.get(temperature) is None:
        return temperature
    else:
        return temperature_to_humidity_map[temperature]


def humidity_to_location(humidity_to_location_map, humidity):
    if humidity_to_location_map.get(humidity) is None:
        return humidity
    else:
        return humidity_to_location_map[humidity]


def process_line(process_line_map, line):
    return list(map(int, line.strip().split(" ")))


def seed_to_location(seed_to_location_map, seed):
    soil = seed_to_soil(seed)
    fertilizer = soil_to_fertilizer(soil)
    water = fertilizer_to_water(fertilizer)
    light = water_to_light(water)
    temperature = light_to_temperature(light)
    humidity = temperature_to_humidity(temperature)
    location = humidity_to_location(humidity)
    return location


def main():
    with open("input.txt") as file:
        lines = file.readlines()
        seeds = list(map(int, lines[0].strip().split(" ")[1:]))

        i = 1
        while i < len(lines):
            if lines[i] == seed_to_soil_label:
                i += 1
                while i < len(lines) and lines[i] != "\n":
                    source_start, dest_start, range_length = process_line(
                        lines[i])
                    populate_mapper(seed_to_soil_map,
                                    source_start, dest_start, range_length)
                    i += 1
            elif lines[i] == soil_to_fertilizer_label:
                i += 1
                while i < len(lines) and lines[i] != "\n":
                    source_start, dest_start, range_length = process_line(
                        lines[i])
                    populate_mapper(soil_to_fertilizer_map,
                                    source_start, dest_start, range_length)
                    i += 1
            elif lines[i] == fertilizer_to_water_label:
                i += 1
                while i < len(lines) and lines[i] != "\n":
                    source_start, dest_start, range_length = process_line(
                        lines[i])
                    populate_mapper(fertilizer_to_water_map,
                                    source_start, dest_start, range_length)
                    i += 1
            elif lines[i] == water_to_light_label:
                i += 1
                while i < len(lines) and lines[i] != "\n":
                    source_start, dest_start, range_length = process_line(
                        lines[i])
                    populate_mapper(water_to_light_map,
                                    source_start, dest_start, range_length)
                    i += 1
            elif lines[i] == light_to_temperature_label:
                i += 1
                while i < len(lines) and lines[i] != "\n":
                    source_start, dest_start, range_length = process_line(
                        lines[i])
                    populate_mapper(light_to_temperature_map,
                                    source_start, dest_start, range_length)
                    i += 1
            elif lines[i] == temperature_to_humidity_label:
                i += 1
                while i < len(lines) and lines[i] != "\n":
                    source_start, dest_start, range_length = process_line(
                        lines[i])
                    populate_mapper(temperature_to_humidity_map,
                                    source_start, dest_start, range_length)
                    i += 1
            elif lines[i] == humidity_to_location_label:
                i += 1
                while i < len(lines) and lines[i] != "\n":
                    source_start, dest_start, range_length = process_line(
                        lines[i])
                    populate_mapper(humidity_to_location_map,
                                    source_start, dest_start, range_length)
                    i += 1
            i += 1

        min_location = float("inf")
        for seed in seeds:
            min_location = min(min_location, seed_to_location(seed))

        print(min_location)


if __name__ == "__main__":
    main()
