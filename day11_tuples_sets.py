# Day 11 - Tuples and Sets

goalkeepers = (
    "Uğurcan Çakır",
    "Günay Güvenç",
    "Batuhan Şen"
)

defenders = (
    "Davinson Sánchez",
    "Abdülkerim Bardakcı",
    "Kaan Ayhan",
    "Eren Elmalı",
    "Ismail Jakobs",
    "Sacha Boey",
    "Wilfried Singo"
)

midfielders = (
    "Lucas Torreira",
    "Gabriel Sara",
    "Mario Lemina",
    "İlkay Gündoğan",
    "Yáser Asprilla"
)

forwards = (
    "Victor Osimhen",
    "Mauro Icardi",
    "Barış Alper Yılmaz",
    "Yunus Akgün",
    "Leroy Sané",
    "Roland Sallai",
    "Noa Lang"
)

print("=== GALATASARAY SQUAD ===")

print("\nGoalkeepers:")
for player in goalkeepers:
    print("-", player)

print("\nDefenders:")
for player in defenders:
    print("-", player)

print("\nMidfielders:")
for player in midfielders:
    print("-", player)

print("\nForwards:")
for player in forwards:
    print("-", player)

all_players = set(
    goalkeepers +
    defenders +
    midfielders +
    forwards
)

print(f"\nTotal unique players: {len(all_players)}")