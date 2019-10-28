public class WildMatch {
    public boolean isMatch (String s, String p) {
        int i = 0, j = 0;
        int m = s.length(), n = p.length();
        int last_match = -1, starj = -1;
        while (i < m) {
            if ( j < n && (s.charAt(i) == p.charAt(j) || p.charAt(j) == '?')) {
                i++; j++;
            } else if (j < n && p.charAt(j) == '*') {
                starj = j;
                j++;
                last_match = i;
            }
            else if (starj != -1) { // there's  '*' thing 
                j = starj + 1;
                last_match++;
                i = last_match;
            }
            else return false;
        }
        while (j < n && p.charAt(j) == '*') j++;
        return j == n;
    }

    public static void main (String[] args) {
        String s = "aab";
        String p = "*a*b";
        boolean result = new WildMatch().isMatch(s, p);
        System.out.println(result);
    }
}