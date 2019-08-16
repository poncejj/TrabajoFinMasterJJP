GENETIC_ALGORITHM = 'GA'
TABU_SEARCH = 'TS'
ANT_COLONY_OPT = 'AC'

ALGORITHM_CHOICES = [
	(GENETIC_ALGORITHM, 'Genetic Algorithm'),
    (TABU_SEARCH, 'Tabu Search'),
    (ANT_COLONY_OPT, 'Ant Colony Optimization'),
]
PROBLEM_CHOICES = (
    (1, ("Best route acording demand")),
    (2, ("Best rout acording the type of product"))
)