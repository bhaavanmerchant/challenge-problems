package com.bhaavan.assignment;

import java.util.ArrayList;

public class Arena {
    public final static int UNREASONABLE_ROUND_LIMIT = 100;
    int num_rounds = 10;

    public int getNum_rounds() {
        return num_rounds;
    }

    public ArrayList<Player> getPlayers() {
        return players;
    }

    public Scorecard getScorecard() {
        return scorecard;
    }

    ArrayList<Player> players = new ArrayList<Player>();
    Scorecard scorecard;

    public Arena(int rounds) {
        if (valid_number_of_rounds(rounds)) {
            num_rounds = rounds;
        } else {
            System.out.println("Invalid number of rounds. Using sane defaults. If this is incorrect, please exit.");
        }
        players.add(new Player(true));
        players.add(new Player(false));

        scorecard = new Scorecard(players);

    }

    public boolean valid_number_of_rounds(int n_rounds) {
        return (n_rounds > 0 && n_rounds < UNREASONABLE_ROUND_LIMIT);
    }

    public void start() {
        for (int i =0; i < num_rounds; i++) {
            // Play game
            Player playerOne = players.get(0);
            Player playerTwo = players.get(1);
            Game game = new RockPaperScissor();
            Results playerOneResult = game.play(playerOne, playerTwo);
            if (playerOneResult == Results.WIN) {
                scorecard.registerVictory(playerOne);
            } else if (playerOneResult == Results.LOSS) {
                scorecard.registerVictory(playerTwo);
            }
        }
        System.out.println("The rounds have ended. Thank you for gaming with us!");
        scorecard.printSummary();
    }
}
