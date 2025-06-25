import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

public class TDList {
    private int size;
    private final List<Item> items;

    public TDList() {
        this.size = 0;
        this.items = new ArrayList<>();
    }

    public void AddItem(Item item) {
        items.add(item);
    }

    public void BuildItemFromInput(Scanner scanner) {
    System.out.print("Enter item name: ");
    String name = scanner.nextLine();

    Timestamp timeCreated = new Timestamp(System.currentTimeMillis());

    System.out.print("Enter finish by time (yyyy-MM-dd HH:mm:ss): ");
    Timestamp finishByTime = Timestamp.valueOf(scanner.nextLine());

    System.out.print("Enter reminder time (yyyy-MM-dd HH:mm:ss): ");
    Timestamp reminderTimestamp = Timestamp.valueOf(scanner.nextLine());

    Timestamp timeCompleted = null;
    boolean isDone = false;

    Item item = new Item(name, timeCreated, finishByTime, timeCompleted, reminderTimestamp, isDone);

    System.out.println("Enter details (type 'end' to finish):");
    while (true) {
        String detailText = scanner.nextLine();
        if (detailText.equalsIgnoreCase("end")) {
            break;
        }
        item.AddDetail(new Detail(detailText));
    }

    AddItem(item);
    size += 1;
    System.out.println("Item successfully created and added!");
    }

    public int GetSize() {
        return size;
    }

    public void DisplayItems(){
        for (Item item : items) {
            item.DisplayInfo();
            System.out.println();
        }
    }

    public void DeleteItem(Scanner scanner) {
        int itemIndex = 0;
        for (Item item : items) {
            itemIndex += 1;
            String printItem = String.format("%s - %s", itemIndex, item.GetName());
            System.out.println(printItem);
        }
        System.out.print("Which item would you like to delete?  ");

        int choiceIndex = scanner.nextInt() - 1;
        try {
            items.remove(choiceIndex);
        } catch (IndexOutOfBoundsException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    public void CompleteItem(Scanner scanner) {
    if (items.isEmpty()) {
        System.out.println("No items to complete.");
        return;
    }

    // Loop through items, then number and print them
    int itemIndex = 1;
    for (Item item : items) {
        String printItem = String.format("%d - %s", itemIndex, item.GetName());
        System.out.println(printItem);
        itemIndex++;
    }

    System.out.print("Which item would you like to mark as complete? ");

    try {
        int choiceIndex = scanner.nextInt() - 1;
        scanner.nextLine();

        Item chosenItem = items.get(choiceIndex);
        if (!chosenItem.GetIsDone()) {
            chosenItem.SetIsDone(true);
            chosenItem.SetTimeCompleted(new Timestamp(System.currentTimeMillis()));
            System.out.println("Marked \"" + chosenItem.GetName() + "\" as completed.");
        } else {
            System.out.println("That item is already marked as completed.");
        }
    } catch (IndexOutOfBoundsException e) {
        System.out.println("Invalid choice: index out of bounds.");
    } catch (InputMismatchException e) {
        System.out.println("Invalid input: please enter a number.");
        scanner.nextLine(); // clear the bad input
    }
}


    public void AddDefaultItems() {
        Item item1 = new Item("Buy groceries", new Timestamp(System.currentTimeMillis()), 
                              Timestamp.valueOf("2023-10-15 18:00:00"), null, 
                              Timestamp.valueOf("2023-10-15 17:00:00"), false);
        item1.AddDetail(new Detail("Milk"));
        item1.AddDetail(new Detail("Eggs"));
        AddItem(item1);

        Item item2 = new Item("Complete project report", new Timestamp(System.currentTimeMillis()), 
                              Timestamp.valueOf("2023-10-20 23:59:59"), null, 
                              Timestamp.valueOf("2023-10-19 12:00:00"), false);
        item2.AddDetail(new Detail("Draft the introduction"));
        item2.AddDetail(new Detail("Review with team"));
        AddItem(item2);
    }
}