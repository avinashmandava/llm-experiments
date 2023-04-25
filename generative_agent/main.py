import json
from environment import Environment
from agent import Agent
from config import SIM_CLOCK_INCREMENT_MINUTES
from time import sleep
from datetime import datetime, timedelta

def main():

  sim_time = datetime(2023, 2, 1, 0, 0)

  print(f"Starting simulation at {sim_time}")
  # INSTANTIATE ENVIRONMENT AND AGENTS STATE
  environment = Environment(sim_time)
  print("Environment instantiated")
  agents = environment.agents
  print("Agents instantiated")
  # START SIMULATION CLOCK
  # Artificial counter for dev
  count = 0

  while count==0:
    for _,agent in agents.items():
      agent.sim_time = sim_time
      print(f"Generating observations for agent: {agent.name} at {agent.sim_time}")
      agent.observe()
      print(agent.name)
      print(agent.sim_time)
      print(agent.current_observations)
      print(agent.current_day_plan)
      print(agent.current_block_plan)
      print(agent.current_activity)

    # Save state
    state = environment.to_dict()
    state["sim_time"] = sim_time.strftime("%Y-%m-%d %H:%M:%S")
    environment.save_state(state)

    # Increment simulation clock
    sim_time += timedelta(minutes=SIM_CLOCK_INCREMENT_MINUTES)
    # Counter increment for dev
    count += 1

if __name__ == '__main__':
  main()