import math
import requests
import time

max_velocity = 2  # lightyear/day
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
engine_kpd = 0
electricity_power = 0
electricity = 0
growth_coeficent = 0
electricity_kpd = 0
need_energy = 0
bad_flighting_plan = requests.get("https://dt.miet.ru/ppo_it_final", headers=token).json()
fly_plan = {1:[20, 40]}
day = 1
current_distance = 0
mission = 1
history = {}
resources = {}
authoclav = []
consumed = 20


def count_energy(*args):
    global need_energy
    need_energy = sum(list(range(temperature + 1)))


def update_mass(*args):
    global ship_mass, sh_population
    ship_mass = 192 + sh_population


def update_electricity(*args):
    global electricity_power, electricity
    electricity = electricity_power * power_per_fuel


def update_velocity(*args):
    global max_velocity, reactor_power, ship_mass, velocity
    update_mass()
    velocity = 2 * (engine_kpd * 100 / 80) * (200 / ship_mass)


def update_growth_coefficent(*args):
    global growth_coeficent, temperature
    global oxygen, consumed
    growth_coeficent = math.sin((math.pi * (-1)) / 2 +
                                (math.pi * (temperature + 0.5 * 20) / 40))


def update_sh(*args):
    global sh_population, growth_coeficent
    sh_population += sh_population * growth_coeficent


def autoclave_maintenance(*args):
    global sh_population, min_SH_population
    sh_population = min_SH_population

def calculate(*args):
    global max_velocity, fuel, max_velocity, max_engine_kpd
    global power_per_fuel, temperature, oxygen, reactor_power
    global min_temperature, max_temperature, max_oxygen_consuption
    global ship_mass, ship_start_mass, velocity, engine_kpd
    global electricity_power, electricity, growth_coeficent
    global electricity_kpd, need_energy, fly_plan, day, engine_kpd
    global mission, current_distance, authoclav, consumed
    distance, cargo = fly_plan[mission][0], fly_plan[mission][1]
    fuel = 0
    temperature = 10
    oxygen = 20
    reactor_power = 0
    ship_mass = 192 + 8
    velocity = 0
    electricity_power = 0
    electricity = 0
    need_energy = 0
    day = 1
    temperature = 30
    count_energy()
    electricity_kpd = 11 * electricity / 100
    engine_kpd = 1 - electricity_kpd
    sh_population = 8
    update_growth_coefficent(20)
    update_sh()
    update_velocity()
    mission = 1
    consumed = 20 * sh_population
    current_distance += velocity
    history[day] = [mission, current_distance, sh_population,
                    fuel, oxygen, velocity]
    resources[day] = [sh_population, fuel, oxygen]
    while mission <= len(fly_plan):
        if sh_population < fly_plan[mission][1] + 8:
            temperature = 30
            engine_kpd = 1 - 0.43
            electricity_kpd = 0.43
        else:
            temperature = 20
            electricity_kpd = 0.2
            engine_kpd = 0.8
        update_growth_coefficent()
        update_sh()
        oxygen = 20 * sh_population
        update_mass()
        update_velocity()
        current_distance += velocity
        fuel += 100
        history[day] = [mission, current_distance, sh_population,
                        fuel, oxygen, velocity]
        resources[day] = [sh_population, fuel, oxygen]
        if current_distance > distance:
            mission += 1
            current_distance = 0
            if mission <= len(fly_plan):
                distance, cargo = fly_plan[mission][0], fly_plan[mission][1]
            else:
                break
            velocity = 0
            temperature = 0
            sh_population = 8
        sh_population += sh_population
        day += 1
        authoclav = [temperature, consumed]

calculate()
