class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> ast = new Stack<>();
        
        for(int a: asteroids){
            if(a>0){
                ast.push(a);
            }
            else{
                while(!ast.isEmpty() && ast.peek() > 0 && ast.peek()<-a){
                    ast.pop();
                }
                if(ast.isEmpty() || ast.peek()<0){
                    ast.push(a);
                }
                if(ast.peek()==-a){
                    ast.pop();
                }
            }
        }
         int[] res = new int[ast.size()];
        int i = ast.size() - 1;

        while(!ast.isEmpty()) {
            res[i--] = ast.pop();
        }

        return res;   
}
}