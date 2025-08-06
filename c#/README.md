# Core .NET & C# Questions

## Beginner to Intermediate

### 1. What is the .NET Framework and how does it work

The .NET Framework is a suite of tools used for software development in the Microsoft Ecosystem. 
This includes the compiler, the runtime and other tooling such as visual studio.
This includes frontend focused technologies such as Blazor or MVC, web services with ASP and
backend services.
It is a legacy product of .NET
The LTS version is .NET Framework 4.8

### 2. What is the difference between .NET Framework, .NET Core, and .NET 5/6/7/8+

.NET Framework predates the other tech, allowed development on windows based machines.

.NET Core expanded development to non-windows based machines such as Linux, which 
allowed hosting in platforms such as Azure or AWS. The LTS version is .NET Core 3.1

.NET 5/6/7/8 merged .NET Core and .NET Framework, Xamarin, Mono as one unified platform called simply .NET. The latest LTS ones are .NET 6 and .NET 8


### 3. Explain the difference between value types and reference types in C#

Value types hold the actual value of a data type, whereas reference types hold a memory address which could go to another reference type or the actual value. Holding a reference can be advantageous because it can smaller than replicating large values.

### 4. What is the purpose of the using statement in C#

The using keyword defines a scope of which an objects life time is guaranteed to be ended 
once the scope is left. It prevents the object sticking around which could lately cause 
the machine to run out of memory

### 5. What is garbage collection and how does it work in .NET

Garbage collection identifies and removes objects from memory that no longer need to be there.It runs whenever the CLR determines it can run GC. The CLR has a managed heap of memory, where it divides object into generations. Generation 0 is for short-lived objects, Gen 1 for objects that survived Gen 0 GC, and Generation 2 is for long lived data such as static data or large collections. The CLR runs Gen 0 garbage collection the most frequently on the assumption that most newly created objects are short-lived.

It uses a Mark-and-Compact algorithm to identify all live objects starting from GC roots, it dthen sweeps and compacts all unused and dead objects and compacts live and still used objects to save space. It then updates all references of the updated objects through GC. 

Objects can have a finalizer function or by implementing the IDisposable interface. This is defined by a ~ method with the same name as the class. The code within this is ran when GC is about to remove it from memory. It can be used to manually close any connections to files or databases that have been created prior.

### 6. What are assemblies and namespaces

Assemblies are compiled .NET programs that can be imported or deployed as services. Usually compiled to a .dll or .exe file. It holds compiled types, metadata and resources. The compiled code is in intermediate language code.

namespaces define a scope for a given program, they usually contain many classes used to build the program. Can be seen as a label for a group of code. They are not tied to physical files or assemblies, just a concept within code.

### 7. What is the difference between == and .Equals in C#

.Equals checks that two reference types have the same value, whilst == is used to check whether two value types are the same or two references are the same, not the value within the reference

## Advanced

### 8. Explain the role of the CLR (Common Language Runtime)

The common-language runtime is the core execution engine of .NET, it runs .NET applications. It handles memory, threads, type safety and garbage collection. It does JIT compilation, Garbage collection, thread management and exception handling. 

It consumes compiled c# / vb.net, f# code (IL code) from the compiler, and executes it as native machine code 

C# -> IL -> CLR -> Native code -> CPU

### 9. What are delegates and events in C#? How do you use them?

### 10. What is reflection in .NET and when would you use it?

### 11. What are async/await in C# and how do they improve performance

Async/Await tells your program to free up the current thread whilst it waits for input from a service which could take a long amount of time to come back with data. This
speeds up your program as the thread is free to do other tasks whilst it waits.

### 12. What is the difference between IEnumerable, IQueryable, List<T>?

IEnumerable is used on in-memory data as an interface allowing looping over and LINQ
Queries against it

IQueryable extends IEnumerable, allows querying over data-sources such as databases

List<T> implements IEnumerable, it allows indexing and doesn't defer exection like IEnumerable. a concrete resizable collection, unlike IEnumerable's by themselves. It executes immediately
which is therefore less performant than IEnumerables, as they ensure they are only executed when neccessary.

### 13. Explain boxing and unboxing

boxing is the process of converting a value type into a object

e.g. 

```
int number = 42;
object boxed = number; // boxing
```

unboxing is the process of converting an object into a value type
implicit, lose information
e.g.

```
object boxed = 42;
int number = (int)boxed; // unboxing
```
explicit, gain information/more restrictive as to what type the 'number' variable is

### 14. How does dependency injection work in .NET Core

Depedency injeciton became built into the ecosystem, treated as a first-class feature
You register services via an interface and an implementation of that interface
into the DI Container

``` builder.services.AddTransient<IMessageService, EmailService>();```
- transient = new instance everyime
- scoped = one instance per request, 
- singleton = one instance per application lifetime

Then can inject the service into the constructor of other objects
and its handled by .NET to supply it via the DI Container, it resolves
it automatically

.NET Core has the Microsoft.Extensions.DependencyInjection package by default

## OOP & Design Patterns

### 1. What are the four pillars of OOP?

- Encapsulation, bundling all releated fields and methods into a cohesive class. It promotes hiding uncessary data from classes that use it, making it more simple to use.

- Abstraction, deriving classes from interfaces or abstract classes, promoting code reuse and hiding implementation details

- Inheritance, inheriting code from a base class, promoting code reuse

- Polymorphism, the ability of many different types to be used from the same interface for different purposes.

### 2. Can you explain SOLID principles?

- Single Responsibility Principle, a class should have only one reason to change. Each class should do one thing well

- Open/Closed principle, software entities should be open to extension, but closed for modification. i.e. don't change code that is being used already, but additional code but be added to enhance the original class if required

- Liskov Substition Principle, subtypes must be substitutable for their base types.

- Interface Segragation, clients should not be forced to depend on interfaces they do not use

- Dependency Inversion, depend on abstractions, not concrete implementaions. High-level modules should not depend on low-level modules

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

## Extra

### 1. What is nuget

### 2. What is the minimal hosting model

it is a simplified way to build ASP.NET Core apps in .NET 6 in a Program.cs file. It removes a lot of boilerplate

