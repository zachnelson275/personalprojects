import java.sql.Timestamp;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class TDList {
    private int size;
    private List<Item> items;

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
            item.DisplayDetails();
            System.out.println();
        }
    }
}