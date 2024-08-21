class Environment:
    def __init__(self, size=2, agent_position=0, dirt_positions=None):
        self.size = size
        self.dirt_positions = dirt_positions if dirt_positions else [False] * size
        self.agent_position = agent_position
    
    def is_dirty(self, position):
        return self.dirt_positions[position]
    
    def clean(self, position):
        self.dirt_positions[position] = False
    
    def move_agent(self, new_position):
        if 0 <= new_position < self.size:
            self.agent_position = new_position
    
    def get_agent_position(self):
        return self.agent_position
    
    def is_clean(self):
        return all(not dirty for dirty in self.dirt_positions)

class Agent:
    def __init__(self, environment):
        self.environment = environment
        self.performance_score = 0
    
    def perceive(self):
        position = self.environment.get_agent_position()
        is_dirty = self.environment.is_dirty(position)
        return position, is_dirty
    
    def act(self, perception):
        position, is_dirty = perception
        if is_dirty:
            print("---> Dirt found, cleaning. :-]")
            self.environment.clean(position)
            self.performance_score += 1
        else:
            print("---> No dirt found, moving to other square. :-]")
            new_position = (position + 1) % self.environment.size
            self.environment.move_agent(new_position)
            self.performance_score -= 1

    def get_performance_score(self):
        return self.performance_score

def run_simulation(environment, agent, steps=10):
    for step in range(steps):
        print(f"Step {step + 1}: Position: {environment.get_agent_position()}, Dirt: {environment.dirt_positions[environment.get_agent_position()]}, Performance: {agent.get_performance_score()}")
        perception = agent.perceive()
        agent.act(perception)
        if environment.is_clean():
            print(f"Final performance score: {agent.get_performance_score()}")
            break
    return agent.get_performance_score()

potential_dirt_pos = [[True, True], [True, False], [False, True], [False, False]]
potential_agent_pos = [0, 1]
possibilities = 1
total_score = 0

for dirt_pos in potential_dirt_pos:
    for agent_pos in potential_agent_pos:
        print("\n")
        print(f"Run number: {possibilities} -- Starting position is {agent_pos}, dirt positions is {dirt_pos}.")
        environment = Environment(agent_position=agent_pos, dirt_positions=dirt_pos.copy())
        agent = Agent(environment)
        total_score += run_simulation(environment, agent, steps=10)
        possibilities += 1

print("\n")
print("------------------------------------------------")
average_score = total_score / (possibilities-1)
print(f"Here is the average score: {average_score}.")