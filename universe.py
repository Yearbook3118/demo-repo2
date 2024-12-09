import universe
universe.start()
universe.stars.append("Sun", "Sirius", "Alpha Centauri")
universe.stars[0].temp = 5000
universe.stars[0].planets.append("Earth")
universe.stars[0].planets[0].temperature = 288 # 15C
universe.stars[0].planets[0].add("Life")
universe.stars[0].planets[0].life.add("Animals", "Humans", "Water")
