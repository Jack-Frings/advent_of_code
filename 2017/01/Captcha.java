import java.util.*;
import java.io.*;

public class Captcha {
  public static void main(String[] args) throws FileNotFoundException {
    Scanner scanner = new Scanner(new File("captcha.txt"));
    String line = scanner.nextLine();
    int sum = 0;
    for (int i = 0; i < line.length(); i++) {
      if (i < line.length() - 1) {
        if (line.substring(i, i+1).equals(line.substring(i+1, i+2))) {
          sum += Integer.valueOf(line.substring(i, i+1));
        }
      } else if (line.substring(i, i+1).equals(line.substring(0, 1))) {
        sum += Integer.valueOf(line.substring(i, i+1));
      }
    }
    //    System.out.println(sum);

    sum = 0;
    int halfway;
    for (int i = 0; i < line.length(); i++) { 
      halfway = i + (line.length() / 2);
      if (halfway >= line.length()) {
        halfway -= line.length();
      }
      if (line.substring(i, i+1).equals(line.substring(halfway, halfway+1))) {
        sum += Integer.valueOf(line.substring(i, i+1));
      }
    }
    System.out.println(sum);
  }
}
