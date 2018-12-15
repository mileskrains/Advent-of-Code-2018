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