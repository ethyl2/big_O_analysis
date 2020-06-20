# Big O Analysis Practice

This repo contains some example files to practice determining big O time and space complexity.

It also contains a few visualizations.

I would suggest looking at the examples in random order.

---

In order to run the visualizations, you need matplotlib.

Your setup may differ. Here's how I do it:

In terminal:

```
pipenv install
pipenv shell
pip install matplotlib
```

---

I would love to add more examples. This is just a start.

**Please send me a pull request if you have more examples to add.** Thank you!

---

# A little about what Big O is:

## As far as time complexity goes:

"Big O notation is the language we use to describe the complexity of an algorithm. In other words, Big O notation is the language we use for talking about how long an algorithm takes to run. It is how we compare the efficiency of different approaches to a problem. With Big O notation we express the runtime in terms of how quickly it grows relative to the input, as the input gets larger."

from https://medium.com/karuna-sehgal/a-simplified-explanation-of-the-big-o-notation-82523585e835#:~:text=In%20other%20words%2C%20Big%20O,as%20the%20input%20gets%20larger%20.

With Big O, we talk about the worst-case scenerios.

## As far as space complexity goes:

Similar to time, except that we look at memory (or space cost). We look at which additional memory is needed (besides what is needed for the inputs) as the input gets larger.
