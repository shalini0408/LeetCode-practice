class Solution {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] res = new int[length];
        int prefix = 1; //[1,1,2,6] pref = 24
        for (int i=0;i<nums.length;i++){
            res[i]= prefix;
            prefix = prefix*nums[i];
        }
        int suffix = 1;
        for(int j = length-1;j>=0;j--){
            res[j]=res[j]*suffix;
            suffix = suffix*nums[j];
        }
        return res;
    }
}