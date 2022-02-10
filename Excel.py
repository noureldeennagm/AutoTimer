from json2excel import Json2Excel

if __name__ == '__main__':
    json2excel = Json2Excel(head_name_cols=["name"])
    # print(json2excel.run('./test.json'))

    jsons = [
        
           {
                    "name": "C:\\Windows\\system32\\cmd.exe - python  autotimer.py",
            
                    "minutes": 1,
                
            },
            { 
                    "name": "Anaconda Navigator",
            
                    "minutes": 5 ,
            },
            { 
                    "name": "Netflix",
            
                    "minutes": 32,
                    
             },
            {            
                    "name": "youtube.com",
            
                    "minutes": 12,
                    
            },
            {       
                    "name": "codingdiksha.com",
            
                    "minutes": 3,
                    
             },
            {                    
                    "name": "instagram.com",
           
                    "minutes": 1,
                    
           
              },
            {                   
                    "name": "moodle.rwth-aachen.de",
            
                    "minutes": 1,
                  
             },
            {                   
                    "name": "facebook.com",
           
                    "minutes": 4,
                  
             },
            {                    
                    "name": "Slack | tower crane",
           
                    "minutes": 7,
                    
                },
            {                
                    "name": "Snipping Tool",
            
                    "minutes": 1,
                   
             },
            {                   
                    "name": "2021_WiSe_DDP_final_submission_Nagm_Leitner.pptx - PowerPoint",
            
                    "minutes": 45,

            },
            {                    
                    "name": "AutoTimer",
                    "minutes": 1,
            },
           
    ]
    print(json2excel.run(jsons))