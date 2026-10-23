class Solution {
    public boolean isIsomorphic(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        String res="";
        HashMap<String,String> map=new HashMap<>();
        for(int i=0;i<s.length();i++){
           
            if(!map.containsKey(s.charAt(i)+"") && !(map.values().contains(t.charAt(i)+""))){
                map.put(s.charAt(i)+"",t.charAt(i)+"");
            }
        }
        System.out.println(map);
        for(int j=0;j<t.length();j++){
            res+=map.get(s.charAt(j)+"");
        }
        //System.out.println(res);
        if(res.equals(t)) return true;
        else return false;
    }
}