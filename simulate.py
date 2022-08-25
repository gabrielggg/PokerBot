from pypokerengine.api.game import start_poker, setup_config
import itertools
import matplotlib.pyplot as plt

from callbot import CallBot
from databloggerbot import DataBloggerBot
import numpy as np

if __name__ == '__main__':
    blogger_bot = DataBloggerBot()

    # The stack log contains the stacks of the Data Blogger bot after each game (the initial stack is 100)
    stack_log = []
    stack_values = []
    stack_values_2 = []
    for round in range(50):
        p1, p2= blogger_bot, CallBot()

        config = setup_config(max_round=7, initial_stack=500, small_blind_amount=5)
        config.register_player(name="p1", algorithm=p1)
        config.register_player(name="p2", algorithm=p2)
        game_result = start_poker(config, verbose=1)

        stack_log.append([player['stack'] for player in game_result['players'] if player['uuid'] == blogger_bot.uuid])
        stack_values.append((int(np.mean(stack_log))))
        print('Avg. stack:', '%d' % (int(np.mean(stack_log))))
        print(stack_values)
        print(stack_log)
        #print(list(itertools.chain(*stack_log)))
        
    sum_list = itertools.accumulate(list(itertools.chain(*stack_log)))
    for index,num in enumerate(sum_list):
        print(num-(500*(index+1)))
        stack_values_2.append(num-(500*(index+1)))
    plt.plot(stack_values_2)
    plt.show()