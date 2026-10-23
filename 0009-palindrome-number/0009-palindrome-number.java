class Solution {
    public boolean isPalindrome(int x) {
        String temp = Integer.toString(x);
        String result = "";
        for(int i = temp.length()-1; i>=0; i--){
            System.out.println(temp.charAt(i));
            result = result + temp.charAt(i);
        }
        // System.out.println(result);
        // System.out.println(temp);
        if(temp.equals(result)){
            return true;
        }
        return false;
    }
}