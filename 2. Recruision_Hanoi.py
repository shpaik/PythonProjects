# -*- coding: utf-8 -*-
print("\n----------------------------------- Hanoi")
#recruision
def move_disk(disk_num, start_peg, end_peg):
    print("Move %d stone from stick %d to stick %d" % (disk_num, start_peg, end_peg))

def hanoi(num_discs, start_peg, end_peg):
    # base case
    if num_discs == 0:
        return

    # recursive case
    other_peg = 6 - start_peg - end_peg
    # all stones except biggest stone to other peg
    hanoi(num_discs - 1, start_peg, other_peg)

    # biggest stone to end_peg
    move_disk(num_discs, start_peg, end_peg)

    # rest to end_peg
    hanoi(num_discs - 1, other_peg, end_peg)

# Test
hanoi(3, 1, 3)