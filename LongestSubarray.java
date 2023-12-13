import java.util.*;

public class LongestSubarray {

    public static int findLengthOfLongestSubarray(int[] nums) {
        int maxLength = 0;
        int start = 0;

        Map<Integer, Integer> lastIndexMap = new HashMap<>();

        for (int end = 0; end < nums.length; end++) {
            if (lastIndexMap.containsKey(nums[end])) {
                // If the current element is repeated, move the start index to the right of the previous occurrence
                start = Math.max(start, lastIndexMap.get(nums[end]) + 1);
            }

            // Update the last index of the current element
            lastIndexMap.put(nums[end], end);

            // Update the maximum length of the subarray
            maxLength = Math.max(maxLength, end - start + 1);
        }

        return maxLength;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();

        int[] nums = new int[size];

        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < size; i++) {
            nums[i] = scanner.nextInt();
        }

        int result = findLengthOfLongestSubarray(nums);

        System.out.println("Length of the longest subarray: " + result);
    }
}
