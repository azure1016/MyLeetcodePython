import java.util.*;

class Solution {
    public int maxPoints(int[][] points) {
        if (points == null) return 0;
        if (points.length < 3) return points.length;
        Map<Integer, Map<Integer, Integer>> map = new HashMap<Integer, Map<Integer, Integer>>();
        int result = 0;
        for (int i = 0; i < points.length; i++){
            int overlap = 0, dx = 0, dy = 0, max = 0;
            for (int j = i+1; j < points.length; j++){
                dx = points[j][0] - points[i][0];
                dy = points[j][1] - points[i][1];
                if (dx == 0 && dy == 0) {
                    overlap++;
                    continue;
                }
                else if (dx == 0) dy = 1;
                else if (dy == 0) dx = 1;
                else {
                    int g = gcd(dx, dy);
                    dx /= g;
                    dy /= g;
                }
                if (map.containsKey(dx)){
                    if (map.get(dx).containsKey(dy)) map.get(dx).put(dy, map.get(dx).get(dy) + 1);
                    else map.get(dx).put(dy, 1);
                }
                else{
                    Map<Integer, Integer> new_line = new HashMap<Integer, Integer>();
                    new_line.put(dy, 1);
                    map.put(dx, new_line);
                }
                max = Math.max(max, map.get(dx).get(dy));
            }
            result = Math.max(result, max + overlap + 1);
            map.clear();
        }
        return result;
    }

    public int gcd(int x, int y){
        int temp = x % y;
        while (temp != 0){
            x = y;
            y = temp;
            temp = x % y;
        }
        return y;
    }
}

