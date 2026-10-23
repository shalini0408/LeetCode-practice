class Solution {
    public int[] plusOne(int[] digits) {
        int carry=1;
        int sum=0;
        int i=digits.length-1;
        int arr[]=new int[digits.length+1];
        while(i>=0){
            sum=carry+digits[i];
            if(sum>9){
                digits[i]=sum%10;
                carry=sum/10;
            }
            else{
                digits[i]+=1;
                return digits;
            }
            i=i-1;
        }
        if(carry>0){
           arr[0]=carry;
           for(int j=1;j<arr.length;j++){
               arr[j]=digits[j-1];
           }
        }
        
        return arr;
    }
}