import java.sql.Timestamp;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;

public class Item {
    private final String name;
    private final Timestamp timeCreated;
    private Timestamp finishByTime;
    private final Timestamp timeCompleted;
    private Timestamp reminderTimestamp;
    private boolean isDone;
    private List<Detail> details;
    
    public Item(String name, Timestamp timeCreated, Timestamp finishByTime, Timestamp timeCompleted, Timestamp reminderTimestamp, boolean isDone) {
        this.name = name;
        this.timeCreated = timeCreated;
        this.finishByTime = finishByTime;
        this.timeCompleted = timeCompleted;
        this.reminderTimestamp = reminderTimestamp;
        this.isDone = isDone;
        this.details = new ArrayList<>();
    }

    public void DisplayInfo() {
        // Format info for print
        String createDate = new SimpleDateFormat("MM/dd/yyyy HH:mm:ss").format(timeCreated);
        String finishDate = new SimpleDateFormat("MM/dd/yyyy HH:mm:ss").format(finishByTime);
        String reminderDate = new SimpleDateFormat("MM/dd/yyyy HH:mm:ss").format(reminderTimestamp);
        String statusString = isDone 
            ? "Completed " + new SimpleDateFormat("MM/dd/yyyy HH:mm:ss").format(timeCompleted)
            : "Not Complete";

        // Get details from the item
        StringBuilder detailsListBuilder = new StringBuilder();
            for (Detail detail : details) {
                detailsListBuilder.append("  - ").append(detail.getInfo()).append(System.lineSeparator());
        }

        // Format info and details for output
        String detailsString = String.format(
            "%s%nCreated on: %s%nFinish by: %s%nReminder set for: %s%n%s%ndetails:%n%s",
            name, createDate, finishDate, reminderDate, statusString, detailsListBuilder.toString()
        );

        System.out.println(detailsString);
    }

    public void AddDetail(Detail detail) {
        details.add(detail);
    }

    public String GetName() {
        return this.name;
    }
}