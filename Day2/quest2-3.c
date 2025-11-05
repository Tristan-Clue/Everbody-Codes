#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

typedef struct comp
{
	long	x;
	long	y;
}			t_comp;


int	main(int argc, char **argv)
{
	char	array[1001][1001];
	t_comp	num;
	t_comp	sub;
	t_comp	temp;
	t_comp	subtemp;
	int		i;
	int		j;
	int		iteration;
	int		count;

	(void)argc;
	memset(array, '*', sizeof(array));
	sub.x = atoi(argv[1]);
	sub.y = atoi(argv[2]);
	count = 0;
	i = 0;
	while (i < 1001)
	{
		j = 0;
		subtemp.y = sub.y + (i);
		while (j < 1001)
		{
			iteration = 0;
			num.x = 0;
			num.y = 0;
			subtemp.x = sub.x + (j);
			while (iteration < 100)
			{
				temp.x = num.x;
				temp.y = num.y;
				num.x = ((temp.x * temp.x) - (temp.y * temp.y));
				num.y = ((temp.x * temp.y) + (temp.y * temp.x));
				num.x /= 100000;
				num.y /= 100000;
				num.x += subtemp.x;
				num.y += subtemp.y;
				iteration += 1;
				if (num.x > 1000000 || num.x < -1000000
		   			|| num.y > 1000000 || num.y < -1000000)
				{	
					iteration = -1;
					break;
				}
			}
			if (iteration == 100)
			{
				array[i][j] = '@';
				count += 1;
			}
			j += 1;
		}
		i += 1;
	}
/*
	i = 0;
	while (i < 101)
	{
		j = 0;
		while (j < 101)
		{
			printf("%c", array[i][j]);
			j++;
		}
		printf("\n");
		i++;
	}
*/
	printf("%d\n", count);
}
