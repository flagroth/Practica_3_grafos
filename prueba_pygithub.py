from github import Github
import networkx as nx
from networkx_viewer import Viewer
from networkx.readwrite import json_graph
import json
import sys

def get_followers(followers, visited, pending):
    user=pending.pop(0)
    try:
        for f in g.get_user(user).get_followers():
            followers.append((user,f.login))
#            print(f.login)
            if len(visited) < 0 and f.login not in visited:
                pending.append(f.login)
    except :
        print("Excepción")
        return -1
    visited.append(user)
    if len(pending)>0:
        get_followers(followers, visited, pending)
    else:
        return 0
    

if	__name__ == "__main__":
    # First create a Github instance:
    if len(sys.argv)<2:
        exit("usage: python prueba_pygithub.py <usuario>")
    g = Github("flagroth","6igavdkE#")
    visited=[]
    pending=[]
    followers=[]
    languages=[]
    programs=[]
    repos=[]
    contributed=[]

    initial=str(sys.argv[1])

    pending.append(initial)

    get_followers(followers, visited, pending)
    graph = nx.DiGraph()
    graph.add_edges_from(followers, type='users')

    node=1
    for u in graph.nodes():
        graph.node[u]['type']='user'
        print("Users=[" + str(node) + "/" + str(len(graph.nodes())) + "]")
        for repo in g.get_user(u).get_repos():
            repos.append(repo.name)
            languages.append(repo.language)
            programs.append((repo.name,repo.language))
            contributed.append((u,repo.name))
        node=node+1

    languages=list(set(languages))
    repos=list(set(repos))
    # print(languages)

    graph.add_nodes_from(languages, type='language')
    graph.add_nodes_from(repos, type='repo')
    graph.add_edges_from(contributed)
    graph.add_edges_from(programs)

    # print(graph.edges())
    # print(graph.nodes())

    data = json_graph.node_link_data(graph)

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
        outfile.flush()
        outfile.close()

    # app = Viewer(graph)
    # app.mainloop()
    
