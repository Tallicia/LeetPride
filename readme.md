
# LeetPride


# To make algorithm and data structure learning more exciting, colorful and enjoyable.

LeetPride interrogates the created classes and 
runs the tests specified to ensure success and optimize focus on problem
solving maximizing data structure an algorithm absorption.

simply install with 
```pip install leetpride```

[LeetPride depends on modules listed in requirements.txt](requirements.txt)

It is recommended to create a venv and install the requirements.
```
python3 -m venv venv
./venv/scripts/activate
python3 -m pip install -U pip
python3 -m pip install -r requirements.txt 
```

>Then quickly get going quickly with a typical py file to begin coding solutions 
with and import and common python boilerplate for generating and running tests on solutions.
>
>There are simple setups to get going in seconds. Also, there are capabilities to easily 
test and time multiple method implementations and different class method call sequencing for
class testing. 

```from leetpridecore import *```

<h2>For either -method- or -class- solutions:</h2>
Class - class questions generally entail verifying output of sequenced method calls:
```
class Pride:
    def __init__(self, always)
        self.love = always
     
    def love(sef, equality:str = 'forever') -> bool:
        return self.love == True
```

Method - general class Solution, so to align with LC practices:
```
class Solution:
    # @timeit
    def method1(self, nums: List[int], target: int) -> List[int | None]:
        return [nums[target]]
```

Example of required generate_tests() method using separate tests and
expected results zipped together: 
``` 
def generate_tests():
    tests = (['Pride', 'loving', ],
             ['forever !',
              None,
              ])
    expected_test_results = [True, 'LGBTQ Lover forever !!!!', ]

    return list(zip(tests[0], tests[1], expected_test_results))
```

[Examples can be found in the Examples Folder](Examples)

> The standard main for running Class and Method solution tests is as follows:



```
def main() -> Optional[int] | None:
    tests_unified = generate_tests()
    lpc = LeetPrideCore(time_all=True)
    lpc.solution_hash_display(tests_unified)
    any_fail = lpc.run_tests(tests_unified)
    return completion_display(any_fail)


if __name__ == '__main__':
    exit(main())
    
```

# A few notes:
Instantiating the LeetCodeCore object takes an optional time_all bool parameter.
-- If enabled to True, this will dynamically wrap any non @timeit wrapped methods
designated for testing with a @timeit decorator and provide timing
duration information detail.


