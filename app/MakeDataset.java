import java.nio.file.Files;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import kon.lib.coord.CoordDouble;
import kon.lib.col.Col;

public class MakeDataset{
    public static void main(String[] args){
        //int[] col_nums = {0,1};
        //CoordDouble jiko = new CoordDouble("../data/jinshin_zahyou_short.csv", col_nums);
        //jiko.readData(",");
        //jiko.show();
        Col target = new Col("../data/line_short.txt",0);
        target.readData(" ");
        for(int i=0; i<target.coords.size();i++){
            Path original_path= Paths.get("../data/image/"+(i+1)+".png");
            Path dataset_path= Paths.get("../data/datasets/road_shape/"+target.coords.get(i)+"/"+(i+1)+".png");
            try{
                Files.copy(original_path, dataset_path);
            }catch(IOException e){
                System.out.println("データセットのコピーに失敗しました(´・ω・)");
                e.printStackTrace();
            }
        }
    }
}
