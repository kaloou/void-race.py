import random, time, gaming_tools

print("Lancer la fonction set_the_game pour lancer le jeu Shootins Stars!")
gaming_tools.reset_game()

#----------SET THE GAME--------------#
def set_the_game():
    if gaming_tools.planet_exists(planet="Epsilon Aurigae"):
        print("Une planète avec ce nom existe déjà.")
    if gaming_tools.planet_exists(planet="Aldebaran"):
        print("Une planète avec ce nom existe déjà.")
    
    gaming_tools.add_new_planet(planet="Epsilon Aurigae", resources=0)
    gaming_tools.set_planet_location(planet="Epsilon Aurigae", coord_x=1000, coord_y=1000)

    gaming_tools.add_new_planet(planet="Aldebaran", resources=0)
    gaming_tools.set_planet_location(planet="Aldebaran", coord_x=0, coord_y=0)

    print("\n*-*-*-*-*-*-*-**-*-*-*-*-*-*-*BIENVENUE DANS SHOOTING STARS*-*-*-*-*-*-*-**-*-*-*-*-*-*-*\n")
    print("-------------------------------------------------------------\n")
    print("Dans ce jeu, vous incarnerez un capitaine de vaisseau spatial chargé d'explorer l'univers infini.\nVotre mission : découvrir de nouvelles planètes, améliorer votre vaisseau, et atteindre la planète Epsilon Aurigae en un seul morceau.\nRappel : ce n'est pas un jeu collectif, mais une compétition pour le voyage le plus rapide !\n")
    print("-------------------------------------------------------------\n")
    print(" Règles du Jeu :\n")
    print("-------------------------------------------------------------\n")
    print(" 1. Préparation du Voyage :\nDéfinissez un ordre de passage avant de commencer votre aventure intergalactique.Qui sera le premier à s'envoler vers l'inconnu ?\nCréez votre propre vaisseau spatial en lui donnant un nom. Votre vaisseau sera votre compagnon fidèle tout au long de votre voyage.\nCréer et explorer différentes planètes pour collecter des ressources essentielles pour votre voyage. Les ressources seront nécessaires\npour les réparations et les améliorations de votre vaisseau.\n")
    print(" 2. La Course à la Planète Epsilon :\nVotre objectif ultime est d'atteindre la planète Epsilon Aurigae. C'est une compétition avec d'autres capitaines.\nSoyez le premier à y arriver !Investissez dans l'amélioration de la vitesse de votre vaisseau pour atteindre des destinations plus rapidement.\nSoyez stratégique dans vos décisions pour maximiser votre exploration intergalactique.\n")
    print(" 3. Gérer les Péripéties de l'Espace : \nMéfiez-vous des défis imprévus de l'espace, tels que les pannes et les obstacles. Soyez prêt à résoudre les problèmes en cours de route.\nEn cas de panne de votre vaisseau, utilisez les ressources des planètes pour effectuer des réparations et éviter d'être coincé dans l'espace.\nGérez le temps avec sagesse pour ne pas être distancé par vos concurrents.")
    print("-------------------------------------------------------------\n")
    print("Voici les différentes fonctions que vous pouvez utiliser pour jouer:\nCréer son vaisseau ----> create_ship(nom du vaisseau)\nCréer une planète ----> create_planet(nom de la planète, coord_x, coord_y)\nDéplacer son vaisseau vers une autre planète ----> move_ship(nom du vaisseau, nom de la planète de destination)\nRéparer son vaisseau ----> repair_ship(nom du vaisseau)\nAméliorer la vitesse de son vaisseau ----> improve_ship_speed(nom du vaisseau)\nAfficher le statut du vaisseau ----> get_ship_info(nom du vaisseau)\n")

#----------PLANET FUNCNTIONS----------#

