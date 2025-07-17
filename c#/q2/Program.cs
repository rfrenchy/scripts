/**
: How to find if the given string is a palindrome or not?
Ans.: The user will input a string and we need to print “Palindrome” or “Not Palindrome” based on whether the input string is a palindrome or not.

input: madam, output: Palindrome
input: step on no pets, output: Palindrome
input: book, output: Not Palindrome
if we pass an integer as a string parameter then also this method will give the correct output

input: 1221, output: Palindrome

*/

string[] cli_args = Environment.GetCommandLineArgs();

string input = cli_args[1];

int i = 0;
bool palindrome = true;
for (int j = input.Length-1; j >= 0;  j--) {
    if (input[j] != input[i])
    {
        palindrome = false;
        break;
    }
    i++;
}

if (palindrome) {
    Console.WriteLine("Palindrome");
} else {
    Console.WriteLine("Not Palindrome");
}