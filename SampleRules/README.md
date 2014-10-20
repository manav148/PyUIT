Rules Explained:
```
[ -> Set of Rules
    [ -> Each Rule can have multiple test, Each test corresponds to a single url
        {-> Test
            "url": "https://www.google.com/", 
            "fields": { -> Fields to be filled in page 
                "q": "I am lucky"
            }, 
            "success_string": "lucky" -> The test is successful if we find this string in the final page
        }
    ], 
    [
        {
            "url": "https://www.google.com/", 
            "fields": {
                "q": "selenium" 
            }, 
            "success_string": "automation"
        }
    ]
]
```