# HOW DO LAMBDA EXPRESSIONS MAKE CODE MORE CONCISE?
# Lambda expressions make code more concise by use less amount of
# lines for the same purpose that a 'for' loop. You should use
# lambda expressions on simple loops that doesn't require a many
# lines of code.

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return (lambda p: {"max_power": max(p), "min_power": min(p),
                       "avg_power": sum(p) / len(p)})([m["power"]
                                                       for m in mages])


def main() -> None:
    artifacts: list[dict] = [
        {
            "name": "Return Scepter",
            "power": 10,
            "type": "Staff"
        },
        {
            "name": "Narsil",
            "power": 90,
            "type": "Sword"
        },
        {
            "name": "Gold Clock",
            "power": 50,
            "type": "Clock"
        },
        {
            "name": "100 acre Book",
            "power": 30,
            "type": "Book"
        }
    ]
    mages: list[dict] = [
        {
            "name": "Rasmodius",
            "power": 70,
            "element": "Psychic"
        },
        {
            "name": "Gandalf",
            "power": 95,
            "element": "Light"
        },
        {
            "name": "Merlin",
            "power": 55,
            "element": "Water"
        },
        {
            "name": "Krobus",
            "power": 42,
            "element": "Darkness"
        }
    ]
    spells: list[str] = [
        "Word of Power",
        "Teleport",
        "Telekinesis",
        "Shadow Step"
    ]
    print("Testing artifact sorter...")
    print(artifact_sorter(artifacts))
    print("\nTesting power filter...")
    print(power_filter(mages, 60))
    print("\nTesting spell transformer...")
    print(spell_transformer(spells))
    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
