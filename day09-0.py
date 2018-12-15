# sub 1: 436212, too high, runs slow (approx 15s)

marbles = [0]
cur_pos = 0

player_ct = 426
player_scores = [0] * player_ct
high_marble = 72058

for m in range(1, high_marble+1):
    cur_player = m % player_ct
    if m % 23 == 0:
        cur_pos = (cur_pos - 7) % len(marbles) + 1
        rem_val = marbles.pop(cur_pos)
        player_scores[cur_player] += m + rem_val
    else:
        cur_pos = (cur_pos + 2) % len(marbles)
        marbles = marbles[:cur_pos+1]+[m]+marbles[cur_pos+1:]

print(max(player_scores))