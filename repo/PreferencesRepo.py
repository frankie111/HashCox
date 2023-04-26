import os.path
import pickle

from repo.Preferences import Preferences

prefs_file = "repo/Preferences.pickle"


def save(prefs: Preferences):
    with open(prefs_file, 'wb') as f:
        pickle.dump(prefs, f)


def load():
    preferences = Preferences()
    if os.path.getsize(prefs_file) > 0:
        with open(prefs_file, 'rb') as f:
            preferences = pickle.load(f)

    return preferences
