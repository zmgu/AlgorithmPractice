class Solution {
    public int[] solution(String s) {
        int[] answer = new int[2];
        int rt = 0;
        int rem0 = 0;
        String str = "";
        do{           
            str = "";
            
            for(int i = 0; i<s.length();i++){
                if(s.charAt(i)=='1'){
                    str += "1";
                } else {
                    rem0 ++;
                }
            }
            int strl = str.length();
            s = Integer.toBinaryString(strl);
            rt ++;
        }while(s.length()>1);
        
        answer[0] = rt;
        answer[1] = rem0;
        
        return answer;
    }
}
