from pypokerengine.engine.hand_evaluator import HandEvaluator
from pypokerengine.players import BasePokerPlayer
from pypokerengine.utils.card_utils import _pick_unused_card, _fill_community_card, gen_cards, estimate_hole_card_win_rate


class DataBloggerBot(BasePokerPlayer):
    def __init__(self):
        super().__init__()
        self.wins = 0
        self.losses = 0

    def declare_action(self, valid_actions, hole_card, round_state):
        # Estimate the win rate
        win_rate = estimate_hole_card_win_rate(nb_simulation=1000, nb_player=2, hole_card=gen_cards(hole_card), community_card=gen_cards(round_state['community_card']))
        #win_rate = estimate_hole_card_win_rate(nb_simulation=1000, nb_player=self.num_players, hole_card=hole_card, community_card=round_state['community_card'])
        # Check whether it is possible to call
        # if ((round_state['big_blind_pos']) == 0):
        #         print(round_state['round_count'])
        #         print('*****************yo soy big blind')
        # elif ((round_state['small_blind_pos']) == 0):
        #         print(round_state['round_count'])
        #         print('*****************yo soy small blind')

        print(round_state)
        #print(((round_state['small_blind_amount'])*2))
            
        call_amount = [item for item in valid_actions if item['action'] == 'call'][0]['amount']



        amount = None

        # If the win rate is large enough, then raise
        if win_rate > 0.5:
            raise_amount_options = [item for item in valid_actions if item['action'] == 'raise'][0]['amount']
            if win_rate > 0.85:
                # If it is extremely likely to win, then raise as much as possible
                action = 'raise'
                amount = raise_amount_options['max']
            elif win_rate > 0.75:
                # If it is likely to win, then raise by the minimum amount possible
                action = 'raise'
                amount = raise_amount_options['min']
            else:
                # If there is a chance to win, then call
                action = 'call'
        else:
            action = 'call' if (((round_state['big_blind_pos']) == 0) and call_amount == ((round_state['small_blind_amount'])*2) and ((round_state['street']) == 'preflop')) or (call_amount == 0)  else 'fold'

        # Set the amount
        if amount is None:
            items = [item for item in valid_actions if item['action'] == action]
            amount = items[0]['amount']

        return action, amount

    def receive_game_start_message(self, game_info):
        self.num_players = game_info['player_num']

    def receive_round_start_message(self, round_count, hole_card, seats):
        pass

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, action, round_state):
        pass

    def receive_round_result_message(self, winners, hand_info, round_state):
        is_winner = self.uuid in [item['uuid'] for item in winners]
        self.wins += int(is_winner)
        self.losses += int(not is_winner)


def setup_ai():
    return DataBloggerBot()