'''
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.
'''


def divisorGame(n):

    return n % 2 == 0


print(divisorGame(21))

'''
- if the number is even for alice to always win she can use the strategy of if n is even she choose i so that once subtracted n will be odd forcing bob
to pick and odd number after which she will continue until she gets to one leaving bob with not number to choose from (optimamlly)
- if the number is odd bob can use the same to strategy to win

- simply put if each player was to play optimally;
    - Alice will always win if the number is even and Bob will always win if the number is odd

'''
