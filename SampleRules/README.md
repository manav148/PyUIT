Rules Explained:
```
[ -> UI Tests begin (List of Rules)
    [ -> Each Rule can have multiple test, Each test corresponds to a single url
        {-> Each Test is dictionary of key value pairs
            "url": "https://www.google.com/", 
            "fields": { -> Fields to be filled in page 
                "q": "I am lucky"
            }, 
            "success_string": "lucky" -> The test is successful if we find this string after filling and posting the form
        }
    ], -> Cookies are cleared after 1st rule is finished
    [ -> Rule 2 begins
        {
            "url": "https://www.google.com/", 
            "fields": {
                "q": "selenium" 
            }, 
            "success_string": "automation"
        }
    ] -> Rule 2 Ends
] -> UI Tests End
```