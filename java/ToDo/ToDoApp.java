import java.util.Scanner;

public class ToDoApp {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            TDList myList = new TDList();
            
            System.out.println("Choose an option: \n1. Add Item manually\n2. Add default items\n3. Display all items");
            int choice = scanner.nextInt();

            if (choice == 1) {
                myList.BuildItemFromInput(scanner);
            } else if (choice == 2) {
                myList.AddDefaultItems();
            } else if (choice == 3) {
                myList.DisplayItems();
            } else {
                System.out.println("Invalid choice. Please try again.");
            }
            scanner.close();
        }  
    }
}
