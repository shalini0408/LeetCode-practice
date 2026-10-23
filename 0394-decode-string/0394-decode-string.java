class Solution {
    public String decodeString(String s) {
        Stack<Object> stack = new Stack<>();
        StringBuilder sb = new StringBuilder();
        int n = 0;

        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                n = n * 10 + (c - '0');
                System.out.println("Digit: " + c + " → n=" + n);

            } else if (c == '[') {
                System.out.println("'[' → pushing sb=\"" + sb + "\" and n=" + n);
                stack.push(sb);
                stack.push(n);
                sb = new StringBuilder();
                n = 0;
                System.out.println("     stack=" + stack + " | sb reset to \"\" | n reset to 0");

            } else if (c == ']') {
                int k = (int)stack.pop();
                StringBuilder prev = (StringBuilder) stack.pop();
                System.out.println("']' → popped k=" + k + ", popped prev=\"" + prev + "\", current sb=\"" + sb + "\"");
                while (k-- > 0) prev.append(sb);
                sb = prev;
                System.out.println("     after repeat → sb=\"" + sb + "\"");

            } else {
                sb.append(c);
                System.out.println("Char: " + c + " → sb=\"" + sb + "\"");
            }
        }

        System.out.println("\nFinal result: " + sb);
        return sb.toString();
    }
}