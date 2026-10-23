class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int n= rooms.size();
        boolean[] visited = new boolean[n];
        dfs(0,rooms,visited);
        for(boolean isVisited : visited){
            if(!isVisited){
                return false;
            }
        }
        return true;
    }

    private void dfs(int currentRoom, List<List<Integer>> rooms, boolean[] visited){
        visited[currentRoom] = true;
        for(int key : rooms.get(currentRoom)){
            System.out.println(rooms.get(currentRoom));
             if (!visited[key]) {
                dfs(key, rooms, visited);
            }
        }
    }
}