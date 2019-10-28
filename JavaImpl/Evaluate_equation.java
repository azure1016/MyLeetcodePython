//import java.util.Arrays.*;
import java.util.*;

public class Evaluate_equation {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> map = new HashMap<>();
        for (int i = 0; i < equations.size(); i++) {
            map.putIfAbsent(equations.get(i).get(0), new HashMap<>());
            map.putIfAbsent(equations.get(i).get(1), new HashMap<>());
            map.get(equations.get(i).get(0)).put(equations.get(i).get(1), values[i]);
            map.get(equations.get(i).get(1)).put(equations.get(i).get(0), 1.0 / values[i]);
        }

        double[] result = new double[queries.size()];
        for (int i = 0; i < queries.size(); i++) {
            result[i] = dfs(queries.get(i).get(0), queries.get(i).get(1), 1.0, map, new HashSet<>());
        }
        return result;
    }

    private double dfs(String src, String dst, double current_result, Map<String, Map<String, Double>> map,
            Set<String> seen) {
        if (!map.containsKey(src) | !map.containsKey(dst) | !seen.add(src))
            return -1;
        if (src.equals(dst))
            return current_result;
        for (String inter : map.get(src).keySet()) {
            double inter_result = dfs(inter, dst, current_result * map.get(src).get(inter), map, seen);
            if (inter_result != -1)
                return inter_result;
        }
        return -1;
    }

    
    public static void main(String[] args) {

        List<List<String>> equations = new ArrayList<>();
        equations.add(Arrays.asList("a", "b"));
        equations.add(Arrays.asList("b", "c"));
        equations.add(Arrays.asList("c", "d"));
       
        double[] values = new double[] {2.0, 3.0, 4.0};

        List<List<String>> queries = new ArrayList<>();
        queries.add(Arrays.asList("a", "c"));
        queries.add(Arrays.asList("a", "a"));
        queries.add(Arrays.asList("x", "x"));
        queries.add(Arrays.asList("a", "x"));
        Evaluate_equation calc = new Evaluate_equation();
        double[] result = calc.calcEquation(equations, values, queries);
        for(int i = 0; i < result.length; i++) {
            System.out.println(result[i]);
        }
    }
}