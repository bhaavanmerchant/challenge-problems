package project;

import java.nio.charset.Charset;
import java.util.Random;

public class Player {
    String name;
    enum Type {
        BOT,
        HUMAN
    }
    Type player_type;

    public Player(boolean is_human) {
        name = generate_random_name();
        if (is_human) {
            player_type = Type.HUMAN;
        } else {
            player_type = Type.BOT;
            name = "BOT_" + name;
        }
    }

    public String generate_random_name() {
        byte[] array = new byte[7]; // length is bounded by 7
        new Random().nextBytes(array);
        return new String(array, Charset.forName("UTF-8"));
    }

}