def create_planet(planet_name, coord_x, coord_y):
    """
    Creates a new planet with a given name, random resources, and coordinates (x, y).
    Ensures the planet name is unique.

    Parameters:
    planet_name (str): The name of the planet to create.
    coord_x (int): The x-coordinate of the planet.
    coord_y (int): The y-coordinate of the planet.

    Returns:
    The confirmation that the planet has been correctly created 

    Raises:
    ValueError: If a planet with the same name already exists.
    """

    if gaming_tools.planet_exists(planet_name):
        print("Une planète avec le nom %s existe déjà." % planet_name)
    
    resources = random.randint(5, 20)
    
    gaming_tools.add_new_planet(planet_name, resources)
    gaming_tools.set_planet_location(planet_name, coord_x , coord_y)

    print("La planète a bien été créée ! Elle s'appelle %s et est placée en (%d, %d)" % (planet_name, coord_x, coord_y))

#----------SHIP FUNCNTIONS----------#

def create_ship(name):
    """
    Creates a ship with a given name. The ship has an initial speed of 1 parsec per second and is not broken.

    Parameters:
    name (str): The name of the ship to create.

    Returns:
    The confirmation that the ship has been correctly created 

    Raises:
    ValueError: If a ship with the same name already exists.

    """
    if gaming_tools.ship_exists(name):
        print("Un vaisseau avec le nom %s existe déjà." % name)
    
    gaming_tools.add_new_ship(name, speed=1, broken=False)
    gaming_tools.set_ship_location(name, "Aldebaran")
    planet_a= gaming_tools.get_ship_location(name)
    
    print("Votre vaisseau a été créé ! Il s'appelle %s et se trouve actuellement sur la planète %s en (0,0)" % (name,planet_a))

    # -----------------------------------------------

def move_ship(ship_name, destination_planet):
    """
    Moves a ship from its current planet to another planet. Calculates the jump duration based on the ship's speed and the distance between planets.
    Updates the ship's position and the time it will be ready for another action.

    Parameters:
    ship_name (str): The name of the ship to move.
    destination_planet (str): The name of the destination planet.

    Returns:
    str: A message indicating the result of the movement or action.

    Raises:
    ValueError: If the ship or destination planet does not exist.

    Notes:
    - If the ship breaks down during the jump, it must be repaired.
    - If the ship arrives at the Epsilon Aurigae planet, the player wins.

    """
    if not gaming_tools.ship_exists(ship_name):
        print("Le vaisseau avec le nom %s n'existe pas." % ship_name)
    
    if not gaming_tools.planet_exists(destination_planet):
        print("La planète de destination nommée %s n'existe pas." % destination_planet)
    
    if gaming_tools.is_ship_broken(ship_name):
        print("Le vaisseau '%s' est en panne et ne peut pas se déplacer." % ship_name)
    
    current_planet = gaming_tools.get_ship_location(ship_name)
    current_x, current_y = gaming_tools.get_planet_location(current_planet)
    dest_x, dest_y = gaming_tools.get_planet_location(destination_planet)
    
    distance = ((dest_x - current_x) ** 2 + (dest_y - current_y) ** 2) ** 0.5
    speed = gaming_tools.get_ship_speed(ship_name)
    
    time_needed = distance / speed
    a=1

    coord=gaming_tools.get_ship_location(ship_name)
    start_time = time.time()
    gaming_tools.set_when_ship_is_ready(ship_name, start_time + time_needed) 

    if coord == "Epsilon Aurigae" and a==1: 
        print("Le vaisseau %s se dirige vers la planète Epsilon Aurigae\." % (ship_name,time_needed))
        a= a+1
    if coord =="Epsilon Aurigae" and a >1:
        print("Le vaisseau %s à gagné la course" % ship_name)    
    
    else:    
        if time_needed > 0:

            if random.randint(1, 3) == 3:
                gaming_tools.set_ship_broken(ship_name, True)
                gaming_tools.set_ship_location(ship_name, destination_planet)
                gaming_tools.set_when_ship_is_ready(ship_name, start_time + time_needed)  
                print("Le vaisseau est tombé en panne à l'arrivée de la planète. Veuillez le réparer")
            
            gaming_tools.set_when_ship_is_ready(ship_name, start_time + time_needed)
            gaming_tools.set_ship_location(ship_name, destination_planet)
            print("Le vaisseau se déplace vers %s. Temps estimé : %f secondes." % (destination_planet, time_needed))
        else:
            print("Le vaisseau est déjà sur la planète %s." % destination_planet)

    # ----------------------------------------

