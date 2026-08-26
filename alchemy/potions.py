import elements

def healing_potion() -> str:
    return ("Healing potion brewed with "
    f"’{elements.create_earth()}’ and ’{elements.create_air()}")

def strength_potion() -> str:
    return  ("Strength potion brewed with "
    f"’{create_fire()}’ and ’{create_water()}")
if __name__ == "__main__":
    print(healing_potion())
    print(strength_potion())