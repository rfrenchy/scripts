
/**
Q.3: How to reverse the order of words in a given string?
Ans.: The user will input a sentence and we need to reverse the sequence of words in the sentence.

input: Welcome to Csharp corner, output: corner Csharp to Welcome
*/

string[] cli_args = Environment.GetCommandLineArgs();
string input = cli_args[1];

string[] words = input.Split(" ");

Console.WriteLine(words.Length);
string reversed_input = "";

for (int i = words.Length - 1; i >= 0; i--)
{
    reversed_input += words[i] + " ";
}

Console.WriteLine(reversed_input);

