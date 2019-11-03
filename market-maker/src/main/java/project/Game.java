package project;

public class Game {
    public final static int UNREASONABLE_ROUND_LIMIT = 100;
    int num_rounds = 10;
    public Game(int rounds) {
        if (valid_number_of_rounds(rounds)) {
            num_rounds = rounds;
        } else {
            System.out.println("Invalid number of rounds. Using sane defaults. If this is incorrect, please exit.");
        }
    }

    public boolean valid_number_of_rounds(int num_rounds) {
        return (num_rounds > 0 && num_rounds < UNREASONABLE_ROUND_LIMIT);
    }

    public void start() {

    }
}
