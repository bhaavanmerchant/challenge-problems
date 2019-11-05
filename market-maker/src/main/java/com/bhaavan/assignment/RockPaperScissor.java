package com.bhaavan.assignment;

import com.google.common.collect.ImmutableMap;

import java.util.*;

public class RockPaperScissor implements Game {

    int get_input(Player player) {
        if (player.player_type == PlayerType.HUMAN) {
            return get_user_input();
        }
        return get_bot_input();
    }

    int get_bot_input() {
        return new Random().nextInt(3) + 1;
    }

    int get_user_input() {
        System.out.println("Enter your choice:️️");
        int hand = 0;
        boolean valid_move = false;
        while (!valid_move) {
            try {
                Scanner input = new Scanner(System.in);
                hand = input.nextInt();
                if (hand < 1 || hand > 3) {
                    throw new InputMismatchException();
                }
                valid_move = true;
            } catch (InputMismatchException e) {
                System.out.println("You entered an illegal value. Acceptable values are 1, 2 or 3. Please try again.");
            }
        }
        return hand;
    }

    public Results judge_game(int moveOne, int moveTwo) {
        if (moveOne == moveTwo) {
            return Results.DRAW;
        } else if ( (moveTwo + 2) % 3 == (moveOne %3) ) {
            return Results.LOSS;
        }
        return Results.WIN;
    }

    final Map<Integer, String> map = ImmutableMap.of(1,"Rock \uD83D\uDC4A", 2, "Paper \uD83D\uDD90", 3, "Scissor ✌");

    @Override
    public Results play(Player player1, Player player2) {
        System.out.println("Your valid choices are:");
        for (int i = 1; i <=3 ; i++) {
            System.out.println("(" + String.valueOf(i) + ") " + map.get(i));
        }
        int playerOneMove = get_input(player1);
        int playerTwoMove = get_input(player2);
        System.out.println(player2.name + " played " + map.get(playerTwoMove));
        Results r = judge_game(playerOneMove, playerTwoMove);
        if (r == Results.WIN) {
            System.out.println("You win!");
        } else  if (r == Results.DRAW) {
            System.out.println("It's a draw.");
        } else {
            System.out.println("You lose!");
        }
        return r;
    }
}
