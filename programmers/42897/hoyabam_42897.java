public static void main(String[] args) {
    int[] money = {5, 2, 3, 6, 5, 2, 20};
    int answer;

    int[] a = new int[money.length];
    a[0] = money[0];
    a[1] = Math.max(money[0], money[1]);

    int[] b = new int[money.length];
    b[0] = money[1];
    b[1] = Math.max(money[1], money[2]);

    for (int i = 2; i < money.length - 1; i++) {
        a[i] = Math.max(a[i - 1], money[i] + a[i - 2]);
        b[i] = Math.max(b[i - 1], money[i + 1] + b[i - 2]);
    }

    answer = Math.max(a[a.length - 2], b[b.length - 2]);
    System.out.println(answer);
}