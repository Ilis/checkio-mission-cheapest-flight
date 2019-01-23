"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[
                ['A', 'C', 100],
                ['A', 'B', 20],
                ['B', 'C', 50]
            ], 'A', 'C'],
            "answer": 70,
            "explanation": "A->B(20)->C(50)"
        },
        {
            "input": [[
                ['A', 'C', 100],
                ['A', 'B', 20],
                ['B', 'C', 50]
            ], 'C', 'A'],
            "answer": 70,
            "explanation": "C->B(50)->A(20)"
        },
        {
            "input": [[
                ['A', 'C', 40],
                ['A', 'B', 20],
                ['A', 'D', 20],
                ['B', 'C', 50],
                ['D', 'C', 70]
            ], 'D', 'C'],
            "answer": 60,
            "explanation": "D->A(20)->C(40)"
        },
        {
            "input": [[
                ['A', 'C', 100],
                ['A', 'B', 20],
                ['D', 'F', 900]
            ], 'A', 'F'],
            "answer": 0,
            "explanation": "no connection"
        },
        {
            "input": [[
                ['A', 'B', 10],
                ['A', 'C', 15],
                ['B', 'D', 15],
                ['C', 'D', 10]
            ], 'A', 'D'],
            "answer": 25,
            "explanation": "A->B(10)->D(15) || A->C(15)->D(10)"
        }
    ],
    "Extra": [
        {
            "input": [[
                ['A', 'B', 10],
                ['A', 'C', 20],
                ['B', 'D', 15],
                ['C', 'D', 5],
                ['D', 'E', 5],
                ['E', 'F', 10],
                ['C', 'F', 25]
            ], 'A', 'F'],
            "answer": 40,
            "explanation": "A->B(10)->D(15)->E(5)->F(10)"
        }
    ]
}
