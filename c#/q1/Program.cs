// See https://aka.ms/new-console-template for more information

/**
Q.1: How to reverse a string?
Ans.: The user will input a string and the method should return the reverse of that string

input: hello, output: olleh
input: hello world, output: dlrow olleh

*/

string[] cli_args = Environment.GetCommandLineArgs();

if (cli_args.Length > 1)
{
    string input = cli_args[1];
    string output = "";
    
    for (int i = input.Length; i > 0; i--)
    {
        output += input[i - 1];
    }

    Console.WriteLine(output);
}
public class Questions
{
    public string Q1(string input)
    {
        string output = "";

        for (int i = input.Length; i > 0; i--)
        {
            output += input[i - 1];
        }

        return output;
    }
}





