# FAQ about Big O

Q: Why do we focus on the growth of runtime versus exact runtime?

A: "The exact runtime is dependent on the specific computer that is running the algorithm, so we cannot compare efficiencies that way. By focusing on the general growth, we can avoid the differences in exact runtime between machines and environments."

source: https://learn.lambdaschool.com/cs/module/reck76SPX26beGSqE/

---

Q: Why do we talk about runtime relative to the input size?

A: "We talk about runtime relative to the input size because we need to express our speed in terms of something. So we show the speed of the algorithm in terms of the input size. That way, we can see how the speed reacts as the input size grows."

source: https://learn.lambdaschool.com/cs/module/reck76SPX26beGSqE/

---

Q: Why do we care about the differences in input sizes?

A: We focus on what happens when the input get extremely large. "The differences in speed are likely to be minimal when the input size is small. When the input size gets enormous, that is where we can see the differences in efficiency between different algorithms."

source: https://learn.lambdaschool.com/cs/module/reck76SPX26beGSqE/

---

Q: Do constants ever matter?

A: Not officially when determining the official Big O notation of an algorithm. That said, "just because two algorithms have the same Big O notation doesn’t mean they are equal."

An example where it might be wise to consider the constants:

"Imagine you have a script that takes 1 hour to run. By improving the function, you can divide that runtime by six, and now it only takes 10 minutes to run. With Big O notation, O(n) and O(n/6) can both be written as O(n), but that doesn’t mean it isn’t worth optimizing the script to save 50 minutes every time the script runs."

source: https://learn.lambdaschool.com/cs/module/reck76SPX26beGSqE/
