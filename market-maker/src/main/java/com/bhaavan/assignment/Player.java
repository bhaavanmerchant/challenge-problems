package com.bhaavan.assignment;

import java.nio.charset.Charset;
import java.util.Random;

public class Player {
    String name;
    PlayerType player_type;

    public Player(boolean is_human) {
        name = generate_random_name();
        if (is_human) {
            player_type = PlayerType.HUMAN;
        } else {
            player_type = PlayerType.BOT;
            name = "BOT_" + name;
        }
    }

    public String generate_random_name() {
        return "Player" + String.valueOf(10 + new Random().nextInt(89));
    }

}
