# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

My version of the recommender system uses a weighted content-based filtering approach, where each song is treated as a set of attributes and compared against a user’s personalized “Vibe Profile.” Each song is described by its genre and mood, which are categorical features, as well as its energy level, which is a numerical value between 0.0 and 1.0. The user profile stores their ideal preferences for these same attributes, allowing the system to measure how well each song aligns with what they’re looking for. The scoring logic prioritizes genre as the strongest signal, awarding +2.0 points for a match, followed by mood with +1.0 point. Energy is handled differently, using a linear decay formula (1.0 − |UserEnergy − SongEnergy|) to reward songs that are closest to the user’s desired energy level rather than simply favoring high or low values. After calculating a total score for every song in the dataset, the system sorts all songs from highest to lowest score and returns the top K recommendations.

Song Features: title, genre, mood, energy (float).

UserProfile Features: fav_genre, fav_mood, target_energy (float).


My current plan:
My version of the recommender uses a Weighted Content-Based Filtering approach. It treats every song as a collection of data points and compares them against a user's specific "Vibe Profile."

Data Features
Song Features: title, genre, mood, energy (0.0–1.0).

UserProfile: favorite_genre, favorite_mood, target_energy.

System Architecture & Logic
The following flowchart visualizes how a single user profile is compared against the entire song catalog to produce a ranked list:

![System Workflow](images/workflow_diagram.png)

The Algorithm Recipe
Genre Anchor (+2.0): If the song genre matches the user's preference, it receives a heavy bonus. This ensures the recommendation stays within the user's preferred style.

Mood Modifier (+1.0): If the mood matches, a secondary bonus is applied to refine the "feeling" of the recommendation.

Energy Proximity (Up to +1.0): Calculated as 1.0 - abs(user_energy - song_energy). This rewards songs that are closer to the user's target intensity.

Final Ranking: All scores are summed (max 4.0), and the system sorts the songs to return the Top K results.

Potential Biases
Genre Over-Prioritization: Because Genre is worth twice as much as Mood, the system may ignore a perfectly "Sad" song if it belongs to a different genre, potentially creating a "Genre Filter Bubble."

Small Catalog Limitation: With only 20 songs, the system might struggle to find a "perfect" match, leading to recommendations that only meet one of the three criteria.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

When I shifted the algorithm's focus, the system’s behavior changed from being a rigid "Genre-First" filter to a more fluid "Vibe-First" recommender. Reducing the genre weight from 2.0 to 0.5 caused the system to stop gatekeeping by category; instead of only seeing Rock songs for my "Melancholic Rock" profile, the system began suggesting "Sad" songs from any genre that hit the target energy of 0.55. When experimenting with technical features like tempo, the results became even more granular, though it risked over-complicating the "vibe" by penalizing great songs just for being a few BPM off. Across different users, the system proved highly adaptive: it successfully isolated "Library Rain" for the Chill Lofi fan and "Black Hole Sun" for the Rock fan, but the "Adversarial" test revealed a key bias—if energy is weighted too heavily, the system completely ignores the user's emotional "Mood" preference in favor of raw intensity.

**Baseline Pop Results:**
![Baseline Results](images/baseline_test.png)

**Custom Melancholic Rock Results:**
![Rock Results](images/melancholic_rock_results.png)

**Diverse Profiles Batch Test:**
![Multiple Profiles](images/multiple_profiles_test.png)
---

## Limitations and Risks


The primary limitation of this recommender is its heavy reliance on manual tagging, meaning if a song is mislabeled in the CSV, it effectively disappears from relevant searches. Because the system lacks natural language processing, it has no understanding of lyrics or cultural context; it cannot tell the difference between a song that is "Sad" because of its melody and one that is "Sad" because of its story. Furthermore, the small catalog of only 20 tracks creates a diversity bottleneck, where the same "perfect matches" like Black Hole Sun will always dominate the top results, creating a "Filter Bubble" that prevents users from discovering new genres. Finally, the linear energy math is a blunt instrument that treats all energy gaps equally, failing to account for how human ears perceive the difference between "chill" and "intense" music across different styles.
![Adversarial Bias Test](images/adversarial_test.png)
---



## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

