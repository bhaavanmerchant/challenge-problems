/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package com.bhaavan.assignment;

import org.junit.Test;

import static org.junit.Assert.assertTrue;

public class PlayerTest {
    @Test public void testNameGenerator() {
        Player classUnderTest = new Player(true);
        System.out.println(classUnderTest.generate_random_name().length());
        assertTrue("random string name is generated", classUnderTest.generate_random_name().length() == 8);
    }

    @Test public void testBotGetsBotName() {
        Player classUnderTest = new Player(false);
        assertTrue("bot is initialized with a bot prefix", classUnderTest.name.startsWith("BOT_"));
    }

    @Test public void testHumanPlayerIsHuman() {
        Player classUnderTest = new Player(true);
        assertTrue("Player is of type human", classUnderTest.player_type == PlayerType.HUMAN);
    }
}
