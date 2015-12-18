# Topic Search With Twitter and Wiki

This is a lightweight app that allows users to search their interested topics in Twitter and Wikipedia.

## How to use it?

Type in the topic of your interest in the search text box and click 'Search' button. You will be directed into a
search result page. 

Refresh the page will update the page with the latest results for the same search term.

## Performance Profile

On my local dev environment, a normal search result page will be rendered in about 10 seconds. So the performance is
not very satisfactory. Most of the time is used by waiting for response from the two search apis, especially wikipedia api, 
because the content can be long.

To reduce the bottlenecks. Two things can be used, caching can be used to store recent user search results, so the 
time to wait for api responses can be reduced in certain circumstances.

Concurrency may also be used to so queries can be done at the same time.

## Tests

The app code base contains higher level functional tests and lower level unit tests

To test functional tests, run

```
python manage.py test functional_tests
```

To test unit tests, run

```
python manage.py test topic_search
```

## Future improvements:

- Allow users to check a box and limit results to those near them

- Track terms searched by users and visualize statistics




