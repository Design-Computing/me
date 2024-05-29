"""Play around it this file, see if it does what you think it'll do."""

bucket = []
other_bucket = [6, "5", 4, 3, 2, 1, "💅"]
for value in other_bucket:
    bucket.append(value * 3)

print(bucket)

import random

guard = 0


def hat():
    for i in range(random.randrange(1, 5)):
        print("🎩")


while True and guard < 500:
    print("snare 🥁")
    hat()
    guard += 1

is_it = "format "
print("{is_it : ^20}normal string")
print(f"{is_it : ^20}string")
