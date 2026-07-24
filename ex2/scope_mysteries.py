# HOW DO CLOSURES ENABLE FUNCTIONS TO "REMEMBER" THEIR CREATION ENVIRONMENT?
# Closures "remember" their creation environment by "remember" the reference
# (memory location) of the exterior function

# WHAT ARE THE BENEFITS OF LEXICAL SCOPING IN FUNCTIONAL PROGRAMMING?
# The lexical scoping in functional programming allow creation of private
# functions without the use of global variables.

from collections.abc import Callable


def mage_counter() -> Callable:
    count: int = 0

    def inner_count() -> int:
        nonlocal count
        count += 1
        return count
    return inner_count


def spell_acumulator(initial_power: int) -> Callable:
    amount: int = initial_power

    def accumulate(power: int) -> int:
        nonlocal amount
        amount += power
        return amount
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply_enchantment(item: str) -> str:
        return f"{enchantment_type} {item}"
    return apply_enchantment


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        memory[key] = value

    def recall(key: str) -> object:
        return memory.get(key, "Memory not found")
    return {"store": store, "recall": recall}


def main() -> None:
    counter1: Callable = mage_counter()
    counter2: Callable = mage_counter()
    accumulator: Callable = spell_acumulator(50)
    Flaming_enchantment: Callable = enchantment_factory("Flaming")
    Frozen_enchantment: Callable = enchantment_factory("Frozen")
    vault: dict[str, Callable] = memory_vault()

    print("Testing mage counter...")
    print(f"Counter 1: {counter1()}")
    print(f"Counter 1: {counter1()}")
    print(f"Counter 1: {counter1()}")
    print(f"Counter 2: {counter2()}")
    print(f"Counter 2: {counter2()}")
    print(f"Counter 2: {counter2()}")

    print("\nTesting spell accumulator...")
    print(f"Accumulator: {accumulator(50)}")
    print(f"Accumulator: {accumulator(100)}")
    print(f"Accumulator: {accumulator(150)}")

    print("\nTesting enchantment factory...")
    print(Flaming_enchantment("Sword"))
    print(Frozen_enchantment("Shield"))

    print("\nTesting memory vault...")
    print("Storing 'secret' = 42")
    vault["store"]("secret", 42)
    print("Recalling 'secret'")
    print(vault["recall"]("secret"))


if __name__ == "__main__":
    main()
