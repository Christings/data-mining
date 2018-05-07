# date:2017-10-19
# name:Lilly

from math import sqrt


# users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0,
#                       "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
#          "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5,
#                   "Vampire Weekend": 3.0},
#          "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5,
#                   "Slightly Stoopid": 1.0},
#          "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5,
#                  "The Strokes": 4.0, "Vampire Weekend": 2.0},
#          "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0,
#                     "Vampire Weekend": 1.0},
#          "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5,
#                     "The Strokes": 4.0, "Vampire Weekend": 4.0},
#          "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0,
#                  "Slightly Stoopid": 4.0, "The Strokes": 5.0},
#          "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5,
#                       "The Strokes": 3.0}
#          }

music = {"Dr Dog/Fate": {"piano": 2.5, "vocals": 4, "beat": 3.5, "blues": 3, "guitar": 5, "backup vocals": 4, "rap": 1},
         "Phoenix/Lisztomania": {"piano": 2, "vocals": 5, "beat": 5, "blues": 3, "guitar": 2, "backup vocals": 1,
                                 "rap": 1},
         "Heartless Bastards/Out at Sea": {"piano": 1, "vocals": 5, "beat": 4, "blues": 2, "guitar": 4,
                                           "backup vocals": 1, "rap": 1},
         "Todd Snider/Don't Tempt Me": {"piano": 4, "vocals": 5, "beat": 4, "blues": 4, "guitar": 1, "backup vocals": 5,
                                        "rap": 1},
         "The Black Keys/Magic Potion": {"piano": 1, "vocals": 4, "beat": 5, "blues": 3.5, "guitar": 5,
                                         "backup vocals": 1, "rap": 1},
         "Glee Cast/Jessie's Girl": {"piano": 1, "vocals": 5, "beat": 3.5, "blues": 3, "guitar": 4, "backup vocals": 5,
                                     "rap": 1},
         "La Roux/Bulletproof": {"piano": 5, "vocals": 5, "beat": 4, "blues": 2, "guitar": 1, "backup vocals": 1,
                                 "rap": 1},
         "Mike Posner": {"piano": 2.5, "vocals": 4, "beat": 4, "blues": 1, "guitar": 1, "backup vocals": 1, "rap": 1},
         "Black Eyed Peas/Rock That Body": {"piano": 2, "vocals": 5, "beat": 5, "blues": 1, "guitar": 2,
                                            "backup vocals": 2, "rap": 4},
         "Lady Gaga/Alejandro": {"piano": 1, "vocals": 5, "beat": 3, "blues": 2, "guitar": 1, "backup vocals": 2,
                                 "rap": 1}}

items = {"Dr Dog/Fate": [2.5, 4, 3.5, 3, 5, 4, 1],
         "Phoenix/Lisztomania": [2, 5, 5, 3, 2, 1, 1],
         "Heartless Bastards/Out at Sea": [1, 5, 4, 2, 4, 1, 1],
         "Todd Snider/Don't Tempt Me": [4, 5, 4, 4, 1, 5, 1],
         "The Black Keys/Magic Potion": [1, 4, 5, 3.5, 5, 1, 1],
         "Glee Cast/Jessie's Girl": [1, 5, 3.5, 3, 4, 5, 1],
         "La Roux/Bulletproof": [5, 5, 4, 2, 1, 1, 1],
         "Mike Posner": [2.5, 4, 4, 1, 1, 1, 1],
         "Black Eyed Peas/Rock That Body": [2, 5, 5, 1, 2, 2, 4],
         "Lady Gaga/Alejandro": [1, 5, 3, 2, 1, 2, 1]}
users = {
    "Angelica": {"Dr Dog/Fate": "L",
                 "Phoenix/Lisztomania": "L",
                 "Heartless Bastards/Out at Sea": "D",
                 "Todd Snider/Don't Tempt Me": "D",
                 "The Black Keys/Magic Potion": "D",
                 "Glee Cast/Jessie's Girl": "L",
                 "La Roux/Bulletproof": "D",
                 "Mike Posner": "D",
                 "Black Eyed Peas/Rock That Body": "D",
                 "Lady Gaga/Alejandro": "L"},
    "Bill": {"Dr Dog/Fate": "L",
             "Phoenix/Lisztomania": "L",
             "Heartless Bastards/Out at Sea": "L",
             "Todd Snider/Don't Tempt Me": "D",
             "The Black Keys/Magic Potion": "L",
             "Glee Cast/Jessie's Girl": "L",
             "La Roux/Bulletproof": "D",
             "Mike Posner": "D",
             "Black Eyed Peas/Rock That Body": "D",
             "Lady Gaga/Alejandro": "D"}



}


# 计算曼哈顿距离
def manhattan(vector1, vector2):
    """Computes the Manhattan distance. Both rating1 and rating2 are dictionaries
           of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    distance = 0
    total = 0
    n = len(vector1)
    for i in range(n):
        distance += abs(vector1[i] - vector2[i])
    return distance


# 寻找最近的用户
def computeNearestNeighbor(itemName, itemVector, items):
    """creates a sorted list of users based on their distance to item"""
    distances = []
    for otherItem in items:
        if otherItem != itemName:
            distance = manhattan(itemVector, items[otherItem])
            distances.append((distance, otherItem))
    # sort based on distance -- closest first
    distances.sort()
    return distances


# 分类函数
def classify(user, itemName, itemVector):
    """Give list of recommendations"""
    # first find nearest neighbor
    nearest = computeNearestNeighbor(itemName, itemVector, items)[0][1]
    print(nearest)
    # now find bands neighbor rated that user didn't
    rating = users[user][nearest]
    return rating

    # examples - uncomment to run


# recommend("Dr Dog/Fate", music)
r=classify("Angelica", "Cagle", [1, 5, 2.5, 1, 1, 5, 1])
print(r)
