from copy import deepcopy
import random
from typing import Optional
from eckity.evaluators.simple_population_evaluator import Individual
from eckity.genetic_encodings.gp.tree.tree_individual import Tree
from eckity.genetic_operators.mutations.vector_n_point_mutation import (
    VectorNPointMutation,
)
from eckity.genetic_operators.genetic_operator import GeneticOperator


class VectorShuffleIndexesMutation(VectorNPointMutation):
    """
    Uniform N Point indexes shuffle mutation.
    """

    def __init__(self, probability=1.0, events=None, n=1):
        super().__init__(probability=probability, arity=1, events=events, n=n)

    def attempt_operator(self, individuals, attempt_num):
        """
        Attempt to perform the mutation operator
        Parameters
        ----------
        individuals : list of individuals
            individuals to mutate
        attempt_num : int
            Current attempt number
        Returns
        ----------
        tuple of (bool, list of individuals)
            first return value determines if the the attempt succeeded
            second return value is the operator result
        """
        succeeded = True
        for individual in individuals:
            for i in range(self.n):
                if random.random() < self.probability:
                    swap_indx = random.randint(0, individual.size() - 2)
                    if swap_indx >= i:
                        swap_indx += 1
                    tmp = individual.cell_value(swap_indx)
                    individual.set_cell_value(swap_indx, individual.cell_value(i))
                    individual.set_cell_value(i, tmp)

        self.applied_individuals = individuals
        return succeeded, individuals


class TreeShrinkMutation(GeneticOperator):
    def __init__(self, probability=1, arity=1, events=None):
        """
        This operator shrinks the *individual* by choosing randomly a branch and
        replacing it with one of the branch's arguments (also randomly chosen).
        """
        super().__init__(probability=probability, arity=arity, events=events)

    def apply(self, individuals_: list[Tree]) -> list[Tree]:
        """
        Apply mutation in-place on `individuals`.
        Returns
        -------
        List of mutated individuals.
        """
        individuals = deepcopy(individuals_)
        for individual in individuals:
            copy = deepcopy(individual)
            if random.random() > self.probability:
                continue

            while individual.tree == copy.tree:
                # Convert subtree list to a `Tree` object, using deepcopy hackery.
                subtree = deepcopy(individual)
                subtree.tree = individual.random_subtree()
                sub_subtree = subtree.random_subtree()
                index = index_of_subtree(individual.tree, subtree.tree)
                assert index is not None
                replace_subtree(individual, index, sub_subtree)

        self.applied_individuals = individuals
        return individuals


def index_of_subtree(tree: list, subtree: list) -> Optional[int]:
    """
    Return the index of `subtree` in `tree`.
    """
    for i in range(len(tree)):
        if tree[i : i + len(subtree)] == subtree:
            return i
    return None


def replace_subtree(tree: Tree, index: int, new_subtree: list):
    """
    Replace the subtree starting at `index` with `new_subtree`

    Parameters
    ----------
    subtree - new subtree to replace the some existing subtree in this individual's tree

    Returns
    -------
    None
    """
    end_i = tree._find_subtree_end([index])
    left_part = tree.tree[:index]
    right_part = tree.tree[(end_i + 1) :]
    tree.tree = left_part + new_subtree + right_part
