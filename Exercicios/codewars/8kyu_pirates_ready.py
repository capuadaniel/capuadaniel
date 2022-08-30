def cannons_ready(gunners):
    # Fire! or Shiver me timbers!
    cancel = 0
    for k, v in gunners.items():
        if v == "nay":
            cancel += 1

    if cancel == 0:
        return ("Fire!")
    else:
        return ("Shiver me timbers!")

a = {'Mike': 'aye', 'Joe': 'aye', 'Johnson': 'aye', 'Peter': 'aye'}
b = {'Mike': 'aye', 'Joe': 'nay', 'Johnson': 'aye', 'Peter': 'aye'}
print(cannons_ready(a), 'Fire!')
print(cannons_ready(b), 'Shiver me timbers!')