Building this simulation made me realize that recommendation systems are basically just taking someone’s “vibe” and turning it into numbers. Every song gets broken down into features, and then the system just compares those to what the user wants. What actually matters is the “algorithm recipe” like how much weight I give to genre vs. mood vs. energy because that completely changes what gets recommended. The system isn’t actually understanding the music at all, it’s just doing math and picking whatever is closest to the user’s preferences.

I also started to see how bias naturally shows up depending on how those weights are set. For example, since I weighted genre more heavily, the system would sometimes pick a song in the “right” genre even if the mood didn’t match what the user asked for. That kind of creates a filter bubble, where certain songs or even whole genres get pushed out just because of how I designed the scoring. When I tested edge cases, it became clear that if you prioritize things like energy over mood, the system can completely miss the point and recommend something that technically fits the numbers but feels totally off. It made me realize how easy it is for the actual human intent to get lost just because of how the math is set up.

---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeRank v1.0**  

---

## 2. Intended Use  

This is a classroom simulation built to show how content-based filtering actually works under the hood. It recommends a ranked list of 5 songs from a small dataset based on a user’s genre, mood, and energy preferences. It assumes the user has a fixed “vibe profile,” so it’s not meant for real-world or production use, just learning how recommender systems think.

---

## 3. How the Model Works  

This model basically acts like a “vibe matcher” that turns music into numbers and compares them to what the user wants.

Each song has three features: genre, mood, and energy. The system then scores each song based on how close it is to the user’s preferences.

Genre match gets the biggest boost (+2.0) since it’s treated as the strongest signal.
Mood match adds a smaller boost (+1.0).
Energy is handled by checking how close the song’s energy is to the user’s target using a simple distance formula, so closer = better.

I also added explanation text for each recommendation so it’s not just a black box—you can actually see why a song was picked (like “Genre match +2.0”).

---

## 4. Data  

The dataset has about 15–20 songs stored in a CSV file. It started off pretty basic (pop, lofi, etc.), but I added more variety like melancholic rock tracks (Radiohead, Soundgarden, etc.) to make it more interesting.

That said, the data is still pretty Western/mainstream-heavy and doesn’t really capture deeper things like lyrics, subgenres, or musical complexity so it’s still kind of a simplified version of real music taste.

---

## 5. Strengths  

The model works really well when the user’s preferences line up with what’s in the dataset. For example, when I tested a melancholic rock profile, it actually pulled really accurate “sad rock” songs at the top. So within a specific vibe, it does a solid job of locking in and finding matches.

---

## 6. Limitations and Bias 

One big issue is “label bias.” Since genre is weighted the most, the model will sometimes choose the “right genre” over the “right mood,” even when that doesn’t really match what the user asked for.

It also has a diversity problem because the dataset is small so the same songs keep showing up over and over again.

On top of that, it completely ignores emotional or cultural context. For example, it treats a song like Hurt by Johnny Cash as just numbers, not something emotionally heavy. So small numerical differences can outweigh actual human meaning.

---

## 7. Evaluation  

I tested it using four profiles: Default Pop, Melancholic Rock, Chill Lofi, and an adversarial high-energy “weeper” profile. I mainly looked at how the top results changed when I adjusted weights.

What stood out was how sensitive the system is when I increased the energy weight, it basically stopped caring about mood and started recommending high-energy “gym” type songs instead of sad ones. It made it really clear how much the results depend on the math setup.

---

## 8. Future Work  

If I had more time, I’d improve it by:

Adding a “serendipity” factor so users don’t get stuck in the same vibe loop
Using acoustic features like acousticness to better separate instrumental vs. electronic tracks
Improving explanations so it can say things like “this is similar to your favorite artist” instead of just raw score breakdowns

---

## 9. Personal Reflection  

This project made it clear that recommendation systems aren’t actually “understanding” music, they’re just doing fast math on patterns. What surprised me most is how easy it is to accidentally introduce bias just by tweaking a weight slightly. Something like changing 1.5 to 2.0 can completely shift what the system thinks is “good.”

It honestly changed how I look at apps like Spotify, because now I realize the reason I sometimes get stuck in the same type of songs is probably because the system is optimizing for numbers, not vibes.
