namespace Tests;

using Questions;

public class UnitTest1
{
    [Fact]
    public void Q1Test1()
    {
        string expected = "dlrow olleh";
        string result = Questions.Q1("hello world");

        Assert.Equal(expected, result);
    }

    [Fact]
    public void Q2Test1()
    {
        string expected = "Palindrome";
        string result = Questions.Q2("hannah");

        Assert.Equal(expected, result);
    }

    [Fact]
    public void Q2Test2()
    {
        string expected = "Not Palindrome";
        string result = Questions.Q2("hello world");

        Assert.Equal(expected, result);
    }

    [Fact]
    public void Q3Test1()
    {
        string sentence = "this is a sentence";
        string expected = "sentence a is this";
        string result = Questions.Q3(sentence);

        Assert.Equal(expected, result);
    }

    [Fact]
    public void Q4Test1()
    {
        string sentence = "this is a sentence";
        string expected = "sentence a is this";
        string result = Questions.Q3(sentence);

        Assert.Equal(expected, result);
    }

    [Fact]
    public void Q5Test1()
    {
        Dictionary<char, int> result = Questions.Q5("hello world");

        Assert.Equal(1, result['h']);
        Assert.Equal(2, result['o']);
        Assert.Equal(3, result['l']);
    }

    [Fact]
    public void Q6Test1()
    {
        string sentence = "hello world";
        string expected = "helo wrd";
        string result = Questions.Q6(sentence);

        Assert.Equal(expected, result);
    }
    
}