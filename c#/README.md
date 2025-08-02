# Core .NET & C# Questions

## Beginner to Intermediate

### 1. What is the .NET Framework and how does it work

The .NET Framework is a suite of tools used for software development in the Microsoft Ecosystem. This includes
frontend focused technologies such as Blazor or MVC, web services with ASP and backend services.

### 2. What is the difference between .NET Framework, .NET Core, and .NET 5/6/7/8+

.NET Framework predates the other tech, allowed development on windows based machines.

.NET Core expanded development to non-windows based machines such as Linux, which allowed hosting in platforms such as Azure or AWS

.NET 5/6/7/8 ...

### 3. Explain the difference between value types and reference types in C#

Value types hold the actual value of a data type, whereas reference types hold a memory address which could go to another reference type or the actual value.
Holding a reference can be advantageous because it can smaller than replicating large values.

### 4. What is the purpose of the using statement in C#

the using keyword defines a scope of which an objects life time is guaranteed to be ended at the end of it, it prevents the object sticking around
which could lately cause the machine to run out of memory

### 5. What is garbage collection and how does it work in .NET

Garbage collection identifies and removes objects from memory that no longer need to be there. In .NET the process ...

### 6. What are assemblies and namespaces

Assemblies are compiled .NET programs that can be imported or deployed as services
namespaces define a scope for a given program, they usually contain many classes used to build the program

### 7. What is the difference between == and .Equals in C#

.Equals checks that two objects are the same, whilst == is used to check whether two value types are the same

## Advanced

### 8. Explain the role of the CLR (Common Language Runtime)

### 9. What are delegates and events in C#? How do you use them?

### 10. What is reflection in .NET and when would you use it?

### 11. What are async/await in C# and how do they improve performance

Async/Await tells your program to free up the current thread whilst it waits for input from a service which could take a long amount of time to come back with data. This
speeds up your program as the thread is free to do other tasks whilst it waits.

### 12. What is the difference between IEnumerable, IQueryable, List<T>?

### 13. Explain boxing and unboxing

### 14. How does dependency injection work in .NET Core

## OOP & Design Patterns

### 1. What are the four pillars of OOP?

### 2. Can you explain SOLID principles?

### 3. Whats the difference between an interface and an abstract class?

### 4. What are some design patterns you've used (e.g. Singleton, Factory, Repository)?

### 5. How do you implement the Repository and Unit of Work patterns?

## ASP.NET & Web Development

### 1. What is the difference between ASP.NET MVC and ASP.NET Web API?

### 2. How does routing work in ASP.NET Core?

### 3. What is middleware in ASP.NET Core?

### 4. How do you handle authentication and authorization in ASP.NET Core?

### 5. What are Tag helpers and View Components?

## Database & Entity Framework

### 1. What is Entity Framework (EF)?

### 2. What is the difference between EF Core and EF 6?

### 3. What are the different ways to query data in EF Core?

### 4. What is lazy loading vs eager loading vs explicit loading?

### 5. How do you handle migrations in EF Core?

## Testing & Best Practices

### 1. How do you write unit tests in .NET?

Typically you have a unit test project alongside the main project, which you then import and test against.

### 2. What is the difference between unit testing and integration testing?

Unit testing usually involves testing only one class, whilst integration tests multiple classes and how they work together

### 3. What testing frameworks do you use (e.g. xUnit, NUnit, MSTest)?

### 4. What is mocking and do you use it (e.g. with Moq)?

Mocking is when you spoof the return result to a value you want to test against, rather than doing the real action. This can be
useful when the action usually makes a request to a seperate service, mocking allows you to spoof the result without making the request.

## Devops & Tooling

### 1. How do you manage configurations in different environments?

### 2. What CI/CD tools have you used with .NET projects?

TFS, Jenkins, Gitlab

### 3. Have you used Docker with .NET applications?

### 4. How do you monitor and log a .NET Core application?

## Behavioural / Experience Questions

### 1. Tell me about a challenging bug you fixed in a .NET project

### 2. How do you stay up-to-date with .NET technologies?

### 3. Describe a project where you improved performance significantly

### 4. How do you ensure your code is maintanable and scalable
