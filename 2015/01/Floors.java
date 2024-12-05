import java.util.*;
import java.io.*;

public class Floors {
  public static void main(String[] args) throws FileNotFoundException {
    Scanner readIn = new Scanner(new File("floors.txt"));
    String line = readIn.nextLine();
    int floor = 0;
    int first_neg = -1;
    for (int i = 0; i < line.length(); i++) {
      if (line.substring(i, i+1).equals("(")) {
        floor++;
      } else if (line.substring(i, i+1).equals(")")) {
        floor--;
        if (floor < 0 && first_neg == -1) {
          first_neg = i + 1;
        }
      }
    }

    System.out.println("Part One: " + floor);
    System.out.println("Part Two: " + first_neg);
  }
}
