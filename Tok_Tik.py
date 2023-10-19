def main():

    n = int(input())
    views = {}
    view_calc(views, n)

    most_popular_tikker = max(views, key=views.get)
    
    print(most_popular_tikker)

def view_calc(views, n):
    for _ in range(n):
        s, a = input().split()  
        a = int(a)  
        if s in views:
            views[s] += a
        else:
            views[s] = a

main()