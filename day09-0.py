marbles = [0, 2, 1]
cur_pos = 1

player_ct = 426
player_scores = [0] * player_ct
high_marble = 72058

for m in range(3, high_marble + 1):
    cur_player = m % player_ct
    if m % 23 == 0:
        cur_pos -= 7
        if cur_pos < 0:
            cur_pos %= len(marbles)
        rem_val = marbles.pop(cur_pos)
        player_scores[cur_player] += (m + rem_val)
    else:
        cur_pos = cur_pos + 2
        if cur_pos > len(marbles):
            cur_pos %= len(marbles)
        marbles.insert(cur_pos, m)

print(max(player_scores))


class Node:
    def __init__(self, value):
        self.value = value
        self.cw = self
        self.ccw = self

    def insert_cw(self, value):
        new_node = Node(value)
        self.cw.ccw = new_node
        new_node.cw = self.cw
        new_node.ccw = self
        self.cw = new_node
        return new_node

    def remove(self):
        self.ccw.cw = self.cw
        self.cw.ccw = self.ccw
        return self.cw


player_ct = 426
player_scores = [0] * player_ct
high_marble = 7205800

cur_pos = Node(0)

for m in range(1, high_marble + 1):
    cur_player = m % player_ct
    if m % 23 != 0:
        cur_pos = cur_pos.cw.insert_cw(m)
    else:
        for _ in range(7):
            cur_pos = cur_pos.ccw
        score_incr = m + cur_pos.value
        player_scores[cur_player] += score_incr
        cur_pos = cur_pos.remove()

print(max(player_scores))