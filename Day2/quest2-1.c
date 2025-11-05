#include <stdio.h>
#include <math.h>
#include <stdlib.h>

typedef struct comp
{
	int	x;
	int	y;
}			t_comp;

int	main(int argc, char **argv)
{
	t_comp	num;
	t_comp	sub;
	t_comp	temp;
	int		i;

	(void)argc;
	num.x = 0;
	num.y = 0;
	sub.x = atoi(argv[1]);
	sub.y = atoi(argv[2]);
	i = 0;
	while (i < 5)
	{
		temp.x = num.x;
		temp.y = num.y;
		num.x = ((temp.x * temp.x) - (temp.y * temp.y));
		num.y = ((temp.x * temp.y) + (temp.y * temp.x));
		num.x /= 100000;
		num.y /= 100000;
		num.x += sub.x;
		num.y += sub.y;
		i += 1;
		printf("[%d, %d]\n", num.x, num.y);
	}
	printf("[%d, %d]\n", num.x, num.y);
}
