from flask import Flask
from jira import JIRA
username = 'vasundhara.chauhan@innovaccer.com'
password = 'Innovaccer@123'
jira = JIRA(basic_auth=(username, password), options = {'server': 'https://support.innovaccer.com/'})
projects = jira.projects()

app = Flask(__name__)

@app.route('/hello')
def helloIndex():
    #print(projects)
    #jra = jira.project('MER')
    #print(jra.name)                
    #print(jra.lead.displayName)
    '''key='INT'
    jira.create_project(key, name='INTEGER', assignee='daksh.singhal@innovaccer.com', type='Software', 
    	template_name=None)'''
    data = request.get_json()
    print(data)
    return "hello"

app.run()
