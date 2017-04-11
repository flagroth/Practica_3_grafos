from github import Github
import networkx as nx
from networkx_viewer import Viewer
from networkx.readwrite import json_graph
import json


def get_followers(followers, visited, pending):
    user=pending.pop(0)
    print(user)
    visited.append(user)      
    if len(visited)>20:
        return
    try:
        for f in g.get_user(user).get_followers():
            followers.append((user,f.login))
#            print(f.login)
            if f.login not in visited:
                pending.append(f.login)
    except :
        return -1
    get_followers(followers, visited, pending)
    

if	__name__ == "__main__":
    # First create a Github instance:
    g = Github("flagroth","")
    visited=[]
    pending=["adamtheturtle"]
    followers=[]
    get_followers(followers, visited, pending)
    graph = nx.DiGraph()
    graph.add_edges_from(followers)

    # print(graph.edges())
    # print(graph.nodes())

    data = json_graph.node_link_data(graph)

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
        outfile.flush()
        outfile.close()

    # app = Viewer(graph)
    # app.mainloop()
    #
    
