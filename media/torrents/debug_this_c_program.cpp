#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void reverse(char *cadena){

    size_t len = strlen(cadena);
    char *end= cadena;
    char *aux = cadena;
    while(*++end){}
    --end; //end points to a

    for(;len;--len){
        *aux++ = *end--;

    }

}

int main()
{

    char buffer[] = "hello";
    reverse(buffer);
    printf("%s",buffer);


    return 0;
}
