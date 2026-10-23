

int reverse(int x)
{
    int digits[20] = {0};                   // store all digits， x = 123, digits=[3,2,1];       x = 120,  digits=[0,2,1]
    int len = 0;                                 // store length of digits 
    int isNegtive = (x < 0) ? 1:0;    // 

    long num = x;                            // using long to avoid overflow
    if (num < 0) num = -num;        // Notice: cannot use  -x, cause may overflow
 
    while(num > 0 ) {
        int digit = num % 10;
        digits[len++] = digit;
        num /= 10;
    }
    // trim all zeros in the front of digits ， 如 x = 1200，digits=[0,0,2,1]  => firstNonZero=2
    int firstNonZero = 0;
    for(firstNonZero = 0; firstNonZero < len; firstNonZero++) {
        if ( digits[firstNonZero] != 0) break;
    }

    long ret = 0; // store reversed number,  if x = 123, digits=[3,2,1]， ret = (1+10*0) + (2+10*1) + (3+10*2)
    for(int i = firstNonZero; i < len; i++) {
        //printf("i=%d digits[i]=%d, ret = %ld\n", i, digits[i], ret);
        ret = ret * 10 + digits[i];
    }

    if (isNegtive)  ret = -ret;

    // check if overflowed
    if( ret > INT32_MAX || ret < INT32_MIN) return 0;

    return (int)ret;
}