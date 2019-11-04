package project;

import java.util.HashMap;
import java.util.Map;

public class Scorecard {
    HashMap<Player, Integer> results = new HashMap<>();
    public Scorecard(Player[] players) {
        for (Player player : players) {
            results.put(player, 0);
        }
    }

    public void registerVictory(Player p) {
        results.put(p, results.get(p) + 1);
    }

    public void printSummary() {
        System.out.println("Summary of results (win counts):");
        for (Map.Entry<Player, Integer> entry: results.entrySet()) {
            System.out.println("Player " + entry.getKey().name + " : " + entry.getValue());
        }
    }
}
