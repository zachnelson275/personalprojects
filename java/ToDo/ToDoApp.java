import java.util.Scanner;

public class ToDoApp {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            TDList myList = new TDList();
            myList.BuildItemFromInput(scanner);
            // More input with scanner goes here
        }  
    }
}
