import math
import requests

max_velocity = 2 #lightyear/day
fuel = 0
max_engine_kpd = 0.8
engine_kpd = 0
power_per_fuel = 11
temperature = 0
oxygen = 0
reactor_power = 0
min_temperature = 0
max_temperature = 30
max_oxygen_consuption = 60
min_SH_population = 8
sh_population = 8
ship_start_mass = 192
token = {'X-Auth-Token': 'jh2gskwd'}
ship_mass = ship_start_mass + sh_population
velocity = 0
engine_power = 0
electricity_power = 0
electricity = 0
growth_coeficent = 0
electricity_kpd = 0
need_energy = 0
flighting_plan = requests.get("https://dt.miet.ru/ppo_it_final", params=token)
day = 1


def count_energy(*args):
    global need_energy
    need_energy = sum(list(range(temperature + 1)))


def update_mass(*args):
    global ship_mass, sh_population
    ship_mass = 192 + sh_population

    
def update_engine(*args):
    global engine_power, engine_kpd, reactor_power
    global electricity_power
    engine_power = engine_kpd * reactor_power
    electricity_power = (1 - engine_kpd) * reactor_power

    
def update_electricity(*args):
    global electricity_power, electricity
    electricity = electricity_power * power_per_fuel

    
def update_velocity(*args):
    global max_velocity, reactor_power, ship_mass, velocity
    update_mass()
    update_engine()
    velocity = max_velocity * (engine_power / 80) * (200 / ship_mass)

    
def update_growth_coefficent(*args):
    global growth_coeficent, temperature
    global oxygen
    growth_coeficent = math.sin((math.pi * (-1)) / 2 +
                                (math.pi * (temperature + 0.5 * oxygen) / 40))
    
    
def update_sh(*args):
    global sh_population, growth_coeficent
    sh_population = sh_population + sh_population * growth_coeficent
    
    
def autoclave_maintenance(*args):
    global sh_population, min_SH_population
    sh_population = min_SH_population
    
def globalization(*args):
    def start_flight(distance, cargo, *args):
    global max_velocity, fuel, max_velocity, max_engine_kpd
    global power_per_fuel, temperature, oxygen, reactor_power
    global min_temperature, max_temperature, max_oxygen_consuption
    global ship_mass, ship_start_mass, velocity, engine_power
    global electricity_power, electricity, growth_coeficent
    global electricity_kpd, need_energy, flighting_plan, day
    fuel = 0
    temperature = 0
    oxygen = 0
    reactor_power = 0
    ship_mass = 192 + 8
    pass
