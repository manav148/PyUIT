Rules Explained:

[ -> Set of Rules<br>
    [ -> Each Rule can have multiple test, Each test corresponds to a single url<br>
        {-> Test<br>
            "url": "https://www.google.com/", <br>
            "fields": { -> Fields to be filled in page <br>
                "q": "I am lucky"<br>
            }, <br>
            "success_string": "lucky" -> The test is successful if we find this string in the final page<br>
        }<br>
    ], <br>
    [<br>
        {<br>
            "url": "https://www.google.com/", <br>
            "fields": {<br>
                "q": "selenium" <br>
            }, <br>
            "success_string": "automation"<br>
        }<br>
    ]<br>
]<br>
