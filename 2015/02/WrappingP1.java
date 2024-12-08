import java.util.*;
import java.io.*;

public class WrappingP1 {
  public static void main(String[] args) throws FileNotFoundException {
    Scanner in = new Scanner(new File("wrapping.txt"));

    int total = 0;

    while (in.hasNextLine()) {
      // read in each line
      String line = in.nextLine();

      // split line into three parts 
      String[] nums = line.split("x");
      
      // convert each part into an integer 
      int num1 = Integer.valueOf(nums[0]);
      int num2 = Integer.valueOf(nums[1]);
      int num3 = Integer.valueOf(nums[2]);
      
      // multipy all pairs to get areas
      int[] surface_area = new int[3];
      surface_area[0] = num1*num2;
      surface_area[1] = num1*num3;
      surface_area[2] = num2*num3;
      Arrays.sort(surface_area);
       
      // calculate surface area from these products
      total += 2*(surface_area[0] + surface_area[1] + surface_area[2]) + surface_area[0];
     
      // add extra ppaper
      
      // add to total sqft
    }

    System.out.println(total);
  }
}
