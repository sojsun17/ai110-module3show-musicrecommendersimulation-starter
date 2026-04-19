from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = int(row["tempo_bpm"])
            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Compute a recommendation score for one song against user preferences.

    Scoring recipe:
    - Add 2.0 points when song genre matches the favorite genre.
    - Add 1.0 point when song mood matches the favorite mood.
    - Add an energy closeness score using:
      1.0 - abs(target_energy - song_energy)

    Args:
        user_prefs: Preference dictionary containing at least
            "favorite_genre", "favorite_mood", and "target_energy".
        song: Song dictionary containing at least "genre", "mood", and
            "energy".

    Returns:
        A tuple (total_score, reasons) where total_score is a float and
        reasons is a list of human-readable scoring explanations.
    """
    total_score = 0.0
    reasons: List[str] = []

    if song["genre"] == user_prefs["favorite_genre"]:
        total_score += 2.0
        reasons.append("Genre match (+1.0)")

    if song["mood"] == user_prefs["favorite_mood"]:
        total_score += 1.0
        reasons.append("Mood match (+2.0)")

    energy_score = 1.0 - abs(user_prefs["target_energy"] - song["energy"])
    total_score += energy_score
    reasons.append(f"Energy match (+{energy_score:.2f})")

    return total_score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Score and rank songs against user preferences, then return the top-k.

    Each song is scored with score_song(user_prefs, song), transformed into
    a tuple of (song, score, explanation_string), sorted in descending score
    order, and truncated to at most k results.

    Args:
        user_prefs: Dictionary containing the user's preference fields used by
            score_song (favorite genre, mood, target energy, etc.).
        songs: List of song dictionaries loaded from the CSV.
        k: Maximum number of ranked recommendations to return.

    Returns:
        A list of tuples in the format (song_dict, score, explanation_string),
        ordered from highest score to lowest score.
    """
    scored_songs: List[Tuple[Dict, float, str]] = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored_songs.append((song, score, explanation))

    ranked_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return ranked_songs[:k]
