# from replit import clear
from art import logo
import random

def blackjack_game():

  def start_deal(cards):
      shuffled = random.choice(cards)
      return shuffled

  def player_loss(player, computer):
    if sum(player) != 21 and sum(computer) == 21:
      return True
    elif sum(player) == 21 and sum(computer) == 21:
      return True
  # if computer get the 21 as the first hand, computer win, and player loss.

  def done_playing():
    player_sum = sum(player_cards)
    computer_sum = sum(computer_cards)
    print(f"Your hand is: {player_cards}, a total of {player_sum}.")
    print(f"The computer's hand is {computer_cards}, a total of {computer_sum}.")

    if sum(computer_cards) > 21:
      print("The computer got a bust, you win!")
      # cards number bigger than 21 then loss
    elif player_loss(player_cards, computer_cards):
      print("You lose.")
    # when player choose n, not continue the game, then 
    # calculate the sum of computer card sum and player card sum
    elif sum(player_cards) == 21 and sum(computer_cards) != 21:
      print("You win!")
    # player got blackjack but computer didn't player win
    elif sum(player_cards) > 21:
      print("It's a bust, you lose.")
    # player cards number bigger than 21 but computer smaller than 21, then lose
    elif player_sum == computer_sum:
      print("It's a draw.")
    elif player_sum > computer_sum:
      print("You win!")
    else:
      print("You lose.")
    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again == 'y':
      # clear()
      blackjack_game()
    else:
      if play_again == 'n':
        print("Goodbye.")

  def keep_playing():
    shuffled = start_deal(cards)
    player_cards.append(shuffled)
    computer_cards.append(start_deal(cards))
    player_sum = sum(player_cards)
    computer_cards_sum = sum(computer_cards)
    if 11 in player_cards and player_sum >= 21:
      ace = player_cards.index(11)
      player_cards[ace] = 1
      player_sum = sum(player_cards)
    print(f"Your hand is: {player_cards}, a total of {player_sum}.")
    print(f"The computer's hand is {computer_cards}, a total of {computer_cards_sum}.")
    if player_sum > 21:
      print("It's a bust, you lose.")
      play_again = input("Do you want to play again? Type 'y' or 'n': ")
      if play_again == 'y':
        # clear()
        blackjack_game()
      elif play_again == 'n':
        print("Thanks for playing. Goodbye.")
    if player_sum <= 21:
      hit = input("Type 'y' to get another card, type 'n' to pass: ")
      if hit == 'y':
        keep_playing()
      elif hit == 'n':
        done_playing()
  
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player_cards = []
  computer_cards = []
  player_cards.append(start_deal(cards))
  player_cards.append(start_deal(cards))
  computer_cards.append(start_deal(cards))
  computer_cards.append(start_deal(cards))
  # computer first hand is only one card, and player first hand is two cards.
  # At the start of a Blackjack game, the players and the dealer receive two cards each. 
  print(f"Your cards: {player_cards}")
  print(f"The computer's first card: {computer_cards}")
  # if sum(cpu_cards) == 21:
  #   print("")
  
  hit = input("Type 'y' to get another card, type 'n' to pass: ")
  if hit == 'n':
    done_playing()
  elif hit == 'y':
    keep_playing()

blackjack_game()
