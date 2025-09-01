public static void main(String[] args) {
    int n = 4;
    int[] tops = {1, 1, 0, 1};

    System.out.println("최종값 : " + fibonacci(n, tops));
}

public static int fibonacci(int n, int[] tops) {
    int cur = 2 * n + 2;
    int a = 0, b = 1, z = 0;
    for (int i = 2; i <= cur; i++) {
        if (i % 2 == 1) {
            if (tops[z] == 1) {
                int temp = a + b * 2;
                a = b;
                b = temp % 10007;
                z++;
                continue;
            }
            z++;
        }
        int temp = a + b;
        a = b;
        b = temp % 10007;
    }
    return b % 10007;
}