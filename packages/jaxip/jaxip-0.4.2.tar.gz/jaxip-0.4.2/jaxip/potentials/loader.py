import random
from collections import defaultdict
from typing import List

import jax.numpy as jnp
from jaxip.datasets.base import StructureDataset
from jaxip.types import Array


class StructureDataLoader:
    """
    A structure dataloader which samples force and energy from the input dataset.
    It is used particularly for the training models in potentials.
    """

    def __init__(
        self,
        dataset: StructureDataset,
        elements: List[str],
        batch_size: int = 1,
        shuffle: bool = False,
        seed: int = 2022,
    ):
        self.dataset = dataset
        self.elements = elements
        self.batch_size = batch_size
        self.shuffle = shuffle
        random.seed(seed)

    def generate_energy(self) -> Array:

        structures = random.choices(self.dataset, k=self.batch_size)

        energies = jnp.asarray([structure.total_energy for structure in structures])
        return jnp.squeeze(energies)

    def generate_force(self):

        forces = defaultdict()
        state = defaultdict(int)

        while (len(state) >= 0) and all([v < self.batch_size for v in state.values()]):

            structure = random.choice(self.dataset)
            for element in self.elements:

                if state[element] >= self.batch_size:
                    continue
                aids = structure.select(element)

                if forces[element] is None:
                    forces[element] = structure.force[aids]
                else:
                    forces[element] = jnp.concatenate(
                        [
                            jnp.asarray(forces[element]).reshape(1, 3),
                            structure.force[aids],
                        ]
                    )
                state[element] = forces[element].shape[0]

        return forces
