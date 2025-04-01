import charactor
def damage_calculator(attacker:charactor,defender:charactor)->int:
    """Calculates the damage dealt by the attacker to the defender."""
    damage = attacker.attack - defender.defense
    if damage < 0:
        damage = 0
    defender.hp -= damage
    if defender.hp <= 0:
        defender.alive = False
    else:
        defender.alive = True
    return damage