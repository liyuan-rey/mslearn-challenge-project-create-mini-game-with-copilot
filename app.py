#

# 创建名为 choices 的不可变数组，包含三个值 rock, paper, or scissors
import random


choices = ('rock', 'paper', 'scissors')

# 创建名为 Rule 的类型，包含两个属性，分别表示赢家和输家，两个属性都是字符串
class Rule:
    def __init__(self, winner, loser):
        self.winner = winner
        self.loser = loser


# 创建名为 rules 的不可变数组，每个数组元素都是 Rule 类型的实例
rules = (
    Rule('rock', 'scissors'),
    Rule('scissors', 'paper'),
    Rule('paper', 'rock')
)

# 创建名为 player_score 和 computer_score 的整数变量，分别表示玩家和计算机的得分
player_score = 0
computer_score = 0

# 创建名为 player_choice 和 computer_choice 的字符串变量，分别表示玩家和计算机的选择
player_choice = ''
computer_choice = ''

# 创建名为 player_input 的函数，该函数接受一个字符串参数，并返回一个字符串
def player_input(prompt):
    while True:
        choice = input(prompt).lower()
        if choice in choices:
            return choice
        print("Invalid choice. Please enter rock, paper, or scissors.")

# 创建名为 computer_input 的函数，该函数返回 choices 数组中的一个随机元素
def computer_input():
    return random.choice(choices)

# 创建名为 get_winner 的函数，该函数接受两个字符串参数，分别表示玩家和计算机的选择，返回一个字符串
def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    for rule in rules:
        if rule.winner == player_choice and rule.loser == computer_choice:
            return 'player'
        if rule.winner == computer_choice and rule.loser == player_choice:
            return 'computer'
    return 'unknown'

# 创建名为 print_score 的函数，该函数接受两个整数参数，分别表示玩家和计算机的得分
def print_score(player_score, computer_score):
    print(f'Player: {player_score}, Computer: {computer_score}')

# 创建名为 print_choices 的函数，该函数接受一个字符串参数，表示玩家的选择
def print_choices(player_choice):
    print(f'Player: {player_choice}, Computer: {computer_choice}')

# 创建名为 print_winner 的函数，该函数接受一个字符串参数，表示赢家
def print_winner(winner):
    print(f'{winner} wins!')

# 创建名为 print_goodbye 的函数，该函数不接受参数
def print_goodbye():
    print('Goodbye!')

# 创建名为 play_game 的函数，该函数不接受参数
def play_game():
    global player_score
    global computer_score
    global player_choice
    global computer_choice
    player_choice = player_input('rock, paper, or scissors? ')
    computer_choice = computer_input()
    winner = get_winner(player_choice, computer_choice)
    if winner == 'player':
        player_score += 1
    if winner == 'computer':
        computer_score += 1
    print_choices(player_choice)
    print_winner(winner)
    print_score(player_score, computer_score)

# 创建名为 main 的函数，该函数不接受参数
def main():
    play_game()
    while player_score < 3 and computer_score < 3:
        play_game()
    print_goodbye()

# 调用 main 函数
main()




