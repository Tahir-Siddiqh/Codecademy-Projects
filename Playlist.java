import java.util.ArrayList;

class Playlist {
  
  public static void main(String[] args) {
    // Creating Playlist
    ArrayList<String> desertIslandPlaylist = new ArrayList<String>();
    // Adding Songs    
    desertIslandPlaylist.add("Sicko Mode - Travis Scott");
    desertIslandPlaylist.add("90210 - Travis Scott");
    desertIslandPlaylist.add("Feel Good Inc.- Gorillaz");
    desertIslandPlaylist.add("Dirty Harry - Gorillaz");
    desertIslandPlaylist.add("One More Time - Daft Punk");
    desertIslandPlaylist.add("Mo Bamba - Sheck Wes");
    // Check for the list.
    // System.out.println(desertIslandPlaylist);
    // Size should be Less than or equal to 5.
    // System.out.println(desertIslandPlaylist.size());
    // Removing last item.
    desertIslandPlaylist.remove("Mo Bamba - Sheck Wes");
    // Check for size.
    // System.out.println(desertIslandPlaylist.size());
    // Shuffling the list.
    int indexA = desertIslandPlaylist.indexOf("Dirty Harry - Gorillaz");
    int indexB = desertIslandPlaylist.indexOf("90210 - Travis Scott");
    String tempA = "Dirty Harry - Gorillaz";
    desertIslandPlaylist.set(indexA, "90210 - Travis Scott");
    desertIslandPlaylist.set(indexB, tempA);
    System.out.println(desertIslandPlaylist);
  }
  
}
