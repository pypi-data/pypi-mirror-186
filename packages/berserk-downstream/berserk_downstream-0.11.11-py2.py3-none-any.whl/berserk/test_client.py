import berserk
from datetime import datetime

LICHESS_TOKEN = 'pq2djZpS9tI9QZZ4'  # OAuth token for Lichess API access
session = berserk.TokenSession(LICHESS_TOKEN)
lichess = berserk.Client(session=session)

#temp = lichess.broadcasts.create("test", "testing berserk broadcast API")

#temp = lichess.broadcasts.create_round("s2ZsPYib","Round One")
temp = lichess.broadcasts.update_round("2VbflR6w", "Round Not One")

