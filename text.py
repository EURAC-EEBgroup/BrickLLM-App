# CREATE TEXT FOPR WURTH SHOPS

def text_shops_ontology(project_name, building_owner, city, name_building, 
                        latitude, longitude, n_HVAC_zones, building_area, air_temperature_sensors,
                        building_electricity_meter, store_electricity_uuid,
                        uuid_external_air_temperature_sens):
    
    '''
    Create text to generate brick ontology for each store of WURTH dataset

    Param
    ------
    project_name: specify the name of the project. E.g. MODERATE
    building_owner: specify the name of the company, owner of the building/s.
    city: specify the name of the city where the building is located
    type_building: could be a simple building, store, office, etc.
    name_building: specific name of the building
    latitude: latitude where the building is located
    longitude: longitude where the building is located
    n_HVAC_zones: number of HVAC zones in the store.
    building_area: gross or net surface of the store
    air_temperature_sensors: list of UUIDs for air temperature sensors. E.g. ["adgtsg45hfg","gfbsdhuz78","tshuehjr"]
    building_electricity_meter: UUID of the overall building electricity meter
    store_electricity_uuid: UUID of store electricity 
    uuid_external_air_temperature_sens: UUID for the sensor measuring the external temperature
    '''

    result_air_temperature = ""
    for i in range(n_HVAC_zones):
        result_air_temperature += f'In the HVAC zone {i+1}, there is the air temperature sensor having the following UUID "{air_temperature_sensors[i]}". '

    text = f"In the project called {project_name}, there is a building called {name_building} located in {city}, in which there is a store called {name_building}. The building has latitude: {latitude} and longitude: {longitude}. \
    The surface of the store is {building_area} square meters. It has {n_HVAC_zones} HVAC zones. {result_air_temperature} \
    The building has an energy meter with UUID {building_electricity_meter}. \
    The store has an energy meter with UUID {store_electricity_uuid}. \
    The owner of the building is {building_owner}. \
    There is also an external air temperature sensor with UUID {uuid_external_air_temperature_sens}. \
    The database of sensors is available at the following URL: http://193.106.182.151/store_data/api/docs#/"

    return text


project_name = "MODERATE"
building_owner = "WURTH"
city = "Cremona"
latitude = "10.00359"
longitude = "45.15489"
n_HVAC_zones = 4
building_area = 367
name_building = "BCFT"
air_temperature_sensors = ["082262f7-140f-486c-b639-2bcfbc7eeab3", "7473f2b2-a299-4e28-9146-c4ff15269bd1",
                           "465b01cc-8436-4553-be8b-38fdc9e62491", "b14b78f2-4840-453d-b098-75b419e30e9b"]
uuid_external_air_temperature_sens = "9bbc3f66-08d7-4c2a-a58f-b4e6632c9978"
building_electricity_meter = "a1dd4c6c-0a6e-4064-9fc0-029941a33782"
store_electricity_uuid = "753ddfc3-a24e-46ac-b642-c17937a79258"

text = text_shops_ontology(project_name, building_owner,city,name_building,
                        latitude, longitude, n_HVAC_zones, building_area, air_temperature_sensors,
                        building_electricity_meter, store_electricity_uuid, uuid_external_air_temperature_sens)

