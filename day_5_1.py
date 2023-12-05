from io import TextIOWrapper
from parse import *

class MapClass:
    def __init__(self) -> None:
        self.map_entries = list()

    def processValue(self, value_in:int) -> int:
        for entry in self.map_entries:
            dest_start = entry[0]
            source_start = entry[1]
            range_length = entry[2]
            if value_in in range(source_start, source_start + range_length):
                value_out = dest_start + (value_in - source_start)
                return value_out
        return value_in
    
    def add_map_entry(self, dest_start:int, source_start:int, range_length:int):
        self.map_entries.append((dest_start, source_start, range_length))

def read_map(file:TextIOWrapper, map:MapClass):
    file.readline() # name
    map_line = file.readline().strip()
    while map_line != "":
        parsed_map_line = parse("{dest_start:d} {source_start:d} {range_length:d}", map_line)
        map.add_map_entry(parsed_map_line["dest_start"],
                          parsed_map_line["source_start"],
                          parsed_map_line["range_length"])
        map_line = file.readline().strip()

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def run():
    seed_to_soil_map = MapClass()
    soil_to_fertilizer_map = MapClass()
    fertilizer_to_water_map = MapClass()
    water_to_light_map = MapClass()
    light_to_temperature_map = MapClass()
    temperature_to_humidity_map = MapClass()
    humidity_to_location_map = MapClass()
    
    with open("day_5_input.txt") as almanac_file:
        seed_line = almanac_file.readline()
        seed_line_parsed = parse("seeds: {seeds}", seed_line)
        seeds = map(int, seed_line_parsed["seeds"].split())

        almanac_file.readline()

        read_map(almanac_file, seed_to_soil_map)
        read_map(almanac_file, soil_to_fertilizer_map)
        read_map(almanac_file, fertilizer_to_water_map)
        read_map(almanac_file, water_to_light_map)
        read_map(almanac_file, light_to_temperature_map)
        read_map(almanac_file, temperature_to_humidity_map)
        read_map(almanac_file, humidity_to_location_map)

        lowest_location = None

        for (start, count) in chunks(list(seeds), 2):
            print(f"Checking {count} seeds from {start}")
            for seed in range(start, start + count):
                soil = seed_to_soil_map.processValue(seed)
                fertilizer = soil_to_fertilizer_map.processValue(soil)
                water = fertilizer_to_water_map.processValue(fertilizer)
                light = water_to_light_map.processValue(water)
                temperature = light_to_temperature_map.processValue(light)
                humidity = temperature_to_humidity_map.processValue(temperature)
                location = humidity_to_location_map.processValue(humidity)
                
                if lowest_location is None:
                    lowest_location = location
                else:
                    lowest_location = location if location < lowest_location else lowest_location
        
        print(lowest_location)


if __name__ == "__main__":
    run()