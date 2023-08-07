#  Copyright (c) 2023.
#  ProrokLab (https://www.proroklab.org/)
#  All rights reserved.
from tensordict.nn import TensorDictModule
from torch import nn
from torchrl.collectors import SyncDataCollector
from torchrl.envs import ParallelEnv
from torchrl.envs.libs.gym import GymEnv
from torchrl.envs.libs.vmas import VmasEnv

if __name__ == "__main__":
    vmas_env = lambda: VmasEnv("flocking", num_envs=2, n_agents=3)
    vmas_parallel_env = lambda: ParallelEnv(10, vmas_env)

    flocking_policy = TensorDictModule(
        nn.Linear(18, 2), in_keys=["observation"], out_keys=["action"]
    )
    gym_env = lambda: GymEnv("Pendulum-v1", device="cpu")
    gym_parallel_env = lambda: ParallelEnv(10, gym_env)

    pendulum_policy = TensorDictModule(
        nn.Linear(3, 1), in_keys=["observation"], out_keys=["action"]
    )

    coll = SyncDataCollector(
        gym_parallel_env,
        pendulum_policy,
        total_frames=20000,
        max_frames_per_traj=5,
        frames_per_batch=145,
        # env_batch_size_mask=[True, False, True],
        split_trajs=False,
    )

    # multi_coll = MultiSyncDataCollector(
    #     [vmas_parallel_env],
    #     flocking_policy,
    #     total_frames=20000,
    #     max_frames_per_traj=5,
    #     frames_per_batch=200,
    #     env_batch_size_mask=[True, False, True],
    #     split_trajs=False,
    # )

    for data in coll:
        print("Ending", data)
        # print("Traj id", data["traj_ids"])
        break
