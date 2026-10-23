class Solution {
    public boolean isPalindrome(String s) {
        if(s=="") return true;
        String s1=(s.replaceAll("[^A-Za-z0-9]","")).toLowerCase();
        //System.out.println(s1);
        String rev="";
        for(int i=s1.length()-1;i>=0;i--){
            rev+=s1.charAt(i);
        }
        if(rev.equals(s1)) return true;
        else return false;
    }
}