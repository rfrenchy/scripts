# get .net SDK docker image image
FROM mcr.microsoft.com/dotnet/sdk:6.0 as build
WORKDIR /app

# restore project
COPY *.csproj ./
RUN dotnet restore

# build release
COPY . ./
RUN dotnet publish -c Release -o out

# copy release build
FROM mcr.microsoft.com/dotnet/aspnet:6.00 AS runtime
WORKDIR /app
COPY --from=build /app/out ./

# expose app port
EXPOSE 80

# define entrypoint
ENTRYPOINT ["dotnet", "q1.dll"]

