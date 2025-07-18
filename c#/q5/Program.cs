/**
    Q.5: How to count the occurrence of each character in a string?
Ans.: The user will input a string and we need to find the count of each character of the string and display it on console. We won’t be counting space character.

input: hello world;
output: 

h – 1

e – 1

l – 3

o – 2

w – 1

r – 1

d – 1
*/

// get env input
string[] cli_args = Environment.GetCommandLineArgs();
string input = cli_args[1];

// find character counts
Dictionary<char, int> character_counts = [];
for (int i = 0; i < input.Length; i++)
{
    if (input[i] == ' ')
        continue;

    // to lower case, i.e. w and W treated the same when found
    char input_lower = input[i].ToString().ToLower().ToCharArray()[0];

    if (character_counts.TryGetValue(input_lower, out int value))
        character_counts[input_lower] = ++value;
    else
        character_counts[input_lower] = 1;
}

// print
foreach (var key in character_counts.Keys)
    Console.WriteLine(key + " - " + character_counts[key]);   


