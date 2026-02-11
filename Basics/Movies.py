n=int(input("How many movies you need to store:"))
movielist=[]
for i in range(n):
    movies={}
    movies["name"]=input("Enter the movie name:")
    while True:
        rating=int(input(f"How much rating do you give for {movies['name']}:"))
        if(rating>5 or rating<0):
            print("please rate between 0 to 5")
        else:
            movies["rating"]=rating
            break

    movielist.append(movies)    
           
print("All movies stored:")
for movie in movielist:
    print(f"{movie['name']} - Rating: {movie['rating']}")
       