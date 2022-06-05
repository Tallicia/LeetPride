<h1 style = font-size:80px>
<div style="text-align: center;">
<span style="color:purple">L</span>
<span style="color:violet">e</span>
<span style="color:blue">e</span>
<span style="color:green">t</span>
<span style="color:yellow">P</span>
<span style="color:orange">r</span>
<span style="color:orange">i</span>
<span style="color:red">d</span>
<span style="color:violet">e</span>
</div>
</h1>


# To make algorithm and data structure learning more exciting, colorful and enjoyable.

LeetPride interrogates the created classes and 
runs the tests specified to ensure success and optimize focus on problem-solving maximizing data structure an algorithm absorption.

><h3>One time Setup</h3>
>>simply install with 
```pip install leetpride```
>
>[LeetPride depends on modules listed in requirements.txt](requirements.txt)
>
>It is recommended to create a venv and install the requirements.
>>
>>```
>>    python3 -m venv venv
>>    ./venv/scripts/activate
>>    python3 -m pip install -U pip
>>    python3 -m pip install -r requirements.txt 
>>

Screenshot of the 4 simple steps running in seconds.
![img](Examples/LeetPride-001.png)

>><h3>Happy Problem Solving</h3>
>>Then quickly get going given any problem with a typical py file to begin coding solutions 
with and import and common python boilerplate for generating and running tests on solutions.
>>
>>There are 4 basic simple setups to get going in seconds. THe 2nd is just boilerplate that 
> will be replaced as you solve a problem. Also, there are capabilities to easily 
test and time multiple method implementations and different class method call sequencing for
class testing. 

<ol>
<li>

    from leetpridecore import *
</li>

<li>

>> The standard main for running Class and Method solution tests is as follows:

    def main() -> Optional[int] | None:
        tests_unified = generate_tests()
        lpc = LeetPrideCore(time_all=True)
        lpc.solution_hash_display(tests_unified)
        any_fail = lpc.run_tests(tests_unified)
        return completion_display(any_fail)
    if __name__ == '__main__':
        exit(main())
</li>

<li>

>>[Multiple examples can be found in the /Examples folder of test generation simplicity and support for complex cases.](Examples)
>
>>Example of required generate_tests() method using separate tests and
expected results zipped together: 

 
    def generate_tests():
        tests = (['Pride', 'loving', ],
                 ['forever !',
                  None,
                  ])
        expected_test_results = [True, 'LGBTQ Lover forever !!!!', ]
    return list(zip(tests[0], tests[1], expected_test_results))
</li>

<h2>For either -method- or -class- solutions:</h2>
<li>

> >
>><ul>
>>A or B ( but supports mixing too even. )
>A. Class - class questions generally entail verifying output of sequenced method calls:
>
>

    class Pride:
        def __init__(self, always)
            self.love = always
         
        def love(sef, equality:str = 'forever') -> bool:
            return self.love == True
></ul>
><ul>
>B. Method - general class Solution, so to align with LC practices:
>
>


    class Solution:
        # @timeit
        def method1(self, nums: List[int], target: int) -> List[int | None]:
            return [nums[target]]
</ul>
</li>

</ol>

# A few notes:
Instantiating the LeetCodeCore object takes an optional time_all bool parameter.
-- If enabled to True, this will dynamically wrap any non @timeit wrapped methods
designated for testing with a @timeit decorator and provide timing
duration information detail.

Graphies and Linkies helper methods for easy test setup and printout of
representations of node graphs, trees, and linked lists 
are being cleaned up and will be included in very near term update.

Enjoy!
<br>
Tallicia
