

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size)
{
    int n=nums1Size+nums2Size;
    int sorted[n];
    int j,k;
    int i=0;
    j=k=0;
    while(j<nums1Size && k<nums2Size)
    {
        if(nums1[j]<nums2[k])
        {
            sorted[i++]=nums1[j];
            j++;
        }
        else
        {
            sorted[i++]=nums2[k];
            k++;
        }
    }
    while(j<nums1Size)
    {
        sorted[i++]=nums1[j];
        j++;
    }
    while(k<nums2Size)
    {
        sorted[i++]=nums2[k];
        k++;
    }
    if(n%2==0)
    {
        int a,b;
        a=sorted[(n/2)-1];
        b=sorted[n/2];
        double res=(a+b)/2.0;
        return res;
    }
    else
    {
        return sorted[((n+1)/2)-1];
    }
}
