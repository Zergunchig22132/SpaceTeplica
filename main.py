import math
import requests

max_velocity = 2 #lightyear/day
fuel = 0
max_engine_kpd = 0.8
engine_kpd = 0
power_per_fuel = 11
temperature = 0
oxygen = 0
sin = 0
reactor_power = 0
min_temperature = 0
max_temperature = 30
max_oxygen_consuption = 60
min_SH_population = 8
sh_population = 8
ship_start_mass = 192
growth_factor = 0
ship_mass = ship_start_mass + sh_population
velocity = 0
engine_power = 0
electricity_power = 0
electricity = 0
growth_coeficent = 0

def count_energy(need_tempreture):
    return sum(list(range(need_tempreture + 1))) 

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

    
def autoclave_maintenance(*args):
    global sh_population, min_SH_population
    sh_population = min_SH_population
    
