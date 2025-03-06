#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// A function To convert dec to bin (declaration)
int decTo_bin_or_oct(int dec);
__declspec() void fileToBin();
// main program
int main(){
    
    fileToBin();
    return 0;
}

// Definition of function 
int decTo_bin_or_oct(int dec){
    int r,p,b;
    p =1 ;
    b = 0;
    while(dec!=0){
        r = dec % 2 ;
        b = b + r * p;
        p = p * 10;
        dec = (int)dec/2;
    }
    return b;
}
// represent files in binary langauge
void fileToBin(){
    // opening a file
    FILE *text_file ;
    FILE *new_file ;
    // set reading mode 
    // Asking about the name of file :
    char file_name[30];
    printf("Enter the file's name : ") ;scanf("%s",&file_name);
    char BinFile[45];
    sprintf(BinFile,"bin_%s",file_name);
    // start reading and writing
    text_file = fopen(file_name,"r");
    if (!(text_file)){printf("FILE DOESN'T EXIST ... END PROCCESSING");}
    else{
        // start written
        new_file = fopen(BinFile,"w");
        // reading the content of the file
        char ch;
        while ((ch = fgetc(text_file)) != EOF) {
            // EOF = the char isn't an ASCII value
            int CharBin = decTo_bin_or_oct(ch+0);
            char BinStr[7];
            char space = ' ';
            itoa(CharBin,BinStr,10);
            if (ch+0 !=27){
                strncat(BinStr," ",1);
            }
            CharBin==1010 ? fprintf(new_file,"\n") : fprintf(new_file,BinStr);
        }
        // closing the file
        fclose(text_file);
        fclose(new_file);
        printf("Conversion Completed ... (Resualt stored in : %s _bin.txt)",BinFile);
    }
}