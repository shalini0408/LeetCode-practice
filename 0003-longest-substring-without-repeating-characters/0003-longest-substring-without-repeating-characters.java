class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i = 0;
        int longest = 0;
        Set<Character> set = new HashSet<>();

        for (int j = 0; j < s.length(); j++) {

            while (set.contains(s.charAt(j))) {
                set.remove(s.charAt(i));
                i++;
            }

            set.add(s.charAt(j));

            int len = j - i + 1;
            longest = Math.max(longest, len);
        }

        return longest;
    }
}