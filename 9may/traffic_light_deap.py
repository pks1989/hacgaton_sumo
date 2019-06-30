import random
import sys
import subprocess

from deap import creator, base, tools, algorithms


def correct_time(x):
    if x <= 0:
        return 1
    return x


def eval(script_path, max_speed):
    def eval_backed(individual):
        #  sumo_params = ''
        #  for i in individual:
        #      sumo_params = sumo_params + ' ' + str(correct_time(i)) + ' 3'
        sumo_params = ' '.join([str(i) for i in individual])
        sumo_cmd = 'php {} {} '.format(script_path, sumo_params)
        sumo_out = subprocess.check_output(sumo_cmd, shell=True)
        sumo_out = sumo_out.decode('ascii')
        print(sumo_out)
        travel_time, speed = sumo_out.split(' ')
        travel_time, speed = float(travel_time), float(speed)

        if speed > max_speed:
            return -999
        if travel_time > 300:
            return -999
        else:
            # return 1 + (travel_time + 1e-6)
            return -travel_time
    return eval_backed


if __name__ == '__main__':
    n_lights = int(sys.argv[2])
    scrip_path = sys.argv[1]
    max_speed = int(sys.argv[3])

    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)

    toolbox = base.Toolbox()

    toolbox.register("attr_bool", random.randint, 10, 120)
    toolbox.register(
        "individual", tools.initRepeat,
        creator.Individual, toolbox.attr_bool,
        n=n_lights)
    toolbox.register(
        "population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("evaluate", eval(scrip_path, max_speed))
    toolbox.register("mate", tools.cxTwoPoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=5)

    population = toolbox.population(n=50)

    n_generations = 20
    for gen in range(n_generations):
        print('-' * 80)
        print('Generation: {}'.format(gen))
        offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.15)
        fits = toolbox.map(toolbox.evaluate, offspring)
        for fit, ind in zip(fits, offspring):
            print('Traffic lights time: ', [correct_time(i) for i in ind])
            ind.fitness.wvalues = fit
        population = toolbox.select(offspring, k=len(population))
        print('-' * 80)
    top10 = tools.selBest(population, k=10)

    print(top10)

# pip install virtualenv
# python3 -m venv env