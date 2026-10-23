class Solution {
    public int equalPairs(int[][] grid) {
        int n = grid.length;
        Map<String,Integer> rowCount = new HashMap<>();
        for (int i=0;i<n;i++){
            String rowString= Arrays.toString(grid[i]);
            rowCount.put(rowString,rowCount.getOrDefault(rowString,0) + 1);
        }

        int equalPairsCount = 0;
        for(int j=0;j<n;j++){
            int[] colArray=new int[n];
            for(int i=0;i<n;i++){
                colArray[i]=grid[i][j];
            }
            String colString = Arrays.toString(colArray);
            if (rowCount.containsKey(colString)){
                equalPairsCount+=rowCount.get(colString);
            }
        }
        return equalPairsCount;
    }
}