#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
// A function To convert dec to bin (declaration)
int decTo_bin_or_oct(int dec);
void fileToBin();
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
    FILE *text_file;
    FILE *new_file;
    // Ask for the file name.
    char file_name[30];
    printf("Enter the file's name: ");
    scanf("%s", file_name);  // Correct usage without & for string arrays.
    char BinFile[45];
    sprintf(BinFile, "bin_%s", file_name);
    // Open the source file for reading.
    text_file = fopen(file_name, "r");
    if (text_file == NULL) {
        printf("FILE DOESN'T EXIST ... END PROCESSING\n");
        return;
    }
    // Open the output file for writing.
    new_file = fopen(BinFile, "w");
    if (new_file == NULL) {
        printf("Error creating output file.\n");
        fclose(text_file);
        return;
    }
    // The letters string used for converting the sum into a letter.
    char letters[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    int letters_len = (int)strlen(letters);  // Should be 62.
    int ch;  // fgetc returns an int to properly check for EOF.
    while ((ch = fgetc(text_file)) != EOF) {
        if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
            // Perform your conversion function.
            int convResult = decTo_bin_or_oct(ch);
            // Calculate the sum as described.
            int sum = (convResult / 10000) + (convResult % 10000);
            // Ensure the index is within bounds of the letters string.
            int index = sum % letters_len;
            char letter = letters[index];
            // If the character is not the escape character (ASCII 27), add a space after.
            if(ch != 27)
                fprintf(new_file, "%c", letter);
            else
                fprintf(new_file, "%c", letter);
        } else {
            // For non-letter characters, just write them as is.
            if(ch == '\n')
                fprintf(new_file, "\n");
            else
                fprintf(new_file, "%c", ch);
        }
    }
    // Close both files.
    fclose(text_file);
    fclose(new_file);
    printf("Conversion Completed ... (Result stored in: %s)\n", BinFile);
}