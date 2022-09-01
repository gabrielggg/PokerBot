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
    stack_parsed = []
    for round in range(5):
        p1, p2= blogger_bot, CallBot()

        config = setup_config(max_round=10, initial_stack=500, small_blind_amount=5)
        config.register_player(name="p1", algorithm=p1)
        config.register_player(name="p2", algorithm=p2)
        game_result, round_count, stack = start_poker(config, verbose=1)
        print(round_count,"testtest")
        print(stack, "testest222")

        stack_log.append([player['stack'] for player in game_result['players'] if player['uuid'] == blogger_bot.uuid])
        stack_values.append((int(np.mean(stack_log))))
        print('Avg. stack:', '%d' % (int(np.mean(stack_log))))
        print(stack_values)
        print(stack_log)
        actual_stack = 500
        for index,stack_1 in enumerate(stack):
            stack_parsed.append(stack_1["p1"] - actual_stack)
            actual_stack = stack_1["p1"]
            
        #print(list(itertools.chain(*stack_log)))
    print(stack_parsed)    
    sum_list = itertools.accumulate(stack_parsed)
    print(sum_list)
    for index,num in enumerate(sum_list):
        stack_values_2.append(num)
    print(stack_values_2)
    bb100 = (stack_values_2[-1]/10) / (len(stack_values_2)/100)
    print(stack_values_2[-1], len(stack_values_2))
    print(bb100, " <---bb/100")
    plt.plot(stack_values_2)
    plt.show()