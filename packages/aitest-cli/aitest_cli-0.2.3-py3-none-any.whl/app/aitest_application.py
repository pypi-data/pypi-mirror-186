from datetime import *
import click
import os
import requests
import json
from sys import *
import base64
from prettytable import PrettyTable



# Command Group
@click.group(name='configure')
def configure():
    pass

# Creating command 
@configure.command(name='configure')
def configure():
    """If this command is run with no arguments, you will be prompted for configuration values such as your User ID, Client ID and Client Secret ID.If your configure file does not  exist
       (the default location is ~/.aitest/configure), the aitest CLI will create it for you.To keep an existing value, hit enter when prompted for the value.

       To save the configurations , you can run below command:\n
       aitest configure
              
    """
    user_id = input('Enter aiTest User Identifier :')
    client_id = input('Enter Client ID :')
    client_secret_id = input('Enter Client Secret ID :')


    folder_path =os.path.join( os.path.expanduser('~'),".aitest" )
    folder_exist = os.path.exists(folder_path)
    if not folder_exist:
        os.mkdir(folder_path)
        fd = open(os.path.join(folder_path, "configure"), 'w')

        if user_id:
            fd.write("user_id = "+user_id+"\n")
        else:
            fd.write("user_id = "+" "+"\n")
            
        if client_id:
            fd.write("client_id = "+client_id+"\n")
        else:
            fd.write("client_id = "+" "+"\n")

        if client_secret_id:
            fd.write("client_secret_id = "+client_secret_id+"\n")
        else:
            fd.write("client_secret_id = "+" "+"\n")
        fd.close()
    else:
        file_path =os.path.join( os.path.expanduser('~'),".aitest","configure" )
        file = open(file_path,"r")
        content = file.read()
        data = content.split("\n")
        ex_user_id = data[0].split(" = ")[1]
        ex_client_id = data[1].split(" = ")[1]
        ex_client_secret_id=data[2].split(" = ")[1]

        fd = open(os.path.join(folder_path, "configure"), 'w')
        if user_id:
            fd.write("user_id = "+user_id+"\n")
        else:
            fd.write("user_id = "+ex_user_id+"\n")
            
        if client_id:
            fd.write("client_id = "+client_id+"\n")
        else:
            fd.write("client_id = "+ex_client_id+"\n")

        if client_secret_id:
            fd.write("client_secret_id = "+client_secret_id+"\n")
        else:
            fd.write("client_secret_id = "+ex_client_secret_id+"\n")
        fd.close()

# Command Group  
@click.group(name='run')
def run():
    pass

# Creating command
@run.command(name='run')
@click.option('--testrun_id','-id', required=True)
@click.option('--wait_time','-w', default=30, required=False)
@click.option('--git_pass','-p', required=False)
def run(testrun_id, git_pass, wait_time):
    """If this command is run with testrun id as an argument, aitest CLI will create new test for you with same configuration of provided testrun id.Enter git password with -p only if you used git url of the automation code for creating the test otherwise no need to enter git password.
       Enter the waiting time in minutes with -w as an argument, To wait for looking the testrun status in given time.\n
       To re-run the test, you can run below command:\n
       aitest run -id [testrun id] -p [git password] -w [wait_time]
    """    
    try: 
        if os.environ["USER_ID"] and os.environ["CLIENT_ID"] and os.environ["CLIENT_SECRET_ID"]:
            user_id = os.environ["USER_ID"]
            client_id = os.environ["CLIENT_ID"]
            client_secret_id=os.environ["CLIENT_SECRET_ID"]
        else:     
            file_path =os.path.join( os.path.expanduser('~'),".aitest","configure" )
            file = open(file_path,"r")
            content = file.read()
            data = content.split("\n")
            user_id = data[0].split(" = ")[1]
            client_id = data[1].split(" = ")[1]
            client_secret_id=data[2].split(" = ")[1]
    except:
        click.echo('\n"error" : "Please add your valid USER_ID, CLIENT_ID and CLIENT_SECRET_ID in configure file."\n')
        exit()

    str_to_encode = client_id + ":" + client_secret_id

    encoded_str = base64.b64encode(str_to_encode.encode('utf-8'))

    encoded_value = encoded_str.decode('utf-8')

    access_token_api_headers = {"Authorization":f"Basic {encoded_value}", "content-type": "application/x-www-form-urlencoded"}
   
    access_token_api = "https://login-marxeed-dev.auth.us-east-1.amazoncognito.com/oauth2/token"


    data = { 'grant_type': 'client_credentials', 'scope': 'aitestpublic/runtest' }


    token = requests.post(access_token_api,headers=access_token_api_headers,data=data)
    if token.status_code==400:
        click.echo('\n"error" : "Please add your valid Client ID and Client Secret ID ."\n')
        exit()

        
    else:
        token_data = token.json()

    access_token=token_data["access_token"]
  
    headers = {"Authorization": f"Bearer {access_token}", "aiTest-User-Identifier":user_id}

    base_url = "https://api.aitest.dev.appliedaiconsulting.com/public/v1/testrun/load_test"

    dd = {"testrun_id":testrun_id, "git_password":git_pass}
    
    payload=json.dumps(dd)
   

    res2 =requests.post(base_url,data=payload,headers=headers)
    if res2.status_code==401:
        click.echo('\n"error" : "Please add your valid User ID."\n')
        exit()
    if res2.status_code==200:
        res_body=res2.json() 
        test_data=json.loads(res_body['body'])
        click.echo(f"\nTest created successfully\nTest Name : {test_data['load_test_details']['testrun_name']}\nTestrun ID : {test_data['load_test_details']['testrun_id']}\n")
        click.echo("Testrun is in progress, result will be displayed once it get completed.")
        new_time = datetime.now() +timedelta(minutes=int(wait_time))
        test_status=""
        while test_status!="completed":
            if (new_time.strftime("%H:%M:%S"))==(datetime.now().strftime("%H:%M:%S")):
                click.echo(f"The request is timed out. The testrun is still in progress. To see the status of the testrun, please run command : [ aitest status {test_data['load_test_details']['testrun_id']} ].")
                exit()
            base_url = f"https://api.aitest.dev.appliedaiconsulting.com/public/v1/testrun_result/status/{test_data['load_test_details']['testrun_id']}"
            status_res =requests.get(base_url,headers=headers)
            status_test_data=status_res.json()
            body=json.loads(status_test_data['body'])
            test_status = body['testrun_status'] 
            if test_status=="completed":
                testrun_status_details=body['testrun_status_details']
                table = PrettyTable(["browser_name", "browser_version","test run result id", "status", "time taken"])
                click.echo(f"\ntest status : {test_status}\n")
                for i in testrun_status_details:
                    table.add_row([i['browser_name'],i['browser_version'],i['testrun_result_id'],i['testrun_result_status'],i['time_taken']])
                click.echo(table)            
        return 1
    else:
        click.echo(res2.json())
        return 0

