/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package com.bhaavan.assignment;

import org.junit.Test;

import java.util.ArrayList;

import static org.junit.Assert.assertTrue;

public class RockPaperScissorTest {
    @Test public void testGetValidBotInput() {
        Player player = new Player(false);
        RockPaperScissor classUnderTest = new RockPaperScissor();
        int input = classUnderTest.get_input(player);
        assertTrue(input > 0 && input <= 3);
    }

    @Test public void testRockVsPaper() {
        assertTrue("Player 1 loses", new RockPaperScissor().judge_game(1,2) == Results.LOSS);
    }

    @Test public void testPaperVsRock() {
        assertTrue("Player 1 wins", new RockPaperScissor().judge_game(2,1) == Results.WIN);
    }

    @Test public void testScissorVsPaper() {
        assertTrue("Player 1 loses", new RockPaperScissor().judge_game(3,2) == Results.WIN);
    }

    @Test public void testScissorVsRock() {
        assertTrue("Player 1 wins", new RockPaperScissor().judge_game(3,1) == Results.LOSS);
    }

    @Test public void testScissorVsScissor() {
        assertTrue("Player draws", new RockPaperScissor().judge_game(3,3) == Results.DRAW);
    }

}