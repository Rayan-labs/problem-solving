# Jane Street — Hint Singles

September 2026 · Accepted submission

## Overview

A music-themed wordplay puzzle presented as a fictional compilation album. The solution connects altered song titles to artist names, extracts a hidden message, and applies the same rule once more to find the final answer.

The accepted answer matches [Jane Street’s published solution](https://www.janestreet.com/puzzles/hint-singles-solution/).

## Solution walkthrough

### 1. Identify the repeated change

The album title, “23 Hint Singles!”, resembles “23 Hit Singles!” with an extra **N**. This suggests looking for an added-letter pattern elsewhere in the puzzle.

The track list contains recognisable song titles with unusual additions or substitutions. These changes act as clues to altered versions of the original artists’ names.

For example, “Buddy Holly (After Running a 5k)” points to **Weezer**. Someone out of breath after running might be a **wheezer**. Inserting **H** into WEEZER produces WHEEZER.

This gives a rule to test: identify the original artist, insert one letter into their name, and check whether the resulting name fits the modified song title.

### 2. Apply the rule across the track list

The same construction works across all 23 tracks. Spaces and capitalisation are ignored when comparing the letters.

| # | Original artist | Modified name | Added letter | Connection to the clue |
|---|---|---|:---:|---|
| 1 | Weezer | Wheezer | H | Wheezing after a run |
| 2 | Spin Doctors | Spine Doctors | E | MISS: minimally invasive spine surgery |
| 3 | Bad Bunny | Bald Bunny | L | “Sin cabello” means without hair |
| 4 | Miley Cyrus | Miley Cyprus | P | Cyprus fits the geographical clue |
| 5 | Luke Combs | Luke Combos | O | Combos are filled pretzel snacks |
| 6 | State Champs | Statue Champs | U | A statue stands on a plinth |
| 7 | Johnny Cash | Johnny Crash | R | A fender bender is a crash |
| 8 | Foo Fighters | Food Fighters | D | Throwing pies suggests a food fight |
| 9 | Billy Joel | Billy Jor-El | R | Jor-El is Superman’s father, from Krypton |
| 10 | Men at Work | Menu at Work | U | A menu helps with ordering lunch |
| 11 | Chappell Roan | Chappell Roman | M | The title is rendered in Latin |
| 12 | Bob Dylan | Bomb Dylan | M | Trinitrotoluene is TNT |
| 13 | Fleetwood Mac | Fleetwood Mace | E | A mace is a club-like weapon |
| 14 | Big Thief | Brig Thief | R | A brig is a type of sailing vessel |
| 15 | Lana Del Rey | Lana Deli Rey | I | A deli sells sandwiches |
| 16 | Linkin Park | Linkin Spark | S | A spark can start a fire |
| 17 | Cardi B | Cardio B | O | HIIT is a form of exercise |
| 18 | Pet Shop Boys | Pet Shop Buoys | U | Buoys bob on water |
| 19 | David Bowie | David Bowtie | T | A bow tie is neckwear |
| 20 | The Cure | The Curse | S | A curse suggests bad luck |
| 21 | Erykah Badu | Erykah Baidu | I | Baidu fits the Hong Kong listing clue |
| 22 | Hanson | Chanson | C | “Chanson” is French for song |
| 23 | Mariah Carey | Mariah Car Key | K | A car key unlocks the Nissan Sentra |

### 3. Read the added letters in order

Keeping the album’s track order gives:

    HELPOURDRUMMERISOUTSICK

Adding spaces produces:

> HELP! OUR DRUMMER IS OUT SICK

This coherent message supports both the added-letter rule and the order of extraction. However, it is an instruction for one more step, rather than the final answer.

### 4. Treat the message as the bonus track

The extracted message has the same structure as the earlier clues:

> Help! (Our Drummer Is Out Sick)

“Help!” is a song by **The Beatles**. A band whose drummer is absent could be described as **beatless**.

Applying the same one-letter insertion rule gives:

    BEATLES → BEATLESS
                    + S

The final answer is **The Beatless**.

The introductory wording also supports this construction: the puzzle asks for a “brand” you have probably never heard before. BRAND itself is BAND with one extra letter.

### 5. Check the result

The proposed answer follows the same transformation used throughout the puzzle: a real artist’s name gains one letter, creating a name that matches the altered song clue.

The submission was accepted, and Jane Street’s subsequently published official solution confirms **The Beatless**.

## Accepted submission

Listed as **Rayan Labs** among the correct submissions for
Jane Street’s September 2026 puzzle, **Hint Singles**.

[View the original puzzle and correct-submissions list](https://www.janestreet.com/puzzles/hint-singles-index/#correct-submissions-from)

<img width="3456" height="1924" alt="4137C0C3-64D1-4CA7-A019-BE9E4AF4D491_1_201_a" src="https://github.com/user-attachments/assets/57fc45f4-65c9-4edd-bf36-0373a3f97809" />

## Python verification

The accompanying [`verify.py`](verify.py) script checks that each modified artist name is formed by inserting exactly one letter into the original name. It then extracts those letters in track order and verifies the hidden message.

Run it locally from this directory with:

```bash
python3 verify.py
