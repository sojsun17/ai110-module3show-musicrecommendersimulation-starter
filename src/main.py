"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    # user_prefs = {"favorite_genre": "pop", "favorite_mood": "happy", "target_energy": 0.8}
    ''' user_prefs = {
        "favorite_genre": "rock", 
        "favorite_mood": "sad", 
        "target_energy": 0.55
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)
    '''

    # Phase 4: Diverse User Profiles for Stress Testing
    profiles = [
        {
            "name": "Default Pop",
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.8
        },
        {
            "name": "Melancholic Rock",
            "favorite_genre": "rock",
            "favorite_mood": "sad",
            "target_energy": 0.55
        },
        {
            "name": "Chill Lofi",
            "favorite_genre": "lofi",
            "favorite_mood": "calm",
            "target_energy": 0.2
        },
        {
            "name": "Adversarial: The High-Energy Weeper",
            "favorite_genre": "pop",
            "favorite_mood": "sad",
            "target_energy": 0.95
        }
    ]

    for profile in profiles:
        print(f"\n--- Testing Profile: {profile['name']} ---")
        
        # 1. Get the recommendations for THIS profile
        recommendations = recommend_songs(profile, songs, k=5)
        
        # 2. PRINT THEM NOW (Must be indented!)
        for song, score, reasons in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {reasons}\n")



    '''
    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()
    '''

if __name__ == "__main__":
    main()
