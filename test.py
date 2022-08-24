from pypokerengine.utils.card_utils import gen_cards, estimate_hole_card_win_rate
import time

nb_simulation = 1000
nb_player = 3
hole_card = ['CA', 'C2']
community_card = ['H9', 'CK', 'C8']
hole_card = ['Tc', 'Jd']
community_card = ['Kc', '9h', '8c','Kd','Td']

start_time = time.time()
# your code

print(estimate_hole_card_win_rate(nb_simulation=100000, nb_player=2, hole_card=gen_cards(hole_card), community_card=gen_cards(community_card)))

elapsed_time = time.time() - start_time

print(elapsed_time)