import random
from copy import deepcopy
from typing import List

from eckity.genetic_operators.genetic_operator import GeneticOperator
from eckity.genetic_encodings.ga.vector_individual import Vector
from tests.test_tree_shrink_mutation import individuals


class VectorUniformCrossover(GeneticOperator):
    def __init__(self, probability=1, events=None):
        """
        Vector N Point Mutation.

        Randomly chooses N vector cells and performs a small change in their values.

        Parameters
        ----------
        probability : float
            The probability of the mutation operator to be applied

        arity : int
            The number of individuals this mutation is applied on

        events: list of strings
            Events to publish before/after the mutation operator
        """
        self.individuals = None
        self.applied_individuals = None
        super().__init__(probability=probability, arity=2, events=events)

    def apply(self, individuals: List[Vector]) -> List[Vector]:
        """
        Attempt to perform the mutation operator

        Parameters
        ----------
        individuals : list of individuals
            individuals to perform crossover on

        Returns
        ----------
        list of individuals
            individuals after the crossover
        """
        individuals = deepcopy(individuals)
        self.individuals = individuals

        for i in range(len(individuals[0].vector)):
            if random.random() < self.probability:
                individuals[0].vector[i], individuals[1].vector[i] = (
                    individuals[1].vector[i],
                    individuals[0].vector[i],
                )

        self.applied_individuals = individuals
        return individuals
