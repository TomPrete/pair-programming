from pair import *
import random
import csv
import re



everyone = ['Jonathan Almoradie', 'Saumya Bajracharya', 'Val Gabriel', 'Beknazar Zhumabaev', 'Stephen Smith', 'Alexander Taylor', 'Pavel Bogdanov', 'Daniel Tolczyk', 'Justin Savage', 'Kenneth Malley', 'Jorge Silva', 'Bryan Gentz', 'Bryan Lubay', 'Ian Roberson', 'Sunny Noeun', 'Richard Maldonado', 'Kevin Maguire', 'Xuan Liu', 'Chase Cowart', 'Devin Winslow']

class Cohort:

  def __init__(self, name):
    self.name = name
    self.pairs = HashPair.get_pairs()
    self.new_pairs = []
    self.count = 0
    self.pair_programming = None
    self.student_hash_code = {}

  # Converts Cohort to a Hash with a Student Hash
  def convert_student_to_hash(self):
    hash = 7
    for student in everyone:
      new_student = student.lower().replace(' ', '')
      count = 0
      for char in student:
        hash = ord(char) * 7
        count += ord(char) * hash
      self.student_hash_code[student] = count + len(new_student)
    return self.student_hash_code

  # Randomly assigns Pairing partners
  def assign(self, arr):
    random.shuffle(arr)
    pairs = []
    final_pairings = []
    for student in arr:
      pairs.append(student)
      if len(pairs) == 2:
        final_pairings.append(Pair(pairs))
        pairs = []
    return final_pairings

  # Converts possible partners to hash
  def convert_possibilities_to_hash(self):
    new_pair_hash_arr = []
    for pair in self.pair_programming:
      pair_hash = self.student_hash_code[pair.pair[0]] + self.student_hash_code[pair.pair[1]]
      new_pair_hash_arr.append(pair_hash)
    return new_pair_hash_arr

  # Checks whether the randomly newly assigned parnters meet the minimum requirements (they haven't been partners 3 times already)
  def check_possibilities(self):
    self.pair_programming = self.assign(everyone)
    self.new_pair_posibilities_hash = self.convert_possibilities_to_hash()
    for pair_object in self.pairs:
      existing_hash = int(pair_object.hash_pair)
      for pair_possibility in self.new_pair_posibilities_hash:
        if existing_hash == int(pair_possibility):
          if int(pair_object.count) == 3:
            return self.check_possibilities()
    self.update_pairs()
    return self.pair_programming

  # Updates All Pairs with new Count of how many times they've been partners
  def update_pairs(self):
    if len(self.pairs):
      temp_pair_hash = None
      for pair_hash in self.new_pair_posibilities_hash:
        is_match = ''
        for pair in self.pairs:
          is_match = self.find_match_hash(pair_hash, pair.hash_pair)
          if is_match == True:
            self.pairs.remove(pair)
            pair.count += 1
            self.new_pairs.append(pair)
            break
        if is_match == False:
          temp_pair_hash = pair_hash
          is_match = ''
        if temp_pair_hash != None:
          new_pair_hash = HashPair(temp_pair_hash, 1)
          self.new_pairs.append(new_pair_hash)
          temp_pair_hash = None
    self.final_pairs = self.new_pairs + self.pairs
    self.print_pairs()
    return self.save_new_pairs()

  # Finds a match if they were already partners or not
  def find_match_hash(self, new_hash, existing_hash):
    new_hash = int(new_hash)
    existing_hash = int(existing_hash)
    if new_hash == existing_hash:
      return True
    else: return False

  # Saves Partners and How many times they've been partners
  def save_new_pairs(self):
    with open('pairs.csv', mode='w') as pair_csv:
      pair_writer = csv.writer(pair_csv)
      for pair in self.final_pairs:
        pair_writer.writerow([pair.hash_pair, pair.count])
    # pass

  # Prints Parnters
  def print_pairs(self):
    print('--------- PAIR PROGRAMMING PARTNERS ---------')
    for pair in self.pair_programming:
      print(f"{pair.pair[0]} & {pair.pair[1]}")

  # creates hash of already existing partners from already_partners array
  def get_existing_partners(self):
    hash_dict = {}
    for partner in already_partners:
      pair_hash = str(self.student_hash_code[partner[0]] + self.student_hash_code[partner[1]])
      if pair_hash in hash_dict:
        hash_dict[pair_hash] += 1
      else:
        hash_dict[pair_hash] = 1
    for hash in hash_dict:
      print(f"{hash},{hash_dict[hash]}")

kilo = Cohort('kilo')
kilo.convert_student_to_hash()
# kilo.get_existing_partners()
kilo.check_possibilities()
