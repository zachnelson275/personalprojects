import java.util.Scanner;

public class ToDoApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        TDList myList = new TDList();

        myList.BuildItemFromInput(scanner);

        // If you plan more input, do it here

        scanner.close();  
    }
}
