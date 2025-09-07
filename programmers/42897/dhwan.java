//dp방

class Solution {
    public int solution(int[] money) {
        int n = money.length;

        // 첫 번째 집을 털 경우 -> 마지막 집은 못 털음
        int[] dp1 = new int[n];
        dp1[0] = money[0];
        dp1[1] = Math.max(money[0], money[1]);

        for (int i = 2; i < n - 1; i++) {
            dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + money[i]);
        }

        // 첫 번째 집을 안 털 경우 -> 마지막 집까지 털 수 있음
        int[] dp2 = new int[n];
        dp2[1] = money[1];
        for (int i = 2; i < n; i++) {
            dp2[i] = Math.max(dp2[i - 1], dp2[i - 2] + money[i]);
        }

        return Math.max(dp1[n - 2], dp2[n - 1]);
    }
}


//그리디방식( 최종 실패)
//
//class Solution {
//    public static void main(String[] args){
//
//        int[] arr = {1,2,3,1};
//
//        Solution solution = new Solution();
//        System.out.println(solution.solution(arr));
//    }
//
//    public int solution(int[] money) {
//        int answer = 0;
//        int[] steal = new int[money.length];
//
//        Integer[] indexlist = new Integer[money.length];
//        for(int i=0;i<money.length;i++){
//            indexlist[i] = i;
//        }
//
//        Arrays.sort(indexlist, (i, j) -> money[j] - money[i]);
//
//
//        for (int i = 0; i < money.length; i++) {
//            pickYN(money, steal, indexlist[i]);
//        }
//        for (int i = 0; i < money.length; i++) {
//            if (steal[i] == 1) {
//                answer += money[indexlist[i]];
//            }
//        }
//        return answer;
//    }
//
//    public void pickYN(int[] money, int[] steal, int num) {
//        //해당원소를 고르게되면 양옆을 못 고르기 때문에 양옆의 합산과 해당원소의 값을 비교하여 훔칠지 말지를 결정하고자 함.
//        //두 값이 값이 같을경우 1집을 터는게 더 이득이므로 조건절에 반영함
//        if (num == 0) {
//            //배열 첫번째,마지막 비교를 위한 조건
//            if (steal[0] == 1 || steal[money.length - 1] == 1 || steal[1] == 1) {
//                return;
//            } else {
//                if (money[0] >= money[money.length - 1] + money[1]) {
//                    steal[0] = 1;
//                } else {
//                    steal[1] = 1;
//                    steal[money.length - 1] = 1;
//                }
//            }
//        }
//        if (num == money.length - 1) {
//            if (steal[num] == 1 || steal[num - 1] == 1 || steal[0] == 1) return;
//            else {
//                if (money[num] >= money[num - 1] + money[0]) {
//                    steal[num] = 1;
//                } else {
//                    steal[num - 1] = 1;
//                    steal[0] = 1;
//                }
//            }
//        } else {
//            if (steal[num] == 1 || steal[num + 1] == 1 || steal[num - 1] == 1) {
//                return;
//            } else {
//                if (money[num] >= money[num + 1] + money[num - 1]) {
//                    steal[num] = 1;
//                } else {
//                    steal[num + 1] = 1;
//                    steal[num - 1] = 1;
//                }
//            }
//        }
//    }
//}


