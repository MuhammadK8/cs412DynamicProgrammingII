# Rocket Sections - Iterative

## Project Overview
"Rocket Sections" is a Python project that exemplifies a sophisticated transition from recursive to iterative dynamic programming. This project is tailored to address a specific problem using iterative dynamic programming techniques, focusing on optimizing both the space and time complexity of the solution. This approach is critical in high-performance computing environments, such as those encountered in FAANG companies, where efficient algorithmic solutions are essential.


# Original Writeup

In order to identify budding rocket science talent, SpaceX has designed a new modular build-your-own rocket kit for amateur rocketeers to use to construct model rockets. After careful user-studies, SpaceX has found that its customers want to be able to build rockets of widely varying height. Thus, they've arrived at the following idea. Instead of selling rocket fuselage tubing at every height desired by their customers, they'll offer an array of rocket "sections" at varying heights that can be fit together to form a full sized rocket. For example, for the Lil Falcons parts (their entry level kit for preschoolers, that comes complete with a mix your own rocket fuel kit and size 3T smocks) they offer rocket sections in the following sizes: 1 inch, 2 inch  5 inch, and 7 inch sections.

In order to build a rocket of height 15, a kinderscientist could use two 5" sections, two 2" sections, and one 1" section for a total of five sections. Or three 5" sections for a total of three sections. Obviously, construction is made more complicated by the number of sections that need to be arc welded together (there's a companion Kids-Do-Welding TM starter kit made by Hasbro for the preschooler who hasn't gotten started welding yet). The goal of any good rocket designer is to minimize the number of sections used in the construction of their rocket. 

* Input:
The input to the program will be a line containing a space separated, sorted list of the n lengths of available rocket sections for a given kit. The second line will be a single integer representing the length of rocket the user wants to construct. The first line will always include a part of length 1, meaning that all requested lengths can be constructed.

* Sample Output:
<img width="574" alt="image" src="https://github.com/MuhammadK8/cs412RocketSectionsIterative/assets/144934871/6b3b1126-55f9-4a0b-9923-52cb24ba3d59">

# Preview
![RocketSectionsPreview](https://github.com/MuhammadK8/cs412RocketSectionsIterative/assets/144934871/913a6fea-e553-49f2-b661-19dca4e87e18)


---
### Strategic Transition to Iterative Solutions
The project's main innovation lies in converting a recursive dynamic programming solution into an iterative one. This shift is significant in the realm of algorithm design, as iterative solutions are often more efficient than their recursive counterparts, particularly in terms of memory usage and execution speed. These qualities are paramount in high-performance computing environments where resources are at a premium, and efficiency is key.

## Detailed Programming Skills Showcased
- **Deep Understanding of Dynamic Programming**: Demonstrates a profound grasp of dynamic programming principles, skillfully applying them in an iterative context. This understanding is crucial in FAANG companies where dynamic programming is often used to solve complex problems efficiently.
- **Algorithm Optimization**: The project showcases the ability to refine the dynamic programming phase for enhanced performance. This skill is highly valued in tech firms, where optimizing existing algorithms for better efficiency can lead to significant improvements in application performance.
- **Problem-Solving and Code Refactoring**: Involves rethinking and redesigning the solution approach, highlighting advanced problem-solving skills. Refactoring for better performance and maintainability is a common requirement in large-scale software projects, as often encountered in FAANG environments.
- **Efficient Memory Management**: Demonstrates efficient handling of memory in the iterative phase of dynamic programming, a critical aspect in environments where large datasets are the norm, and optimal memory usage is crucial.

## Code Snippets and Examples

### Iterative Dynamic Programming Function
The `blocks_solver` function represents the transition from recursive to iterative dynamic programming. It shows the implementation of a table-based approach to store and utilize computed values, a method that is both memory-efficient and fast, qualities that are highly sought after in systems designed by FAANG companies.

```python
def blocks_solver(blocks, total_target):
    factor = reduce(gcd, blocks)
    new_target, remainder = divmod(total_target, factor)
    if remainder:
        raise ValueError("Cannot make the target with the given blocks")
    blocks = [block // factor for block in blocks]

    # Dynamic programming phase
    memo = [(0, None)] + [None] * new_target
    for target in range(1, new_target + 1):
        min_ans = float('inf')
        min_idx = None
        for idx in range(len(blocks) - 1, -1, -1):
            next_target = target - blocks[idx]
            if next_target < 0:
                continue
            ans, _ = memo[next_target]
            if ans < min_ans:
                min_ans = ans
                min_idx = idx

        ret = (min_ans + 1, min_idx)
        memo[target] = ret

    total_blocks, next_block = memo[new_target]
    if total_blocks == float("inf"):
        raise ValueError("Cannot make the target with the given blocks")

    # Solution building phase
    counts = [0] * len(blocks)
    remaining_target = new_target
    while next_block is not None:
        remaining_target -= blocks[next_block]
        counts[next_block] += 1
        _, next_block = memo[remaining_target]

    return total_blocks, counts
```

## Challenges and Learning

### Transition from Recursive to Iterative
- **Complexity Management**: The project involved intricately managing state and intermediate results in the absence of the natural stack of recursive calls. This is a skill highly valued in tech firms, where understanding and optimizing algorithmic complexity can lead to substantial performance gains.
- **Optimization**: The focus on ensuring the iterative solution's correctness and efficiency in terms of time and space complexity aligns with the performance optimization goals in FAANG companies.

### Skills Enhancement
- **Algorithmic Flexibility**: The ability to switch between recursive and iterative paradigms, as demonstrated in this project, is a key skill in software engineering, particularly in solving complex algorithmic problems typical in FAANG companies.
- **Code Efficiency**: Improving efficiency by reducing call stack overhead is critical in large-scale systems, a common challenge in dynamic programming problems, and a skill highly regarded in the industry.

## Conclusion
"Rocket Sections" showcases high-level programming proficiency, particularly in the realms of dynamic programming, algorithm optimization, and problem-solving. It aligns with the standards expected in top-tier tech companies and illustrates the ability to tackle complex algorithmic challenges. This project could be a decisive factor in demonstrating the candidate’s readiness for high-stakes, performance-critical software development roles in environments such as FAANG companies. Future enhancements could involve further optimizations or applying these techniques to more complex dynamic programming challenges, continuing to push the frontiers of algorithmic efficiency and sophistication.
