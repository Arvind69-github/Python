import java.util.Scanner;

public class UppercaseToLowercase {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a string with uppercase letters: ");
        String inputString = scanner.nextLine();

        // Convert the string to lowercase
        String convertedString = convertUppercaseToLowercase(inputString);

        // Display the result
        System.out.println("Converted string: " + convertedString);
    }

    public static String convertUppercaseToLowercase(String input) {
        // Convert each uppercase letter to lowercase using toLowerCase() method
        String result = "";
        for (int i = 0; i < input.length(); i++) {
            char currentChar = input.charAt(i);
            if (Character.isUpperCase(currentChar)) {
                result += Character.toLowerCase(currentChar);
            } else {
                result += currentChar;
            }
        }
        return result;
    }
}