def repair_ship(ship_name):
    """
    Repairs a ship if it is broken. It consumes resources from the planet for the repair.
    Updates the ship's status and the time it will be ready for another action.

    Parameters:
    ship_name (str): The name of the ship to repair.

    Returns:
    str: A message indicating the result of the repair.

    Raises:
    ValueError: If the ship does not exist or the planet lacks sufficient resources for repair.

    """
    
    if not gaming_tools.ship_exists(ship_name):
        print("Le vaisseau '%s' n'existe pas." % ship_name)
    
    if not gaming_tools.is_ship_broken(ship_name):
        print("Le vaisseau '%s' n'est pas en panne et ne nécessite pas de réparation." % ship_name)
    
    current_planet = gaming_tools.get_ship_location(ship_name)
    planet_resources = gaming_tools.get_planet_resources(current_planet)
    
    repair_cost = 3
    repair_time = 20 * (gaming_tools.get_ship_speed(ship_name))
    
    if planet_resources >= repair_cost:
        gaming_tools.set_when_ship_is_ready(ship_name, repair_time)
        gaming_tools.set_ship_broken(ship_name, False)
        gaming_tools.set_planet_resources(current_planet, planet_resources - repair_cost)
        print("Le vaisseau %s sera réparé avec succès dans exactement %d secondes." % (ship_name,repair_time))
    else:
        print("La planète %s n'a pas suffisamment de ressources pour réparer le vaisseau." % current_planet)

    # ------------------------------------------

def improve_ship_speed(ship_name):
    """
    Improves a ship's speed by spending planet resources. Calculates the required time based on the speed difference.
    Updates the ship's speed and the time it will be ready for another action.

    Parameters:
    ship_name (str): The name of the ship to improve.

    Returns:
    str: A message indicating the result of the improvement.

    Raises:
    ValueError: If the ship does not exist or the planet lacks sufficient resources for improvement.

    """
 
    if not gaming_tools.ship_exists(ship_name):
        print("Le vaisseau %s n'existe pas." % ship_name)
    
    current_planet = gaming_tools.get_ship_location(ship_name)
    planet_resources = gaming_tools.get_planet_resources(current_planet)
    improvement_cost = 1

    if planet_resources < improvement_cost:
        print("La planète %s n'a pas suffisamment de ressources pour améliorer la vitesse du vaisseau." % current_planet)

    new_speed = gaming_tools.get_ship_speed(ship_name) + 1
    improvement_time = 40 * ((new_speed ** 2) - (gaming_tools.get_ship_speed(ship_name) ** 2))

    if planet_resources >= improvement_cost:
        new_speed = gaming_tools.get_ship_speed(ship_name) + 1
        gaming_tools.set_when_ship_is_ready(ship_name, improvement_time)
        gaming_tools.set_ship_speed(ship_name, new_speed)
        gaming_tools.set_planet_resources(current_planet, planet_resources - improvement_cost)
        print("La vitesse du vaisseau %s sera améliorée à %d parsec/seconde dans exactement %d secondes." % (ship_name, new_speed,improvement_time))

def get_ship_info(ship_name):
    """
    Returns information about the ship's current state, including its name, speed, breakdown status, and the time it will be ready for another action.

    Parameters:
    ship_name (str): The name of the ship for which to obtain information.

    Returns:
    str: A message containing information about the ship.

    Raises:
    ValueError: If the ship does not exist.

    """
    if not gaming_tools.ship_exists(ship_name):
        print("Le vaisseau %s n'existe pas." %(ship_name))
    
    speed = gaming_tools.get_ship_speed(ship_name)
    broken = gaming_tools.is_ship_broken(ship_name)
    current_planet=gaming_tools.get_ship_location(ship_name)
    
    print("Nom du vaisseau : %s \nVitesse : %d parsec/seconde\nEn panne : %s \nPlanete acutelle du vaisseau : %s" % (ship_name, speed, broken, current_planet))
