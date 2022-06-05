# Victor

A sassy trash-talking Codenames bot (trashing module under development) in the likeness of his future arch-nemesis [VictoriousChocobo](https://github.com/VictoriousChocobo). This is a WORK IN PROGRESS, but if you want to try the prototype:

### 0. Install [Anaconda](https://www.anaconda.com/products/individual).

### 1. Clone repository:

```sh
git clone https://github.com/da-cali/victor
cd victor
```

### 2. Create conda environment and install dependencies:

```sh
conda create -n victor python=3.9
conda activate victor
conda env update -f environment.yml
```

### 3. Run script.

```sh
python play.py
```

### Example game.

```
Loading model...

Please enter the codenames (separated by spaces).

Red agents:
bite poetry television dancing fugue japan mediterranean bag

Blue agents:
medical disrespectful toy lake purple wisdom smell eye

Bystanders:
lemon nugget destroyer tacky comic gorilla cheeseburger snow

Assasin:
guitar

---------- RED team turn ----------

RED spymaster:
Objective: ['dancing', 'fugue', 'poetry'] 
Clue: 'mazurka' for 3.

RED operatives:
Guess: fugue
✔️
Guess: dancing
✔️
Guess: poetry
✔️

---------- BLUE team turn ----------

BLUE spymaster:
Objective: ['purple', 'smell'] 
Clue: 'aroma' for 2.

BLUE operatives:
Guess: smell
✔️
Guess: lemon
✖️

---------- RED team turn ----------

RED spymaster:
Objective: ['japan', 'mediterranean'] 
Clue: 'greece' for 2.

RED operatives:
Guess: japan
✔️
Guess: mediterranean
✔️

---------- BLUE team turn ----------

BLUE spymaster:
Objective: ['lake'] 
Clue: 'river' for 1.

BLUE operatives:
Guess: lake
✔️

---------- RED team turn ----------

RED spymaster:
Objective: ['bag', 'bite'] 
Clue: 'wallet' for 2.

RED operatives:
Guess: bag
✔️
Guess: bite
✔️

---------- BLUE team turn ----------

BLUE spymaster:
Objective: ['purple'] 
Clue: 'pink' for 1.

BLUE operatives:
Guess: purple
✔️

---------- RED team turn ----------

RED spymaster:
Objective: ['television'] 
Clue: 'TV' for 1.

RED operatives:
Guess: television
✔️

Red team wins.
```

### Authors:
#### Concept: [VictoriousChocobo](https://github.com/VictoriousChocobo).
#### Implementation: [dacali](https://github.com/da-cali).