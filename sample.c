#include <stdio.h>
#include <string.h>

void my_print(char *str)
{

    printf("my print %s \n", str);
}

int add1(int num)
{
    return num + 1;
}

void add2(int *num)
{
    *num += 1;
}

void reverse_string(char *str)
{
    int i;
    int len = strlen(str);
    for (i = 0; i < len / 2; i++)
    {
        char temp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = temp;
    }
}
