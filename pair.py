import csv




class Pair:

  def __init__(self, pair):
    self.pair = pair


class HashPair:

  def __init__(self, hash_pair, count=1):
    self.hash_pair = hash_pair
    self.count = int(count)

  @classmethod
  def get_pairs(cls):
    add_pairs = []
    with open('pairs.csv', mode='r') as pairs_file:
      csv_reader = csv.reader(pairs_file)
      for row in csv_reader:
        if row:
          add_pairs.append(HashPair(row[0], row[1]))
    return add_pairs
