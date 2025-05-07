class Superhero:
    def __init__(self, name, secret_identity, powers, weakness, origin_story):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers  # This should be a list
        self.weakness = weakness
        self.origin_story = origin_story
        self.energy_level = 100
        
    def use_power(self, power_index):
        if power_index < len(self.powers):
            power = self.powers[power_index]
            if self.energy_level >= 10:
                print(f"{self.name} uses {power}!")
                self.energy_level -= 10
                return True
            else:
                print(f"{self.name} is too tired to use {power}!")
                return False
        else:
            print("Invalid power selection!")
            return False
            
    def rest(self):
        print(f"{self.name} takes a well-deserved rest.")
        self.energy_level = min(100, self.energy_level + 30)
        
    def describe(self):
        print(f"Superhero Name: {self.name}")
        print(f"Secret Identity: {self.secret_identity}")
        print(f"Powers: {', '.join(self.powers)}")
        print(f"Weakness: {self.weakness}")
        print(f"Current Energy: {self.energy_level}%")
        
    def __str__(self):
        return f"{self.name} - {', '.join(self.powers[:2])}... (Energy: {self.energy_level}%)"

# Inheritance example
class CosmicHero(Superhero):
    def __init__(self, name, secret_identity, powers, weakness, origin_story, home_planet):
        super().__init__(name, secret_identity, powers, weakness, origin_story)
        self.home_planet = home_planet
        self.cosmic_energy = 200  # Cosmic heroes have more energy
        
    def use_power(self, power_index):
        # Cosmic heroes use powers more efficiently
        if power_index < len(self.powers):
            power = self.powers[power_index]
            if self.energy_level >= 5:  # Only costs 5 energy
                print(f"{self.name} channels cosmic energy to use {power}!")
                self.energy_level -= 5
                return True
            else:
                print(f"{self.name} needs to recharge cosmic energy!")
                return False
        else:
            print("Invalid power selection!")
            return False
            
    def cosmic_blast(self):
        if self.cosmic_energy >= 50:
            print(f"{self.name} unleashes a devastating cosmic blast!")
            self.cosmic_energy -= 50
            return True
        else:
            print("Not enough cosmic energy for a blast!")
            return False

# Example usage
if __name__ == "__main__":
    print("=== Superhero Class Demonstration ===")
    spiderman = Superhero(
        name="Spider-Man",
        secret_identity="Peter Parker",
        powers=["Web-slinging", "Spider-sense", "Wall-crawling", "Super strength"],
        weakness="Ethyl chloride (his web solvent)",
        origin_story="Bitten by a radioactive spider"
    )
    
    silver_surfer = CosmicHero(
        name="Silver Surfer",
        secret_identity="Norrin Radd",
        powers=["Cosmic Power", "Flight", "Energy Manipulation", "Interstellar Travel"],
        weakness="Galactus' influence",
        origin_story="Former herald of Galactus",
        home_planet="Zenn-La"
    )
    
    # Demonstrate methods
    spiderman.describe()
    spiderman.use_power(0)  # Web-slinging
    spiderman.use_power(1)  # Spider-sense
    print(spiderman)
    
    silver_surfer.describe()
    silver_surfer.use_power(0)  # Cosmic Power
    silver_surfer.cosmic_blast()
    print(silver_surfer)
