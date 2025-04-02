import charactor
class base_damage_calculator:
    ...
def damage_calculator(attacker:charactor,defender:charactor)->int:
    """Calculates the damage dealt by the attacker to the defender."""
    damage = attacker.attack - defender.defense
    if damage < 0:
        damage = 0
    defender.hp -= damage
    return damage