package project;

import java.util.ArrayList;

public class Game {
    public final static int UNREASONABLE_ROUND_LIMIT = 100;
    int num_rounds = 10;
    ArrayList<Player> players = new ArrayList<Player>();
    Scorecard scorecard;

    public Game(int rounds) {
        if (valid_number_of_rounds(rounds)) {
            num_rounds = rounds;
        } else {
            System.out.println("Invalid number of rounds. Using sane defaults. If this is incorrect, please exit.");
        }
        players.add(new Player(true));
        players.add(new Player(false));

        scorecard = new Scorecard((Player[]) players.toArray());

    }

    public boolean valid_number_of_rounds(int num_rounds) {
        return (num_rounds > 0 && num_rounds < UNREASONABLE_ROUND_LIMIT);
    }

    public void start() {
        for (int i =0; i < num_rounds; i++) {
            // Play game
            // update scorecard
        }
    }
}
