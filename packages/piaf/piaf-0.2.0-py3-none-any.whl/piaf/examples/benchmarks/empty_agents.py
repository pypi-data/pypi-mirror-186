# coding: utf-8
from __future__ import annotations

import asyncio
from time import perf_counter_ns

from piaf.ptf import AgentPlatform
from piaf.agent import Agent

async def main(n: int) -> None:
    ptf = AgentPlatform("localhost")

    async def _launch_agent(name: str) -> None:
        aid = await ptf.agent_manager.create(
            Agent, name
        )
        await ptf.agent_manager.invoke(aid) 


    await ptf.start()
    
    t_start = perf_counter_ns()
    asyncio.gather(*(_launch_agent(f"aget-{i}") for i in range(n)))
    t_stop = perf_counter_ns()
    
    await ptf.stop()

    print(f"Nb of agents: {n}; Elapsed time: {t_stop - t_start}ns")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("n", metavar="NB_OF_AGENTS", help="How many agents to launch", type=int)

    parsed = parser.parse_args()
    asyncio.run(main(parsed.n))