from github import Github
import networkx as nx
from networkx_viewer import Viewer
    


def get_followers(user, followers, visited, pending):
    visited.append(user)      
    if len(visited)>20:
        return
    try:
        for f in g.get_user(user).get_followers():
            followers.append((user,f.login))
            print(f.login)
            if f.login not in visited:
                pending.append(f.login)
    except :
        return -1
    user=pending.pop(0)
    get_followers(user, followers, visited, pending)
    

# First create a Github instance:
    
if	__name__	==	"__main__":
    g = Github("flagroth","")    
    visited=[]
    pending=[]
    followers=[]
    get_followers("adamtheturtle", followers, visited, pending)
    graph = nx.DiGraph()
    graph.add_edges_from(followers)
    app = Viewer(graph)
    app.mainloop()    
    
    
