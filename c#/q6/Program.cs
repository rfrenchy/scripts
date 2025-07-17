/**
Q.6: How to remove duplicate characters from a string?
Ans.: The user will input a string and the method should remove multiple occurrences of characters in the string

input: csharpcorner, output: csharpone
*/

// Get env input
string[] cli_args = Environment.GetCommandLineArgs();
string input = cli_args[1];

// Get single occurences of a char
List<char> occurrenced = [];
for (int i = 0; i < input.Length; i++)
{
    if (occurrenced.Where(x => x == input[i]).Any())
        occurrenced.Add(input[i]);
}

// print output
string word = "";
foreach (char c in occurrenced)
    word += c;

Console.WriteLine(word);