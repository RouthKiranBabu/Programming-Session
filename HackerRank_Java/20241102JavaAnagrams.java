import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.List;
import java.util.ArrayList;

public class JavaAnagrams{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String fs = scanner.next();
        String ss = scanner.next();
        scanner.close();

        if (fs.length() == ss.length()){
            Map<String, Integer> dict1 = new HashMap<>();
            Map<String, Integer> dict2 = new HashMap<>();

            for (int i = 0; i < fs.length(); i ++){
                //System.out.println(fs.substring(i, i + 1) + ", " + ss.substring(i, i + 1));
                String fss = fs.substring(i, i + 1);
                String sss = ss.substring(i, i + 1);
                String fssk = new String();
                String sssk = new String();

                boolean lowercase_fss = makelower(fss);
                boolean lowercase_sss = makelower(sss);

                if (lowercase_fss){
                    fssk = fss.toUpperCase() + fss;
                }else{
                    fssk = fss + fss.toLowerCase();
                }

                if (lowercase_sss){
                    sssk = sss.toUpperCase() + sss;
                }else{
                    sssk = sss + sss.toLowerCase();
                }

                boolean yfss = dict1.containsKey(fssk);
                boolean ysss = dict2.containsKey(sssk);

                if (!yfss){
                    dict1.put(fssk, 1);
                }else{
                    dict1.put(fssk, dict1.get(fssk) + 1);
                }

                if (!ysss){
                    dict2.put(sssk, 1);
                }else{
                    dict2.put(sssk, dict2.get(sssk) + 1);
                }
            }

            Set<String> dict1k = dict1.keySet();
            Set<String> dict2k = dict2.keySet();

            if (dict1k.size() == dict2k.size()){
                boolean con = true;
                List<String> list1 = new ArrayList<>(dict1k);
                for(int i = 0; i < dict1k.size(); i ++){
                    if (dict1.get(list1.get(i)) != dict2.get(list1.get(i))){
                        con = false;
                        break;
                    }
                }  
                if (con){
                    System.out.println("Anagrams");
                }else{
                    System.out.println("Not Anagrams");
                }
                
            }else{
                System.out.println("Not Anagrams");
            }
        }else{
            System.out.println("Not Anagrams");
        }
    }
    public static boolean makelower(String str){
        return str.equals(str.toLowerCase());
    }
}
