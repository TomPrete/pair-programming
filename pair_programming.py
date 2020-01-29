import random
import csv

everyone = ['Jonathan Almoradie', 'Saumya Bajracharya', 'Val Gabriel', 'Beknazar Zhumabaev', 'Stephen Smith', 'Alexander Taylor', 'Pavel Bogdanov', 'Daniel Tolczyk', 'Justin Savage', 'Kenneth Mallay', 'Jorge Silva', 'Bryan Gentz', 'Bryan Lubay', 'Ian Roberson', 'Sunny Noeun', 'Richard Maldonado', 'Kevin Maguire', 'Xuan Liu', 'Chase Cowart', 'Devin Winslow']

def assign(arr):
  random.shuffle(arr)
  pairs = []
  final_pairings = []
  for student in arr:
    pairs.append(student)
    if len(pairs) == 2:
      final_pairings.append(pairs)
      pairs = []
  return final_pairings
