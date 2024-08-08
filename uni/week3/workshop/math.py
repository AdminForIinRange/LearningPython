import math

class Planet:
    def __init__(self, name, mass, diameter, density, gravity, distance_from_sun, mean_temperature, moon_count, ring_system, global_magnetic_field):
        self.name = name
        self.mass = mass
        self.diameter = diameter
        self.density = density
        self.gravity = gravity
        self.distance_from_sun = distance_from_sun
        self.mean_temperature = mean_temperature
        self.moon_count = moon_count
        self.ring_system = ring_system
        self.global_magnetic_field = global_magnetic_field

    def calculate_radius(self):
        return self.diameter / 2

    def calculate_surface_area(self):
        radius = self.calculate_radius()
        return 4 * math.pi * radius ** 2

    def calculate_mass(self, weight):
        return weight * self.gravity

    def calculate_weight(self, weight):
        return weight * (self.gravity / 9.8)

    def __str__(self):
        moons_description = (
            "no moons" if self.moon_count == 0 else
            "a single moon" if self.moon_count == 1 else
            f"many moons ({self.moon_count})"
        )
        return (
            f"Planet Name: {self.name}\n"
            f"Mass: {self.mass} kg\n"
            f"Distance from Sun: {self.distance_from_sun} km\n"
            f"Moons: {moons_description}\n"
            f"Has Global Magnetic Field: {'Yes' if self.global_magnetic_field else 'No'}\n"
            f"Has Ring System: {'Yes' if self.ring_system else 'No'}"
        )

class SolarSystem:
    def __init__(self):
        self.planets = []

    def add_planet(self, planet):
        valid_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        if planet.name in valid_planets:
            self.planets.append(planet)
        else:
            print(f"Invalid planet: {planet.name} is not a valid planet in this solar system.")

    def remove_planet(self, planet):
        if planet in self.planets:
            self.planets.remove(planet)
        else:
            print(f"Planet {planet.name} is not in the solar system.")

    def __str__(self):
        return "\n".join([str(planet) for planet in self.planets])

# Example usage:

earth = Planet(
    name="Earth",
    mass=5.972e24,
    diameter=12742,
    density=5.51,
    gravity=9.8,
    distance_from_sun=149.6e6,
    mean_temperature=15,
    moon_count=1,
    ring_system=False,
    global_magnetic_field=True
)

solar_system = SolarSystem()
solar_system.add_planet(earth)

print(solar_system)
