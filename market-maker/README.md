This is your classic rock, paper, scissor game implementation in java.

Compiling

To compile the code, I recommend using gradle. You can do this using:
```
docker pull gradle:latest
docker run --rm -u gradle -v "$PWD":/home/gradle/project -w /home/gradle/project gradle gradle jar
```

This takes care of the version requirements of Gradle, Groovy, and JDK required to build the project. 

Note: You might need to prefix those commands with a sudo depending on how you have configured docker on your system.

Once done your build artifact must be ready.

Run

You can run the code using 
```
java -jar build/libs/com.bhaavan.assignment.jar 
```