# Command Group 
@click.group(name='status')
def status():
    """ status command is use to display the status of particular test.  """
    pass

# Creating command
@status.command(name='status')
@click.option('--testrun_id','-id', required=True)
def status(testrun_id):
    """ If this command is run with testrun id as an argument, aitest CLI will display the test details .\n  
        To see the status of test , you can run below command:\n
        aitest status -id [testrun_id]
    """
    try: 
        if os.environ["USER_ID"] and os.environ["CLIENT_ID"] and os.environ["CLIENT_SECRET_ID"]:
            user_id = os.environ["USER_ID"]
            client_id = os.environ["CLIENT_ID"]
            client_secret_id=os.environ["CLIENT_SECRET_ID"]
        else:     
            file_path =os.path.join( os.path.expanduser('~'),".aitest","configure" )
            file = open(file_path,"r")
            content = file.read()
            data = content.split("\n")
            user_id = data[0].split(" = ")[1]
            client_id = data[1].split(" = ")[1]
            client_secret_id=data[2].split(" = ")[1]
    except:
        click.echo('\n"error" : "Please add your valid USER_ID, CLIENT_ID and CLIENT_SECRET_ID in configure file."\n')
        exit()


    str_to_encode = client_id + ":" + client_secret_id

    encoded_str = base64.b64encode(str_to_encode.encode('utf-8'))

    encoded_value = encoded_str.decode('utf-8')

    access_token_api_headers = {"Authorization":f"Basic {encoded_value}", "content-type": "application/x-www-form-urlencoded"}
   
    access_token_api = "https://login-marxeed-dev.auth.us-east-1.amazoncognito.com/oauth2/token"


    data = { 'grant_type': 'client_credentials', 'scope': 'aitestpublic/runtest' }

    token = requests.post(access_token_api,headers=access_token_api_headers,data=data)
    if token.status_code==400:
        click.echo('\n"error" : "Please add your valid Client ID and Client Secret ID ."\n')
        exit()
    else:
        token_data = token.json()

    access_token=token_data["access_token"]

    headers = {"Authorization": f"Bearer {access_token}", "aiTest-User-Identifier":user_id}
    base_url = f"https://api.aitest.dev.appliedaiconsulting.com/public/v1/testrun_result/status/{testrun_id}"

    status_res =requests.get(base_url,headers=headers)
    if status_res.status_code==401:
        click.echo('\n"error" : "Please add your valid User ID."\n')
        exit()
    status_test_data=status_res.json()
        

    body=json.loads(status_test_data['body'])
     
    test_status = body['testrun_status'] 

    testrun_status_details=body['testrun_status_details']

    table = PrettyTable(["browser_name", "browser_version","test run result id", "status", "time taken"])

    click.echo(f"\ntest status : {test_status}\n")
    for i in testrun_status_details:
        table.add_row([i['browser_name'],i['browser_version'],i['testrun_result_id'],i['testrun_result_status'],i['time_taken']])
        # click.echo(f"   {i['browser_name']}-{i['browser_version']}    test run result id: {i['testrun_result_id']}   status: {i['testrun_result_status']}   time taken: {i['time_taken']} secs", )
   
    click.echo(table)
    