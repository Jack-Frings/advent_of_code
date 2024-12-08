import java.util.*;
import java.io.*;

public class WrappingP2 {
  public static void main(String[] args) throws FileNotFoundException {
    Scanner in = new Scanner(new File("wrapping.txt"));

    int total = 0;

    while (in.hasNextLine()) {
      // read in each line
      String line = in.nextLine();

      // split line into three parts 
      String[] nums = line.split("x");
      
      // convert each part into an integer 
      int[] sides = new int[3];
      sides[0] = Integer.valueOf(nums[0]);
      sides[1] = Integer.valueOf(nums[1]);
      sides[2] = Integer.valueOf(nums[2]);
      Arrays.sort(sides);      
      
      total += (sides[0]*sides[1]*sides[2]) + 2*sides[0] + 2*sides[1]; 
     
      // add extra ppaper
      
      // add to total sqft
    }

    System.out.println(total);
  }
}
