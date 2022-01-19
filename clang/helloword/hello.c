#include <stdio.h>

int my_power(int base, int exp);
int main(void)
{
	int res;
	res = my_power(2, 10);
	printf("%d\n", res);

	return 0;
};

int my_power(int base, int exp) // 밑수와 지수를 매개변수로 저장
{
	int res = 1;
	int i;

	for (i = 0; i < exp; i++)
	{
		res *= base;
	}

	return res;
}