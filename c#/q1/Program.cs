namespace Questions;

// https://ankitsharmablogs.com/csharp-coding-questions-for-technical-interviews/
public static class Questions
{
    public static void Main(string[] args)
    { }

    /**
        How to reverse a string?
        Ans.: The user will input a string and the method should return the reverse of that string
    */
    public static string Q1(string input)
    {
        string output = "";

        for (int i = input.Length; i > 0; i--)
        {
            output += input[i - 1];
        }

        return output;
    }
    /**
        How to find if the given string is a palindrome or not?
        Ans.: The user will input a string and we need to print “Palindrome” or “Not Palindrome”
             based on whether the input string is a palindrome or not.
    */
    public static string Q2(string input)
    {
        int i = 0;
        bool palindrome = true;

        for (int j = input.Length - 1; j >= 0; j--)
        {
            if (input[j] != input[i])
            {
                palindrome = false;
                break;
            }
            i++;
        }

        if (palindrome)
            return "Palindrome";

        return "Not Palindrome";
    }

    /**
        How to reverse the order of words in a given string?
        Ans.: The user will input a sentence and we need to reverse the sequence of words in the sentence.
    */
    public static string Q3(string input)
    {
        string[] words = input.Split(" ");

        string reversed_input = "";

        for (int i = words.Length - 1; i >= 0; i--)
            reversed_input += words[i] + " ";

        return reversed_input.Trim();
    }

    /**
        How to reverse each word in a given string?
        Ans.: The user will input a sentence and we need to reverse each word 
            individually without changing its position in the sentence.
    */
    public static string Q4(string input)
    {
        string[] words = input.Split(" ");
        string reversed_words = "";

        for (int i = 0; i < words.Length; i++)
        {
            string word = words[i];

            for (int j = word.Length - 1; j >= 0; j--)
                reversed_words += word[j];

            reversed_words += " ";
        }

        return reversed_words.Trim();
    }

    /**
         How to count the occurrence of each character in a string?
         Ans.: The user will input a string and we need to find the count of each character 
             of the string and display it on console. We won’t be counting space character.
    */
    public static Dictionary<char, int> Q5(string input)
    {
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

        return character_counts;
    }

    /**
        How to remove duplicate characters from a string?
        Ans.: The user will input a string and the method should remove 
            multiple occurrences of characters in the string
    */
    public static string Q6(string input)
    { 
        // Get single occurences of a char
        List<char> occurrenced = [];
        for (int i = 0; i < input.Length; i++)
        {
            if (!occurrenced.Where(x => x == input[i]).Any())
                occurrenced.Add(input[i]);
        }

        return string.Concat(occurrenced.Select(x => x));
    }
}




