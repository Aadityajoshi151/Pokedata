## Pokedata

The purpose of this script is to use the [PokeApi]() to fetch Pokemon data and parse it in the format for a Jenga Card. It will help in automating the process of creating more cards in Adobe Photoshop.

Feel free to fork and modify the script in any way.


### Usage:
 - Clone the repo.
 - Move into the `src` folder.
 - Run the script using `python Pokedata.py` (Windows) or `python3 Pokedata.py` (Linux) and passing `--id` or `--range` flag.

 ### Sample:
**Input:**

 `python3 Pokedata.py --id 53`

**Ouput:**

```
#053 PERSIAN : NORMAL
HEIGHT: 1.0m WEIGHT: 32kg
ATTACKS: pay-day, scratch, cut, headbutt, bite, etc.
Although its fur has many admirers, it is to-
ugh to raise as a pet because of its fickle meanness.
```

**Input:**

 `python3 Pokedata.py --range 44-48`

**Ouput:**

```
#044 GLOOM : GRASS / POISON
HEIGHT: 0.8m WEIGHT: 8kg
ATTACKS: swords-dance, cut, headbutt, take-down, etc.
The fluid that oozes from its mouth isn't dr-
ool. It is a nectar that is used to attract prey.
==============================
#045 VILEPLUME : GRASS / POISON
HEIGHT: 1.2m WEIGHT: 18kg
ATTACKS: swords-dance, cut, headbutt, body-slam, etc.
It has the world’s largest petals. With ever-
y step, the petals shake out heavy clouds of toxic polle
==============================
#046 PARAS : BUG / GRASS
HEIGHT: 0.3m WEIGHT: 5kg
ATTACKS: scratch, swords-dance, cut, headbutt, etc.
Burrows to suck tree roots. The mushrooms on-
its back grow by draw­ ing nutrients from the bug host.
==============================
#047 PARASECT : BUG / GRASS
HEIGHT: 1.0m WEIGHT: 29kg
ATTACKS: scratch, swords-dance, cut, headbutt, etc.
A host-parasite pair in which the parasite m-
ushroom has taken over the host bug. Prefers damp places
==============================
#048 VENONAT : BUG / POISON
HEIGHT: 1.0m WEIGHT: 30kg
ATTACKS: headbutt, tackle, take-down, supersonic, etc.
Lives in the shadows of tall trees where it-
eats insects. It is attracted by light at night.
==============================
```