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
