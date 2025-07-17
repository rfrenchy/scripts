/**
Q.4: How to reverse each word in a given string?
Ans.: The user will input a sentence and we need to reverse each word individually without changing its position in the sentence.

input: Welcome to Csharp corner, output: emocleW ot prahsC renroc

https://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/

*/

string[] cli_args = Environment.GetCommandLineArgs();
string input = cli_args[1];

string[] words = input.Split(" ");
string reversed_words = "";

for (int i = 0; i < words.Length; i++)
{
    string word = words[i];

    for (int j = word.Length - 1; j >= 0; j--)
    {
        reversed_words += word[j];
    }

    reversed_words += " ";
}

Console.WriteLine(reversed_words);
