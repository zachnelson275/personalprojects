import java.util.Scanner;

public class ToDoApp {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            TDList myList = new TDList();
            
            System.out.println("Choose an option: \n1. Add Item manually\n2. Add default items\n3. Display all items\n4. Delete Item\n5. Complete Item\n6. Quit");
            int choice = scanner.nextInt();

            while (choice != 6) {
                switch (choice) {
                    case 1 -> myList.BuildItemFromInput(scanner);
                    case 2 -> myList.AddDefaultItems();
                    case 3 -> myList.DisplayItems();
                    case 4 -> myList.DeleteItem(scanner);
                    case 5 -> myList.CompleteItem(scanner);
                    default -> System.out.println("Invalid choice. Please try again.");
                }
            }
            scanner.close();
        }  
    }
}
