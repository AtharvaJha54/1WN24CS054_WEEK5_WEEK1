import random

class VacuumCleanerAgent:
    def __init__(self, environment):
        self.environment = environment
        self.location = random.choice(list(environment.keys()))
        self.location_condition = self.environment[self.location]

    def sense(self):
        self.location_condition = self.environment[self.location]
        return self.location_condition

    def take_action(self, action):
        if action == "left":
            self.location = "A"
        elif action == "right":
            self.location = "B"
        elif action == "clean":
            self.environment[self.location] = 0

def simulate_environment():
    return {"A": random.randint(0, 1), "B": random.randint(0, 1)}

def main():
    environment = simulate_environment()
    agent = VacuumCleanerAgent(environment)
    
    for i in range(10):
        print(f"Current State: {environment}")
        print(f"Vacuum Cleaner position: {agent.location}")
        
        dirt_status = agent.sense()
        if dirt_status == 1:
            print("Vacuum Cleaner is sucking the Dirt")
            agent.take_action("clean")
        else:
            action = random.choice(["left", "right"])
            print(f"Vacuum Cleaner is moving {action}")
            agent.take_action(action)
        print("-" * 30)

if __name__ == "__main__":
    main()
