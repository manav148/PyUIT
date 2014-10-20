Rules Explained:
```
[ // <b>Set of Rules</b>
    [ // <b>Each Rule can have multiple test, Each test corresponds to a single url</b>
        {// <b>Test</b>
            "url": "https://www.google.com/", 
            "fields": { // <b>Fields to be filled in page </b>
                "q": "I am lucky"
            }, 
            "success_string": "lucky" // <b>The test is successful if we find this string in the final page</b>
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