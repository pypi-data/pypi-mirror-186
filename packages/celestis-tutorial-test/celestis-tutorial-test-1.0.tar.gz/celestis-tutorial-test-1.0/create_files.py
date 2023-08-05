import os

urls_content = '''
# Include your urls in this file
'''

views_content = '''
# Include your views in this file
'''

server_content = ''

def create_project_files(project_name):
    os.makedirs(project_name, exist_ok=True)
    
    urls_path = os.path.join(project_name, "urls.py")
    with open(urls_path, "w") as f:
        f.write(urls_content)

    views_path = os.path.join(project_name, "views.py")
    with open(views_path, "w") as f:
        f.write(views_content)
    
    server_path = os.path.join(project_name, "server.py")
    with open(server_path, "w") as f:
        f.write(server_content)