#!/usr/bin/env python3
from os import path
import sys
sys.setrecursionlimit(10000)

def get_dir_name():
    return path.dirname(path.abspath(__file__))


"""
class Entity:

    _orbits = None

    def __init__(self, name):
        self.name = name

    def orbits(self, entity):
        if self._orbits:
            raise
        self._orbits = entity
    
    def get_orbits(self):
        return self._orbits

def get_input():
    entities = {} 
    with open(path.join(get_dir_name(), "input6.txt"), "r") as f:
        for line in f.readlines():
            ent1, ent2 = line.strip().split(')')
            if not entities.get(ent1):
                entities[ent1] = Entity(ent1)
            if not entities.get(ent2):
                entities[ent2] = Entity(ent2)
            entities[ent2].orbits(entities[ent1])

    return entities


def get_total_orbits(entity, seen_orbits):
    if entity in seen_orbits:
        raise
    seen_orbits.add(entity)
    if not entity.get_orbits():
        print(entity.name + " is not orbiting anything")
        return 0
    print(entity.name + " orbits " + entity._orbits.name)
    return 1 + get_total_orbits(entity.get_orbits(), seen_orbits)


def solve(entities):
    total_orbits = 0
    for entity in entities.values():
        print("getting orbit for " + entity.name)
        added_orbits = get_total_orbits(entity, set())
        print(entity.name + " orbits " + str(added_orbits))
        total_orbits += added_orbits
    return total_orbits

"""
#print(solve(get_input()))  # 295834

class Entity:


    def __init__(self, name):
        self._orbits = []
        self.name = name

    def orbits(self, entity):
        if self.name == 'YOU':
            print("adding " + entity.name + " to YOU")
        if entity not in self._orbits:
            self._orbits += [entity]
    
    def get_orbits(self):
        return self._orbits

def get_input():
    entities = {}
    with open(path.join(get_dir_name(), "input6.txt"), "r") as f:
        for line in f.readlines():
            ent1, ent2 = line.strip().split(')')
            print((ent1, ent2))
            if not entities.get(ent1):
                entities[ent1] = Entity(ent1)
            if not entities.get(ent2):
                entities[ent2] = Entity(ent2)
            print("adding " + entities[ent1].name + " to " + entities[ent2].name)
            entities[ent2].orbits(entities[ent1])
            print("adding " + entities[ent2].name + " to " + entities[ent1].name)
            entities[ent1].orbits(entities[ent2])

        print(entities['YOU']._orbits)
    return entities


def solve2(you):
    print(you._orbits)
    visited = set()
    for orb in you._orbits:
        print(orb.name)
    lifo_queue = [(ent, 0) for ent in you._orbits]
    while lifo_queue:
        ent, distance = lifo_queue.pop()
        if ent.name in visited:
            continue
        visited.add(ent.name)
        if ent.name == 'SAN':
            return distance - 1
        for orb in ent._orbits:
            lifo_queue.append((orb, distance + 1))
    raise

print(solve2(get_input()['YOU']))  # 361
