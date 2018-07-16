// A perfect number is a number for which the sum of its proper divisors is
// exactly equal to the number. For example, the sum of the proper divisors of
// 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
//
// A number n is called deficient if the sum of its proper divisors is less
// than n and it is called abundant if this sum exceeds n.
//
// As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
// number that can be written as the sum of two abundant numbers is 24. By
// mathematical analysis, it can be shown that all integers greater than 28123
// can be written as the sum of two abundant numbers. However, this upper
// limit cannot be reduced any further by analysis even though it is known that
// the greatest number that cannot be expressed as the sum of two abundant
// numbers is less than this limit.
//
// Find the sum of all the positive integers which cannot be written as the sum
// of two abundant numbers.

public class P023 {
    public static void main(String args[]) {
        System.out.println(new P023().sum());
    }

    static int LIMIT = 28123;
    boolean[] isAbundant = new boolean[LIMIT];

    int sum() {
        int sum = 0;
        // Save the result of isAbundant() to the array isAbundant[], avoid
        // recalculation of isAbundant
        for (int i = 1; i < isAbundant.length; i++) {
            isAbundant[i] = isAbundant(i);
        }

        for (int i = 1; i < LIMIT; i++) {
            if (!isSumOf2Abundants(i)) {
                sum += i;
            }
        }
        return sum;
    }

    boolean isSumOf2Abundants(int n) {
        for (int i = 1; i <= n / 2; i++) {
            if (isAbundant[i] && isAbundant[n - i]) {
                return true;
            }
        }
        return false;
    }

    boolean isAbundant(int n) {
        int sum = 1;
        int end = (int) Math.floor(Math.sqrt(n));

        for (int i = 2; i <= end; i++) {
            if (n % i == 0) {
                sum += i + n / i;
            }
        }
        if (Math.sqrt(n) == end) {
            sum -= end;
        }
        return sum > n;
    }
}
