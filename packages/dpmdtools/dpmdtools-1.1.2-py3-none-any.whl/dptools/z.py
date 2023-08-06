import re
import socket

sim_queue_file = 'sims'

def _gen_simulation(sim_queue_file):
    with open(sim_queue_file) as file:
        simulations = [l for line in file for l in line.split()]
    return simulations

s = _gen_simulation(sim_queue_file)
hostname = 'cori09'
host = re.sub("[^a-z]*", "", socket.gethostname())
host = re.sub("[^a-z]*", "", hostname)

