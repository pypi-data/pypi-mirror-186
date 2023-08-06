from copy import deepcopy
import random
from eckity.genetic_operators.selections.selection_method import SelectionMethod


class RouletteSelection(SelectionMethod):
    def __init__(self, k: int, higher_is_better=False, events=None):
        """
        Select 'k' individuals based on their fitness and a random roulette spin.
        Parameters
        ----------
        k: int
            Number of selected individuals.
        Returns
        -------
            List of length 'k' of chosen individuals.
        """
        super().__init__(events=events, higher_is_better=higher_is_better)
        self.k = k
        self.higher_is_better = higher_is_better

    def select(self, source_inds, dest_inds):
        """
        Parameters
        ----------
        source_inds: Source individuals to select from.
        dest_inds: List which selected individuals will be appended to.
        """
        sorted_individuals = sorted(
            source_inds,
            key=lambda ind: ind.get_augmented_fitness(),
            reverse=self.higher_is_better,
        )
        sum_fits = sum(ind.get_augmented_fitness() for ind in source_inds)
        chosen = []
        for _ in range(self.k):
            u = random.random() * sum_fits
            sum_ = 0
            for individual in sorted_individuals:
                sum_ += individual.get_augmented_fitness()
                if sum_ > u:
                    chosen.append(individual)
                    break

        for individual in chosen:
            dest_inds.append(individual.clone())
        self.selected_individuals = dest_inds
        return dest_inds


class RandomSelection(SelectionMethod):
    def __init__(self, k: int, higher_is_better=False, events=None):
        """
        Randonly select 'k' individuals.
        Parameters
        ----------
        k: int
            Number of selected individuals.
        Returns
        -------
            List of length 'k' of chosen individuals.
        """
        super().__init__(events=events, higher_is_better=higher_is_better)
        self.k = k
        self.higher_is_better = higher_is_better

    def select(self, source_inds, dest_inds):
        """
        Parameters
        ----------
        source_inds: Source individuals to select from.
        dest_inds: List which selected individuals will be appended to.
        """
        chosen = random.sample(source_inds, self.k)
        for individual in chosen:
            dest_inds.append(individual.clone())
        self.selected_individuals = dest_inds
        return dest_inds


class StochasticUniversalSelection(SelectionMethod):
    def __init__(self, k: int, higher_is_better=False, events=None):
        """
        Randonly select 'k' individuals.
        Parameters
        ----------
        k: int
            Number of selected individuals.
        Returns
        -------
            List of length 'k' of chosen individuals.
        """
        super().__init__(events=events, higher_is_better=higher_is_better)
        self.k = k
        self.higher_is_better = higher_is_better

    def select(self, source_inds, dest_inds):
        """
        Parameters
        ----------
        source_inds: Source individuals to select from.
        dest_inds: List which selected individuals will be appended to.
        """
        sum_fits = sum(ind.get_augmented_fitness() for ind in source_inds)
        sorted_individuals = sorted(
            source_inds,
            key=lambda ind: ind.get_augmented_fitness(),
            reverse=self.higher_is_better,
        )
        distance = sum_fits / float(self.k)
        start = random.uniform(0, distance)
        points = [start + i * distance for i in range(self.k)]
        chosen = []

        for p in points:
            i = 0
            sum_ = sorted_individuals[0].get_augmented_fitness()
            while sum_ < p:
                i += 1
                sum_ += sorted_individuals[i].get_augmented_fitness()
            chosen.append(sorted_individuals[i])

        for individual in chosen:
            dest_inds.append(individual.clone())
        self.selected_individuals = dest_inds
        return dest_inds
