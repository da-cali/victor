# Victor

A sassy trash-talking Codenames bot (under development) in the likeness of his future arch-nemesis [VictoriousChocobo](https://github.com/VictoriousChocobo). This is a WORK IN PROGRESS, but if you want to try the prototype:

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
Red agents' codenames:
bite poetry television dancing fugue japan mediterranean bag

Blue agents' codename:
medical disrespectful toy lake purple wisdom smell eye 

Bystanders' codenames:
lemon nugget destroyer tacky comic gorilla cheeseburger snow

Assasin codename:
black

---------- Red team turn. ----------

Red spymaster:
Objective: 
['dancing', 'fugue', 'poetry'] 
Clue:
 poems

Red operatives:
Guess: poetry
Correct guess.
Guess: fugue
Correct guess.
Guess: comic
Incorrect guess. End of turn.

---------- Blue team turn. ----------

Blue spymaster:
Objective: 
['purple', 'smell'] 
Clue:
 aroma

Blue operatives:
Guess: smell
Correct guess.
Guess: lemon
Incorrect guess. End of turn.

---------- Red team turn. ----------

Red spymaster:
Objective: 
['japan', 'mediterranean'] 
Clue:
 europe

Red operatives:
Guess: japan
Correct guess.
Guess: mediterranean
Correct guess.

---------- Blue team turn. ----------

Blue spymaster:
Objective: 
['lake'] 
Clue:
 river

Blue operatives:
Guess: lake
Correct guess.

---------- Red team turn. ----------

Red spymaster:
Objective: 
['bag', 'bite'] 
Clue:
 wallet

Red operatives:
Guess: bag
Correct guess.
Guess: bite
Correct guess.

---------- Blue team turn. ----------

Blue spymaster:
Objective: 
['purple'] 
Clue:
 pink

Blue operatives:
Guess: purple
Correct guess.

---------- Red team turn. ----------

Red spymaster:
Objective: 
['television'] 
Clue:
 TV

Red operatives:
Guess: television
Correct guess.

---------- Blue team turn. ----------

Blue spymaster:
Objective: 
['disrespectful'] 
Clue:
 insulting

Blue operatives:
Guess: disrespectful
Correct guess.

---------- Red team turn. ----------

Red spymaster:
Objective: 
['dancing'] 
Clue:
 dancers

Red operatives:
Guess: dancing
Correct guess.
Red team wins.
```

### Authors:
#### Concept: [VictoriousChocobo](https://github.com/VictoriousChocobo).
#### Implementation: [dacali](https://github.com/da-cali).