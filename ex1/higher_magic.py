# HOW DO HIGHER-ORDER FUNCTIONS ENABLE CODE REUSE AND COMPOSITION?
# Higher order functions enable code reuse by taking other functions
# as arguments or return new functions, implementing the same logic
# into multiple times.

# WHAT MAKES FUNCTIONS "FIRST-CLASS CITIZENS" IN PYTHON?
# Functions are "first-class citizens" because they are treated like
# any other value. You can assign them to a variable, use them as
# arguments, return other functions and save them in lists.

from collections.abc import Callable


def cure(target: str, power: int) -> str:
    return f"Cure restores {target} for {power} HP"


def fire(target: str, power: int) -> str:
    return f"Fire hits {target}, dealing {power} damage"


def is_powerful(power: int) -> bool:
    return power >= 50


def condition(target: str, power: int) -> bool:
    return "monster" == target.lower() and power >= 50


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combine(target: str, power: int) -> str:
        return (
                f"Combined spell result: {spell1(target, power)},"
                f" {spell2(target, power)}"
               )
    return combine


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplifier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplifier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def spell_creator(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return spell_creator


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


def main() -> None:
    combined_spell = spell_combiner(cure, fire)
    amplified_spell = power_amplifier(fire, 5)
    conditional = conditional_caster(condition, fire)
    sequence = spell_sequence([fire, cure])

    print("Testing spell combiner...")
    print(combined_spell("Luis", 30))
    print("\nTesting power amplifier...")
    print(amplified_spell("Luis", 50))
    print("\nTesting conditional caster...")
    print(conditional("Monster",  50))
    print("\nTesting spell sequence...")
    print(sequence("Luis", 50))


if __name__ == "__main__":
    main()
